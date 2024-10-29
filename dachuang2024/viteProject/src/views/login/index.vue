<template>
  <div class="login_container">
    <el-row>
      <el-col :span="12" :xs="0"></el-col>
      <el-col :span="12" :xs="24">
        <el-form class="login_form">
          <h1>Hello!</h1>
          <h2>欢迎来到智融医诊平台</h2>
          <h3>
            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
            ——融合模糊粒信息的新一代医疗辅助诊断系统
          </h3>
          <el-form-item class="login_item">
            <h4>账号</h4>
            <el-input
              class="login_input"
              :prefix-icon="User"
              v-model="loginForm.username"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <h4>密码</h4>            
            <el-input
              class="login_input"
              type="password"
              :prefix-icon="Lock"
              v-model="loginForm.password"
              show-password
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-button class="login_btn" type="primary" size="default" @click="login()"
              >登录</el-button
            >
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { User, Lock } from "@element-plus/icons-vue";
import { reactive } from "vue";
import { useRouter } from "vue-router";
//引入用户相关的小仓库
import useUserStore from "@/store/modules/user"
import { ElNotification } from "element-plus";
import {getTime} from '@/utils/time'

let $router=useRouter()
let userStore=useUserStore();

let loginForm = reactive({
  username: "admin",
  password: "111111",
});

const login= async ()=>{
  // 通知仓库发登录请求
  // 请求成功->跳转首页
  // 请求失败->提示错误
  try {
    // 保证登录成功
    await userStore.userLogin(loginForm);
    // 编程式导航跳转到首页
    $router.push('/');
    // 登录成功提示信息
    ElNotification({
      type:'success',
      message:'欢迎回来！',
      title:getTime()
    })
  } catch (error) {
    // 登录失败提示信息
    ElNotification({
      type:'error',
      message:(error as Error).message
    })
  }
  
}


</script>

<style scoped lang="scss">
.login_container {
  width: 100%;
  height: 100vh;
  background: url("@/assets/images/login.jpg") no-repeat;
  background-size: cover;
}
.login_form {
  position: relative;
  width: 80%;
  top: 18vh;
  left: 3vw;
  //background: linear-gradient(#4884ff, #ffff) no-repeat;
  //background: #98a3ff;
  background: #4884ff;
  //background: #427bff;
  padding: 30px;
  //border-radius: 30px 30px 0 0;
  border-radius: 20px;
  box-shadow: 0px 0px 40px grey;
  h1 {
    color: white;
    font-size: 60px;
    margin: 30px 0px;
    font-family: 'Times New Roman', Times, serif;
  }
  h2 {
    color: white;
    font-size: 30px;
    margin: 30px 0px;
    font-family:'Times New Roman', Times, serif
  }
  h3 {
    color: white;
    font-size: 20px;
    margin: 30px 0px;
    font-family: 'Times New Roman', Times, serif;
  }
  h4{
    color: white;
    font-size: 18px;
    margin: 0 0 0 15px;
  }
  .login_input{
    width: 70%;
    height: 40px;
    margin: 5px 42px;
    font-size: 18px;
  }
  .login_btn {
    width: 70%;
    margin: 20px auto;
    height: 40px;
    font-size: 18px;
    background: #96cffa
  }
  .login_item{
    display: flex;
  }
  
}
</style>
