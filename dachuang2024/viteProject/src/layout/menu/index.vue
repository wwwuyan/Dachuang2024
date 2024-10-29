<template>
  <!--没有子路由-->
  <template v-for="item in menuList" :key="item.path">
    <template v-if="!item.children">
      <el-menu-item
        v-if="!item.meta.hidden"
        :index="item.path"
        @click="goRoute"
      >
        <el-icon class="icon_class">
          <component :is="item.meta.icon"></component>
        </el-icon>
        <template #title>
          <span class="title_class">{{ item.meta.title }}</span>
        </template>
      </el-menu-item>
    </template>
    <!--有一个子路由-->
    <template v-if="item.children && item.children.length == 1">
      <el-menu-item
        v-if="!item.children[0].meta.hidden"
        :index="item.children[0].path"
        @click="goRoute"
      >
        <el-icon class="icon_class">
          <component :is="item.children[0].meta.icon"></component>
        </el-icon>
        <template #title>
          <span class="title_class">{{ item.children[0].meta.title }}</span>
        </template>
      </el-menu-item>
    </template>
    <!--有多个子路由-->
    <el-sub-menu
      v-if="item.children && item.children.length > 1"
      :index="item.path"
    >
      <template #title>
        <el-icon class="icon_class">
          <component :is="item.meta.icon"></component>
        </el-icon>
        <span class="title_class">{{ item.meta.title }}</span>
      </template>
      <Menu :menuList="item.children"></Menu>
    </el-sub-menu>
  </template>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
// 获取父组件传来的路由数据
defineProps(["menuList"]);

let $router = useRouter();
const goRoute = (vc: any) => {
  // 路由跳转
  $router.push(vc.index);
};
</script>

<script lang="ts">
export default {
  name: "Menu",
};
</script>

<style scoped>
.title_class {
  padding: 0 0 0 15px;
  font-size: 16px;
}

.icon_class {
  padding: 0 0 0 5px;
}
</style>
