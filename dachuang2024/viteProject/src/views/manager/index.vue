<template>
  <div>
    <div class="page_content">
      <div class="flex" style="margin: 0 0 20px 0">
        <div class="input_box">
          <el-input
            v-model="input"
            placeholder="搜索关键字"
            class="input-with-select"
          >
            <template #append>
              <el-button
                type="primary"
                icon="el-icon-search"
                @click.prevent="searchUser"
                >搜索</el-button
              >
            </template>
          </el-input>
        </div>
      </div>
      <el-table
        :data="
          userList.slice((currentPage - 1) * pageSize, currentPage * pageSize)
        "
        style="width: 100%; "
      >
        <el-table-column prop="id" label="编号"> </el-table-column>

        <el-table-column prop="name" label="姓名"> </el-table-column>

        <el-table-column prop="department" label="就诊科室"> </el-table-column>

        <el-table-column label="病历详情">
          <template #default="scope">
            <el-button slot="reference" @click="fetchFeedback(scope.row)"
              >查看详细</el-button
            >
          </template>
        </el-table-column>

        <el-table-column label="处理状态" prop="is_solved">
          <template v-slot="{ row }">
            <el-switch v-model="row.is_solved" disabled />
          </template>
        </el-table-column>
      </el-table>

      <el-dialog v-model="visible" title="病历详情" width="800">
        <el-form :model="patientDetail">
          <el-form-item>
            
              <el-table :data="tableData" border style="width: 100%">
                <el-table-column prop="daihao" label="代号" />
                <el-table-column prop="name" label="项目名称"/>
                <el-table-column prop="jieguo" label="结果" />
                <el-table-column prop="fanwei" label="参考范围" />
                <el-table-column prop="danwei" label="单位" />
              </el-table>
            
          </el-form-item>
          <el-form-item label="诊断结果">
            <el-input
              v-model="patientDetail[0].description"
              autocomplete="off"
              type="textarea"
              :rows="4"
            />
          </el-form-item>
        </el-form>
        <template #footer>
          <div class="dialog-footer">
            <el-button @click="visible = false">取消</el-button>
            <el-button type="primary" @click="submitDiagnosis">
              确认
            </el-button>
          </div>
        </template>
      </el-dialog>
      <el-pagination
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage"
        :page-size="pageSize"
        layout="prev, pager, next, jumper"
        :total="totalItem"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, Ref } from "vue";
import axios from "axios";

const tableData = [
  {
    daihao: 'AST',
    name: '谷草转氨酶',
    jieguo: '35.7',
    fanwei:'0--40',
    danwei:'U/L',
  },
  {
    daihao: 'LDH',
    name: '乳酸脱氢酶',
    jieguo: '864.3',
    fanwei:'80--280',
    danwei:'U/L',
  },
  {
    daihao: 'CK',
    name: '肌酸激酶',
    jieguo: '77.1',
    fanwei:'24--195',
    danwei:'U/L',
  },
  {
    daihao: 'CK-MB',
    name: '肌酸酶同功酶',
    jieguo: '22.4',
    fanwei:'0--25',
    danwei:'U/L',
  },
  {
    daihao: 'MB%',
    name: 'CK-MB%',
    jieguo: '0.29',
    fanwei:'0.01--0.99',
    danwei:'%',
  },
  {
    daihao: 'cTnI',
    name: '心肌钙蛋白I',
    jieguo: '0.08',
    fanwei:'0--1.68',
    danwei:'ng/ML',
  },
  
]

interface PatientDetail {
  department: string;
  description: string;
  id: number;
  is_solved: boolean;
  name: string;
}
interface RowType {
  department: string;
  description: string;
  id: number;
  is_solved: boolean;
  name: string;
}

const currentPage = ref(1);
const pageSize = ref(10);
const totalItem = ref(0);
const input = ref("");
const userList = ref([]);
const patientDetail: Ref<PatientDetail[]> = ref([]);
const visible = ref(false) as Ref<boolean>;

const fetchUser = () => {
  axios.get("/api/patient").then((res) => {
    userList.value = res.data.data;
    totalItem.value = res.data.data.length;
  });
};

const searchUser = () => {
  const query = input.value;
  if (query !== "") {
    axios.get(`/api/patient/${query}`).then((res) => {
      if (res.data.status == "success") {
        userList.value = res.data.data;
        totalItem.value = res.data.data.length;
      } else {
        userList.value = [];
      }
    });
  }
};

const handleCurrentChange = (newPage: any) => {
  currentPage.value = newPage;
};

const fetchFeedback = (row: RowType) => {
  console.log(row.id);
  axios.get(`/api/patient/${row.id}`).then((res) => {
    console.log(res);
    visible.value = true;
    patientDetail.value = res.data.data;
    console.log(patientDetail.value);
  });
};

const submitDiagnosis = () => {
  console.log(patientDetail.value[0].description);
  const form = new FormData();
  form.append("description", patientDetail.value[0].description);
  axios.put(`/api/patient/${patientDetail.value[0].id}`, form).then((res) => {
    console.log(res);
  });
  visible.value = false;
  fetchUser();
};

onMounted(() => {
  fetchUser();
});
</script>

<style scoped></style>
