import { createApp } from "vue";
import App from "@/App.vue";
// 引入element-plus
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
// 配置element-plus国际化
// @ts-ignore
import zhCn from "element-plus/dist/locale/zh-cn.mjs";
// 配置svg插件
import "virtual:svg-icons-register";
// 引入自定义插件对象：注册整个项目的全局组件
import globalComponent from "@/components";
// 引入模板的全局样式
import "@/styles/index.scss";
// 引入路由
import router from "./router";
// 引入仓库
import pinia from "./store";
// 引入echarts
import * as echarts from 'echarts';

// 获取应用的实例对象
const app = createApp(App);
// 国际化
app.use(ElementPlus, {
  locale: zhCn,
});
// 安装自定义插件
app.use(globalComponent);
// 注册模板路由
app.use(router);
// 安装仓库
app.use(pinia);
// echarts
app.config.globalProperties.$echarts = echarts

// 将应用挂载到挂载点上
app.mount("#app");
