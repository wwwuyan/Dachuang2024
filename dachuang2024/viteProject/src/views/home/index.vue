<template>
  <el-card>
    <div class="box">
      <div class="user-circle">
        <img src="@/assets/icons/user.svg" style="height: 150px" />
      </div>
      <div class="text">
        <h3 class="title">欢迎回来，吴医生！</h3>
        <p class="subtitle">智融医诊平台</p>
        <p class="subtitle">融合模糊粒信息的医疗辅助诊断系统</p>
        <div class="buttonbox">
          <el-button type="success" plain :icon="Platform" size="large" @click="gotoPlat">数据智慧台</el-button>
          <el-button type="warning" plain :icon="Notebook" size="large" @click="gotoManager">数据管家</el-button><br><br>
          <el-button type="primary" plain :icon="Filter" size="large" @click="gotoFilter">特征筛选</el-button>
          <el-button type="primary" plain :icon="Aim" size="large" @click="gotoAim">异常检测</el-button>
          <el-button type="primary" plain :icon="View" size="large" @click="gotoView">辅助识别</el-button>
        </div>
      </div>

      <!--患者信息列表-->
      <div style="margin: 0px 0px 0px 0px">
        <div class="things">患者信息评估列表</div>
        <el-table
          :data="tableData"
          border
          stripe
          style="width: 100%"
          height="300"
        >
          <el-table-column prop="num" label="序号" width="100" />
          <el-table-column prop="card" label="卡号" width="100" />
          <el-table-column prop="name" label="姓名" width="100" />
          <el-table-column prop="room" label="科室" width="100" />
          <el-table-column prop="index" label="指标" width="100" />
          <el-table-column prop="risk" label="风险系数" width="100" />
        </el-table>
      </div>

      <!--代办事务-->
      <div style="margin: 0px 0px 30px 60px">
        <div class="things">待办事务</div>
        <el-timeline style="max-width: 600px">
          <el-timeline-item
            v-for="(activity, index) in activities"
            :key="index"
            :icon="activity.icon"
            :type="activity.type"
            :color="activity.color"
            :size="activity.size"
            :hollow="activity.hollow"
            :timestamp="activity.timestamp"
          >
            {{ activity.content }}
          </el-timeline-item>
        </el-timeline>
      </div>
    </div>
  </el-card>

  <!--走马灯-->
  <div style="margin: 60px 0 0 0">
    <el-carousel :interval="4000" type="card" height="250px">
      <el-carousel-item v-for="item in imglist" :key="item.id">
        <img
          style="object-fit: scale-down; width: 100%; height: 100%"
          :src="item.url"
        />
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script setup lang="ts">
import image1 from "@/assets/images/image1.png";
import image2 from "@/assets/images/image2.png";
import image3 from "@/assets/images/image3.png";
import image4 from "@/assets/images/image4.png";


import { Aim, Filter, MoreFilled, Platform, View, Notebook } from "@element-plus/icons-vue";
import { useRouter } from "vue-router";

let $router=useRouter()

const gotoPlat=()=>{
  $router.push('/screen')
}

const gotoFilter=()=>{
  $router.push('/analyse/reduce')
}

const gotoAim=()=>{
  $router.push('/analyse/detection')
}

const gotoView=()=>{
  $router.push('/analyse/classification')
}

const gotoManager=()=>{
  $router.push('/manager')
}
const tableData = [
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
];

const activities = [
  {
    content: "Custom icon",
    timestamp: "2024-04-12",
    size: "large",
    type: "primary",
    icon: MoreFilled,
  },
  {
    content: "Custom color",
    timestamp: "2024-04-13",
    color: "#0bbd87",
  },
  {
    content: "Custom size",
    timestamp: "2024-04-15",
    size: "large",
  },
  {
    content: "Custom hollow",
    timestamp: "2024-04-17",
    type: "primary",
    hollow: true,
  },
  {
    content: "Default node",
    timestamp: "2024-04-20",
  },
];

const imglist = [
  { id: 0, url: image1 },
  { id: 1, url: image2 },
  { id: 3, url: image3 },
  { id: 4, url: image4 },
];
</script>

<style scoped>
.box {
  display: flex;

  .user-circle {
    height: 150px;
    width: 150px;
    border-radius: 75px;
    overflow: hidden;
    margin-left: 10px;
  }
  .text {
    height: 150px;

    .buttonbox{
      height:200px;
      margin:30px 0px;
      padding: 20px 0px;
      transform: translateX(-140px);
    }
  }
  .title {
    font-size: 30px;
    margin: 20px 30px;
    font-weight: 600;
  }
  .subtitle {
    font-size: 16px;
    padding: 10px 30px;
    color: gray;
  }
  .el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
  }
  .things {
    margin: 0 0 20px 0;
    color: grey;
  }
}
</style>
