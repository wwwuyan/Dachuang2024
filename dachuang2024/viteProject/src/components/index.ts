// 引入所有全局组件
import SvgIcon from "./SvgIcon/index.vue";
// 引入全部图标组件
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

// 全局对象
const allGlobalComponent:any = { SvgIcon };
//对外暴露
export default {
  install(app:any) {
    Object.keys(allGlobalComponent).forEach(key => {
      app.component(key, allGlobalComponent[key]);
    });
    // 将全部图标注册为全局组件
    for (const[key, component] of Object.entries(ElementPlusIconsVue)){
      app.component(key, component)
    }
  },
};
