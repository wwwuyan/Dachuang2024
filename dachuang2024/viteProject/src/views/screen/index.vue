<template>
  <div class="background">
    <div class="top">
      <h1 class="title">医疗数据可视化大屏</h1>
      <div style="transform: translateX(32vw); display: flex; margin: 1vh">
        <el-button
          @click="gotoHome"
          color="#ff7070"
          :icon="SwitchButton"
          circle
        />
        <div style="color: #f56c6c; margin: 1vh 0.5vw">退出</div>
      </div>
    </div>
    <div class="content">
      <div class="left">
        <div id="showleft1" class="left1"></div>
        <div id="showleft3" class="left3"></div>
      </div>
      <div class="center">
        <div class="center1">
          <div class="center11">
            <div class="zhongzuo">
              <div class="text1">主任医师门诊人次</div>
              <div style="display: flex">
                <div class="text2">230</div>
                <div class="text3increase">+15%</div>
              </div>
            </div>
            <div class="zhongzuo">
              <div class="text1">副主任医师门诊人次</div>
              <div style="display: flex">
                <div class="text2">450</div>
                <div class="text3decrease">-10%</div>
              </div>
            </div>
            <div class="zhongzuo">
              <div class="text1">主治医师门诊人次</div>
              <div style="display: flex">
                <div class="text2">366</div>
                <div class="text3increase">+22%</div>
              </div>
            </div>
            <div class="zhongzuo">
              <div class="text1">住院医师门诊人次</div>
              <div style="display: flex">
                <div class="text2">140</div>
                <div class="text3decrease">-8%</div>
              </div>
            </div>
          </div>
          <div id="showcenter12" class="center12"></div>
        </div>
        <div id="showcenter2" class="center2"></div>
      </div>
      <div class="right">
        <div class="right1">
          <div class="things">科室就诊量一览表</div>
          <el-table
            :data="tableData2"
            border
            stripe
            size="small"
            style="width: 100%"
            height="280"
          >
            <el-table-column prop="num" label="序号" width="50" />
            <el-table-column prop="room" label="科室" width="90" />
            <el-table-column prop="people" label="门诊人次" width="90" />
            <el-table-column prop="rate" label="同比增幅" width="90" />
            <el-table-column prop="satisfy" label="综合满意度" width="90" />
          </el-table>
        </div>
        <div class="right2">
          <div class="things">患者信息评估列表</div>
          <el-table :data="tableData1" border stripe size="small" height="340">
            <el-table-column prop="num" label="序号" width="50" />
            <el-table-column prop="card" label="卡号" width="80" />
            <el-table-column prop="name" label="姓名" width="80" />
            <el-table-column prop="room" label="科室" width="80" />
            <el-table-column prop="index" label="指标" width="50" />
            <el-table-column prop="risk" label="风险系数" width="70" />
          </el-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import * as echarts from "echarts";
import { SwitchButton } from "@element-plus/icons-vue";
import { onMounted } from "vue";
import { useRouter } from "vue-router";

let $router = useRouter();

const gotoHome = () => {
  $router.push("/home");
};

const tableData2 = [
  {
    num: "01",
    room: "外科",
    people: "70",
    rate: "7.2%",
    satisfy: "85%",
  },
  {
    num: "02",
    room: "内科",
    people: "62",
    rate: "16.4%",
    satisfy: "83%",
  },
  {
    num: "03",
    room: "儿科",
    people: "45",
    rate: "4.8%",
    satisfy: "77%",
  },
  {
    num: "04",
    room: "眼科",
    people: "30",
    rate: "7%",
    satisfy: "89%",
  },
  {
    num: "05",
    room: "耳鼻喉科",
    people: "28",
    rate: "25%",
    satisfy: "82%",
  },
  {
    num: "06",
    room: "妇科",
    people: "20",
    rate: "27%",
    satisfy: "88%",
  },
  {
    num: "07",
    room: "产科",
    people: "18",
    rate: "-17%",
    satisfy: "85%",
  },
  {
    num: "08",
    room: "肿瘤科",
    people: "10",
    rate: "-33%",
    satisfy: "86%",
  },
];
const tableData1 = [
  {
    num: "01",
    card: "240807",
    name: "王某某",
    room: "眼科",
    index: "8",
    risk: "75%",
  },
  {
    num: "02",
    card: "240808",
    name: "赵某某",
    room: "内科",
    index: "10",
    risk: "90%",
  },
  {
    num: "03",
    card: "240809",
    name: "李某某",
    room: "外科",
    index: "12",
    risk: "88%",
  },
  {
    num: "04",
    card: "240810",
    name: "张某某",
    room: "骨科",
    index: "6",
    risk: "68%",
  },
  {
    num: "05",
    card: "240811",
    name: "陈某某",
    room: "内科",
    index: "6",
    risk: "25%",
  },
  {
    num: "06",
    card: "240812",
    name: "郑某某",
    room: "口腔科",
    index: "4",
    risk: "36%",
  },
  {
    num: "07",
    card: "240813",
    name: "汪某某",
    room: "儿科",
    index: "5",
    risk: "67%",
  },
  {
    num: "08",
    card: "240814",
    name: "李某某",
    room: "内科",
    index: "9",
    risk: "82%",
  },

  {
    num: "09",
    card: "240815",
    name: "王某某",
    room: "内科",
    index: "6",
    risk: "45%",
  },

  {
    num: "10",
    card: "240816",
    name: "朱某某",
    room: "儿科",
    index: "5",
    risk: "93%",
  },

  {
    num: "11",
    card: "240807",
    name: "王某某",
    room: "眼科",
    index: "8",
    risk: "75%",
  },
  {
    num: "12",
    card: "240808",
    name: "赵某某",
    room: "内科",
    index: "10",
    risk: "90%",
  },
  {
    num: "13",
    card: "240809",
    name: "李某某",
    room: "外科",
    index: "12",
    risk: "88%",
  },
  {
    num: "14",
    card: "240810",
    name: "张某某",
    room: "骨科",
    index: "6",
    risk: "68%",
  },
  {
    num: "15",
    card: "240811",
    name: "陈某某",
    room: "内科",
    index: "6",
    risk: "25%",
  },
  {
    num: "16",
    card: "240812",
    name: "郑某某",
    room: "口腔科",
    index: "4",
    risk: "36%",
  },
  {
    num: "17",
    card: "240813",
    name: "汪某某",
    room: "儿科",
    index: "5",
    risk: "67%",
  },
  {
    num: "18",
    card: "240814",
    name: "李某某",
    room: "内科",
    index: "9",
    risk: "82%",
  },

  {
    num: "19",
    card: "240815",
    name: "王某某",
    room: "内科",
    index: "6",
    risk: "45%",
  },

  {
    num: "20",
    card: "240816",
    name: "朱某某",
    room: "儿科",
    index: "5",
    risk: "93%",
  },
];

type EChartsOption = echarts.EChartsOption;
const showcenter2 = () => {
  var app: any = {};
  var chartDom: any = document.getElementById("showcenter2");
  chartDom.removeAttribute("_echarts_instance_");
  var myChart = echarts.init(chartDom);

  var option;

  const categories = (function () {
    let now = new Date();
    let res = [];
    let len = 10;
    while (len--) {
      res.unshift(now.toLocaleTimeString().replace(/^\D*/, ""));
      now = new Date(+now - 2000);
    }
    return res;
  })();
  const categories2 = (function () {
    let res = [];
    let len = 10;
    while (len--) {
      res.push(10 - len - 1);
    }
    return res;
  })();
  const data = (function () {
    let res = [];
    let len = 10;
    while (len--) {
      res.push(Math.round(Math.random() * 100+20));
    }
    return res;
  })();
  const data2 = (function () {
    let res = [];
    let len = 0;
    while (len < 10) {
      res.push(+(Math.random() * 10 + 5).toFixed(1));
      len++;
    }
    return res;
  })();
  option = {
    title: {
      text: "今日就诊量动态图",
    },
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "cross",
        label: {
          backgroundColor: "#283b56",
        },
      },
    },
    grid: {
      bottom: 40,
    },
    legend: {},
    toolbox: {
      show: false,
      feature: {
        dataView: { readOnly: false },
        restore: {},
        saveAsImage: {},
      },
    },
    dataZoom: {
      show: false,
      start: 0,
      end: 100,
    },
    xAxis: [
      {
        type: "category",
        boundaryGap: true,
        data: categories,
      },
      {
        type: "category",
        boundaryGap: true,
        data: categories2,
      },
    ],
    yAxis: [
      {
        type: "value",
        scale: true,
        name: "急诊流量",
        max: 30,
        min: 0,
        boundaryGap: [0.2, 0.2],
      },
      {
        type: "value",
        scale: true,
        name: "门诊流量",
        max: 120,
        min: 0,
        boundaryGap: [0.2, 0.2],
      },
    ],
    series: [
      {
        name: "门诊流量",
        type: "bar",
        xAxisIndex: 1,
        yAxisIndex: 1,
        data: data,
      },
      {
        name: "急诊流量",
        type: "line",
        data: data2,
      },
    ],
  };
  app.count = 11;
  setInterval(function () {
    let axisData = new Date().toLocaleTimeString().replace(/^\D*/, "");
    data.shift();
    data.push(Math.round(Math.random() * 100 + 20));
    data2.shift();
    data2.push(+(Math.random() * 10 + 5).toFixed(0));
    categories.shift();
    categories.push(axisData);
    categories2.shift();
    categories2.push(app.count++);
    myChart.setOption({
      xAxis: [
        {
          data: categories,
        },
        {
          data: categories2,
        },
      ],
      series: [
        {
          data: data,
        },
        {
          data: data2,
        },
      ],
    });
  }, 2100);

  option && myChart.setOption(option);
};

const showcenter12 = () => {
  var chartDom: any = document.getElementById("showcenter12");
  chartDom.removeAttribute("_echarts_instance_");
  var myChart = echarts.init(chartDom);
  var option: EChartsOption;

  option = {
    title: {
      text: "科室就诊量分布图",
      left: "left",
    },
    tooltip: {
      trigger: "item",
    },
    legend: {
      orient: "vertical",
      left: 350,
      top: 60,
    },
    series: [
      {
        name: "科室就诊量",
        type: "pie",
        radius: [70, 140],
        center: ["37%", "53%"],
        avoidLabelOverlap: false,
        padAngle: 2,
        itemStyle: {
          borderRadius: 6,
        },
        label: {
          show: false,
          position: "center",
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 40,
            fontWeight: "bold",
          },
        },
        labelLine: {
          show: false,
        },
        data: [
          { value: 70, name: "外科" },
          { value: 62, name: "内科" },
          { value: 45, name: "儿科" },
          { value: 30, name: "眼科" },
          { value: 28, name: "耳鼻喉科" },
          { value: 20, name: "妇科" },
          { value: 18, name: "产科" },
          { value: 10, name: "肿瘤科" },
        ],
        
      },
    ],
  };
 
  option && myChart.setOption(option);
  
};
const showleft3 = () => {
  var chartDom: any = document.getElementById("showleft3");
  chartDom.removeAttribute("_echarts_instance_");
  var myChart = echarts.init(chartDom);
  var option;

  option = {
    title: {
      text: "手术情况统计表",
      left: "left",
    },
    legend: { orient: "vertical", left: 300, top: 50 },
    tooltip: {},
    grid: {
      bottom: "10%",
    },
    dataset: {
      source: [
        ["product", "去年同期", "本月", "上月"],
        ["一级手术", 300, 260, 280],
        ["二级手术", 207, 176, 184],
        ["三级手术", 157, 170, 130],
        ["四级手术", 80, 60, 40],
      ],
    },
    xAxis: { type: "category" },
    yAxis: { max: 300 },
    // Declare several bar series, each will be mapped
    // to a column of dataset.source by default.
    series: [{ type: "bar" }, { type: "bar" }, { type: "bar" }],
  };

  option && myChart.setOption(option);
};
const showleft1 = () => {
  var chartDom: any = document.getElementById("showleft1");
  chartDom.removeAttribute("_echarts_instance_");
  var myChart = echarts.init(chartDom);
  var option: EChartsOption;

  option = {
    title: {
      text: "今日就诊患者性别年龄分布图",
      left: "left",
    },
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b}: {c} ({d}%)",
    },
    legend: {
      orient: "vertical",
      left: 300,
      bottom: 50,
      data: [
        "80岁以上",
        "70-80岁",
        "60-70岁",
        "50-60岁",
        "40-50岁",
        "30-40岁",
        "20-30岁",
        "10-20岁",
        "0-10岁",
      ],
    },

    series: [
      {
        name: "性别",
        type: "pie",
        selectedMode: "single",
        center: ["35%", "55%"],
        radius: [0, "30%"],
        data: [
          { value: 1048, name: "女" },
          { value: 775, name: "男" },
        ],
        label: {
          position: "inner",
        },
        labelLine: {
          show: false,
        },
      },

      {
        name: "年龄范围",
        type: "pie",
        center: ["35%", "55%"],
        radius: ["40%", "85%"],

        data: [
          { value: 153, name: "80岁以上" },
          { value: 256, name: "70-80岁" },
          { value: 310, name: "60-70岁" },
          { value: 251, name: "50-60岁" },
          { value: 180, name: "40-50岁" },
          { value: 120, name: "30-40岁" },
          { value: 50, name: "20-30岁" },
          { value: 23, name: "10-20岁" },
          { value: 24, name: "0-10岁" },
        ],
        label: {
          position: "inner",
        },
        labelLine: {
          show: false,
        },
      },
    ],
  };

  option && myChart.setOption(option);
};

//*** 挂载Echarts
onMounted(() => {
  showcenter2();
  showcenter12();
  showleft3();
  showleft1();
});
</script>

<style scoped>
.background {
  background-color: #343a3f;
  overflow: hidden;
}
.top {
  width: 100vw;
  height: 9vh;
  display: flex;
  justify-content: center;
  padding: 2vh;
  .title {
    font-size: 30px;
    font-weight: 600;
    /* background: linear-gradient(to bottom, #00ffff, #13215c); */
    background: linear-gradient(to bottom, #5c7bd9, white);

    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
}
.content {
  width: 100vw;
  height: 91vh;
  padding: 0 30px;

  display: flex;
  .left {
    width: 25vw;
    .left1 {
      height: 40vh;
      margin: 0.5vh;
      box-shadow: 0 0 5px black;
      padding: 0.5vh;
      background-color: #f5f7fb;
      border-radius: 5px;
    }
    .left1:hover {
      background-color: #f0f0f5;
    }
    .left3 {
      height: 47.5vh;
      margin: 1vh 0.5vh 1vh 0.5vh;
      box-shadow: 0 0 5px black;
      padding: 0.5vh;
      background-color: #f5f7fb;
      border-radius: 5px;
    }
    .left3:hover {
      background-color: #f0f0f5;
    }
  }
  .center {
    width: 46vw;
    padding: 0.5vh;
    .center1 {
      height: 42vh;
      display: flex;

      .center11 {
        width: 19vw;
        margin: 0 0.5vh 0.5vh 0;
        box-shadow: 0 0 5px black;
        padding: 0.5vh;
        background-color: #f5f7fb;
        border-radius: 5px;
        .zhongzuo {
          height: 9vh;
          margin: 1vh;
          border-radius: 1vh;
          box-shadow: 0 0 10px grey;
          .text1 {
            padding: 1vh;
            text-align: center;
            font-size: 20px;
            font-weight: 600;
          }
          .text2 {
            padding: 0 0 0 2.5vw;
            width: 60%;
            text-align: center;
            font-size: 30px;
            font-weight: 1000;
            background: linear-gradient(to bottom, #ff9800, #eae60e);

            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
          }

          .text3increase {
            padding: 0.5vh 5vw 0 0;
            width: 40%;
            text-align: center;
            font-size: 20px;
            font-weight: 600;
            background: linear-gradient(to bottom, #c6a236, #e1483c);

            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
          }
          .text3decrease {
            padding: 0.5vh 5vw 0 0;
            width: 40%;
            text-align: center;
            font-size: 20px;
            font-weight: 600;
            background: linear-gradient(to bottom, #36dfe4, #d5f9c9);

            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
          }
        }
        .zhongzuo:hover {
          background-color: #f0f0f5;
        }
      }
      .center12 {
        width: 29vw;
        margin: 0 0 0.5vh 0.5vh;
        box-shadow: 0 0 5px black;
        padding: 0.5vh;
        background-color: #f5f7fb;
        border-radius: 5px;
      }
      .center12:hover {
        background-color: #f0f0f5;
      }
    }

    .center2 {
      height: 46vh;
      margin: 0.5vh 0 0.5vh 0;
      box-shadow: 0 0 5px black;
      padding: 0.5vh;
      background-color: #f5f7fb;
      border-radius: 5px;
    }
    .center2:hover {
      background-color: #f0f0f5;
    }
  }
  .right {
    width: 25vw;

    .right1 {
      height: 40vh;
      margin: 0.5vh;
      box-shadow: 0 0 5px black;
      padding: 0.5vh;
      background-color: #f5f7fb;
      border-radius: 5px;
    }
    .right1:hover {
      background-color: #f0f0f5;
    }
    .right2 {
      height: 47.5vh;
      margin: 1vh 0.5vh 1vh 0.5vh;
      box-shadow: 0 0 5px black;
      padding: 0.5vh;
      background-color: #f5f7fb;
      border-radius: 5px;
    }
    .right2:hover {
      background-color: #f0f0f5;
    }
  }
}
.things {
  margin: 0 0 1vh 0;
  color: #464646;
  font-weight: 600;
  font-size: 16px;
}
</style>
