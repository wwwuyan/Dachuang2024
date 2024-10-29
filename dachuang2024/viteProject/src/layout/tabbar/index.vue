<template>
  <div class="tabbar">
    <!--面包屑-->
    <div class="tabbar_left">
      <el-icon style="margin-right: 10px" @click="changeIcon">
        <component :is="layoutSettingStore.fold?'Fold':'Expand'"></component>
      </el-icon>
      <!--左侧面包屑-->
      <el-breadcrumb separator-icon="ArrowRight">
        <!--面包屑动态展示路由-->
        <el-breadcrumb-item v-for="(item, index) in $route.matched" :key="index" v-show="item.meta.title" :to="item.path">
          <el-icon style="margin: 0px 3px">
            <component :is="item.meta.icon"></component>
          </el-icon>
          <span>{{ item.meta.title }}</span>
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!--右侧设置-->
    <div class="tabbar_right">
      <el-button size="default" icon="Refresh" circle @click="updateRefsh"></el-button>
      <el-button
        size="default"
        icon="FullScreen"
        circle
      ></el-button>
      <el-button size="default" icon="Setting" circle></el-button>
      <img src="@/assets/icons/user.svg" style="width: 30px; height: 30px; margin: 0px 10px 0px 30px" />
      <el-dropdown>
        <span class="el-dropdown-link">
          admin
          <el-icon class="el-icon--right">
            <arrow-down />
          </el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script setup lang="ts">
import useLayoutSettingStore from '@/store/modules/setting';
import { useRouter } from "vue-router";

let $router=useRouter()

let layoutSettingStore=useLayoutSettingStore();
// 控制菜单折叠和展开
const changeIcon=()=>{
  layoutSettingStore.fold=!layoutSettingStore.fold
}

const updateRefsh=()=>{
  layoutSettingStore.refsh=!layoutSettingStore.refsh
}

const logout=()=>{
  $router.push('/login')
}
</script>

<script lang="ts">
export default {
  name:"Tabbar",

}
</script>

<style scoped lang="scss">
.tabbar {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-between;
  
  .tabbar_left {
    display: flex;
    align-items: center;
    margin-left: 20px;
  }
  .tabbar_right {
    display: flex;
    align-items: center;
    margin-right: 20px;
  }
}
</style>
