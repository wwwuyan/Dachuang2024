<template>
  <div>
    <router-view v-slot="{Component}">
      <transition name="fade">
        <!--渲染layout一级路由组件-->
        <component :is="Component" v-if="flag"/>
      </transition>
    </router-view>
  </div>
</template>

<script setup lang="ts">
import {watch, ref, nextTick} from 'vue'
import useLayoutSettingStore from '@/store/modules/setting';
let layoutSettingStore=useLayoutSettingStore()

// 控制当前组件是否销毁重建
let flag=ref(true)

// 监听仓库刷新事件是否变化
watch(()=>layoutSettingStore.refsh,()=>{
  flag.value=false;
  nextTick(()=>{
    flag.value=true
  })
})
</script>

<script lang="ts">

export default {
  name:"Main"
}



</script>

<style scoped>
/* .fade-enter-from{
  opacity:0
}
.fade-enter-active{
  transition: all 1s
}
.fade-enter-to{
  opacity:1
} */

</style>