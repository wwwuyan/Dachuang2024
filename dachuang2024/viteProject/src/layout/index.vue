<template>
  <div class="layout_container">
    <!--左侧菜单-->
    <div class="layout_slider">
      <div class="logo" alt="">
        <img src="../../../icon.svg" />
        <p style="font-size: 20px">医疗辅助诊断平台</p>
      </div>
      <!--滚动条展示菜单-->
      <el-scrollbar class="scrollbar">
        <el-menu background-color="#343a3f" text-color="#bbc1c6" :default-active="$route.path">
          <!--根据路由动态生成菜单-->
          <Menu :menuList="userStore.menuRoutes"></Menu>
        </el-menu>
      </el-scrollbar>
    </div>
    <!--顶部导航-->
    <div class="layout_tabbar">
      <Tabbar></Tabbar>
    </div>
    <!--内容展示区-->
    <div class="layout_main">
      <Main></Main>
    </div>
  </div>
</template>

<script setup lang="ts">
// 获取路由对象
import { useRoute } from 'vue-router';
// 引入菜单栏
import Menu from './menu/index.vue'
// 右侧内容展示区域
import Main from './main/index.vue'
// 引入顶部导航栏
import Tabbar from './tabbar/index.vue'
// 引入用户相关小仓库
import useUserStore from '@/store/modules/user'
//import useLayoutSettingStore from '@/store/modules/setting';
let userStore=useUserStore()
//let layoutSettingStore=useLayoutSettingStore()

// 获取路由对象
let $route=useRoute()


</script>

<script lang="ts">
export default {
  name:"Layout"
}
</script>


<style scoped lang="scss">
.layout_container {
  width: 100%;
  height: 100vh;
  background: white;
  .layout_slider {
    width: $base-menu-width;
    height: 100vh;
    background: $base-menu-background;
    box-shadow: 0px 0px 10px $base-menu-background;
    z-index: 1;
    position: relative;
    .logo {
      width: 100%;
      height: 50px;
      padding: 0px 5px;
      margin: 0px 0px 10px 0px;
      color: #bbc1c6;
      display: flex;
      align-items: center;
    
      img {
        width: 40px;
        height: auto;
        margin: 5px 15px;
      }
    }
    .scrollbar {
      width: 100%;
      height: calc(100vh - 60px);
      color: #bbc1c6;
      .el-menu{
        border-right: none;
      }
    }
  }
  .layout_tabbar {
    width: calc(100% - $base-menu-width);
    height: $base-tabbar-height;
    position: fixed;
    top: 0px;
    left: $base-menu-width;
    background: white;
    color: black;
  }
  .layout_main {
    position: absolute;
    width: calc(100% - $base-menu-width);
    height: calc(100vh - $base-tabbar-height);
    background: white;
    top: $base-tabbar-height ;
    left: calc($base-menu-width);
    padding: 20px;
    overflow: auto;
    background-color: #f5f7fb;
  }
}
</style>
