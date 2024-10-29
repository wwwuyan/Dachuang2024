<template>
  <svg :style="{ width, height }">
    <use :xlink:href="prefix + name" :fill="color"></use>
  </svg>
</template>

<script setup lang="ts">
defineProps({
  // 图标前缀
  prefix:{
    type:String,
    default:"#icon-"
  },
  // svg文件名
  name:String,
  // 若想更改颜色，须删除svg文件中的fill属性
  color:{
    type:String,
    default:''
  },
  // 图标宽度
  width:{
    type:String,
    default:'16px'
  },
  // 图标高度
  height:{
    type:String,
    default:'16px'
  }
})
</script>

<style scoped></style>
