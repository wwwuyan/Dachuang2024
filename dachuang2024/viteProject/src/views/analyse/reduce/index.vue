<template>
  <div>
    <div>
      <el-upload
        ref="upload"
        class="upload-demo"
        drag
        action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
        :limit="1"
        :on-exceed="handleExceed"
        :auto-upload="false"
        :http-request="reduction"
      >
        <el-icon class="el-icon--upload"><Filter /></el-icon>
        <div class="el-upload__text">
          Drop file here or <em>click to upload</em>
        </div>
        <div class="el-upload__tip">
          limit 1 .csv file, new file will cover the old file
        </div>
      </el-upload>
    </div>
    <div>
      <el-button class="ml-3" type="primary" plain @click="submitDetail">
        点击上传
      </el-button>

      <el-button class="ml-3" style="margin-left: 10px" plain @click="detail">
        文件详情
      </el-button>

      <el-button
        class="ml-3"
        type="success"
        plain
        @click="dialogFormVisible = true"
      >
        立即筛选
      </el-button>

      <el-button
        class="ml-3"
        style="margin-left: 10px"
        plain
        @click="dialogImageVisible = true"
      >
        可视化结果
      </el-button>
    </div>
    <el-alert
      style="background-color: #f5f7fb; margin: 5px 0; padding: 0"
      title="上传后可查看文件详情"
      type="info"
      :closable="false"
      show-icon
    />
    <div style="margin-top: 10px">
      <el-table
        :default-sort="{ prop: 'date', order: 'descending' }"
        v-loading="loading"
        :data="tableData"
        height="400"
        border
        style="width: 100%"
      >
        <!-- <el-table-column v-if="form.anomalyNum !== ''"type="index" :index="indexMethod" /> -->
        <el-table-column
          v-for="(value, key) in header"
          :key="key"
          :prop="value"
          :label="value"
          sortable
        />
      </el-table>
    </div>

    <el-dialog
      v-model="dialogFormVisible"
      title="参数设置"
      width="500"
      text-align:
      center
    >
      <el-form :model="form">
        <el-form-item label="算法选择" text-align: left>
          <el-select
            v-model="form.algorithm"
            placeholder="请选择特征筛选算法(默认MNIFS算法)"
          >
            <el-option label="MNIFS(基于模糊邻域的属性约简)" value="mnifs" />
            <el-option label="PCA(主成分分析法)" value="pca" />
            <!-- <el-option label="KMEANS" value="kmeans" />
            <el-option label="GMM" value="gmm" /> -->
          </el-select>
        </el-form-item>
        <el-form-item label="MNIFS参数选择" text-align: left  v-if="form.algorithm === 'mnifs'">
          <el-input
            v-model="form.lammda"
            placeholder="请输入MNIFS参数"
            clearable
          />
        </el-form-item>
      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取消</el-button>
          <el-button type="primary" @click="submitreduction"> 确认 </el-button>
        </div>
      </template>
    </el-dialog>

    <el-dialog v-model="dialogTableVisible" title="文件详情" width="800">
      <el-table :data="detailData">
        <el-table-column property="name" label="文件名" width="350" />
        <el-table-column property="sampleSize" label="样本个数" />
        <el-table-column property="attributeNum" label="指标个数" />
      </el-table>
      <el-table
        :data="detailTableData"
        height="300"
        stripe
        border
        style="width: 100%; margin-top: 20px"
      >
        <el-table-column
          type="index"
          :index="indexMethod"
          :label="'id'"
          width="60"
        />
        <el-table-column
          v-for="(value, key) in detailHeader"
          :key="key"
          :prop="value"
          :label="value"
        />
      </el-table>
    </el-dialog>

    <el-dialog v-model="dialogImageVisible" title="可视化结果" width="700">
      <div class="demo-image">
        <div>
          <v-chart class="chart" :option="option" autoresize />
        </div>
      </div>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, Ref } from "vue";
import axios, { AxiosResponse } from "axios";
import { ElMessage } from "element-plus";
import { ElUpload } from "element-plus";
import { genFileId } from "element-plus";
import { Filter} from "@element-plus/icons-vue";
import type { UploadInstance, UploadProps, UploadRawFile } from "element-plus";
import { use } from "echarts/core";
import { BarChart } from 'echarts/charts'
import { GridComponent, TooltipComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'
import VChart from "vue-echarts";

use([GridComponent, BarChart, CanvasRenderer, TooltipComponent])

const loading = ref(false);
const detailLock = ref(false);
const reductionLock = ref(false);
const indexMethod = (index: number) => {
  return index + 1;
};
interface FormDataFile {
  file: File;
}

interface DetailData {
  name: string;
  attributeNum: string;
  sampleSize: string;
}

interface RowData {
  [key: string]: string;
}

const dialogTableVisible = ref(false) as Ref<boolean>;
const dialogFormVisible = ref(false) as Ref<boolean>;
const dialogImageVisible = ref(false) as Ref<boolean>;
const form = reactive({
  algorithm: "请选择特征筛选算法(默认MNIFS算法)",
  isFeatures: false,
  lammda: 0.4
});
const detailData: DetailData[] = reactive([
  {
    name: "",
    sampleSize: "",
    attributeNum: "",
  },
]);
const matrixData: any[] = [];
const tableData = ref<RowData[]>([]);
const detailMatrixData: any[] = [];
const detailTableData = ref<RowData[]>([]);
// const fit = 'fill'
// const url = 'http://localhost:5000/image/KFRAD_reduction.png'
const header = ref({}) as Ref<Record<string, string>>;
const detailHeader = ref({}) as Ref<Record<string, string>>;
// const tableRowClassName = ({ row }: { row: RowData; rowIndex: number }) => {
//   if (Number(row.result) == 0) {
//     return "error-row";
//   }
//   if (Number(row.result) == 1) {
//     return "success-row";
//   }
//   if (Number(row.result) == 2) {
//     return "warning-row";
//   }
// };
const upload = ref<UploadInstance>();
const option = ref({});

const reduction = (file: FormDataFile): any => {
  if (reductionLock.value) {
    let formData = new FormData();
    const isreduction = true;
    formData.append("file", file.file);
    formData.append("is_reduction", isreduction.toString()); // 添加额外的参数
    formData.append("algorithm", form.algorithm);
    formData.append("lammda", form.lammda.toString());
    dialogFormVisible.value = false;
    loading.value = true;
    postreduction(formData).then((res: AxiosResponse<any>) => {
      if (res.data.status == "success") {
        console.log(res.data);
        matrixData.splice(0);
        matrixData.push(...JSON.parse(res.data.data));
        tableData.value.splice(0);
        matrixData.forEach((item: any) => {
          let rowData: RowData = {};
          Object.keys(res.data.header).forEach((index: string) => {
            const key = res.data.header[index];
            let value = item[index];
            rowData[key] = value;
          });
          tableData.value.push(rowData);
        });
        console.log(tableData.value);
        loading.value = false;
        header.value = res.data.header;
        reductionLock.value = false;
        option.value = res.data.option;
      }
    });
  }
  if (detailLock.value) {
    let formData = new FormData();
    formData.append("file", file.file);
    postreduction(formData).then((res: AxiosResponse<any>) => {
      if (res.data.status == "success") {
        detailMatrixData.splice(0);
        detailMatrixData.push(...JSON.parse(res.data.detail_data));
        detailTableData.value.splice(0);
        detailMatrixData.forEach((item: any) => {
          let rowData: RowData = {};
          Object.keys(res.data.detail_header).forEach((index: string) => {
            const key = res.data.detail_header[index];
            let value = item[index];
            rowData[key] = value;
          });
          detailTableData.value.push(rowData);
        });
        ElMessage({
          message: "文件已成功上传",
          type: "success",
        });
        detailData[0].name = res.data.file;
        detailData[0].attributeNum = res.data.col_count;
        detailData[0].sampleSize = res.data.row_count;
        detailHeader.value = res.data.detail_header;
        tableData.value.splice(0);
      }
    });
    detailLock.value = false;
  }
};

const postreduction = (file: FormData) => {
  return axios({
    url: "/api/reduction",
    method: "post",
    data: file,
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};

const detail = (file: File | null) => {
  if (file) {
    dialogTableVisible.value = true;
  } else {
    ElMessage.error("未上传文件");
  }
};

const handleExceed: UploadProps["onExceed"] = (files) => {
  upload.value!.clearFiles();
  const file = files[0] as UploadRawFile;
  file.uid = genFileId();
  upload.value!.handleStart(file);
};

const submitDetail = () => {
  upload.value!.submit();
  detailLock.value = true;
};

const submitreduction = () => {
  upload.value!.submit();
  reductionLock.value = true;
};

</script>

<style>
.el-table .error-row {
  --el-table-tr-bg-color: var(--el-color-error-light-9);
}
.el-table .warning-row {
  --el-table-tr-bg-color: var(--el-color-warning-light-9);
}
.el-table .success-row {
  --el-table-tr-bg-color: var(--el-color-success-light-9);
}
.div_scatter {
  height: 50vh;
  width: 50vw;
}
.chart {
  height: 65vh;
}
</style>
