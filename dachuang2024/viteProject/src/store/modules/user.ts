// 创建用户相关小仓库
import { defineStore } from "pinia";
// 引入接口
import { reqLogin,reqUserInfo } from "@/api/user";
// 引入数据类型
import type { loginForm } from "@/api/user/type";
// 引入路由
import { constantRoute } from "@/router/routes";

// 创建用户小仓库
let useUserStore = defineStore("User", {
  // 小仓库存储数据的地方
  state: () => {
    return {
      // 用户的唯一标识
      token: localStorage.getItem("TOKEN"),
      menuRoutes:constantRoute
    };
  },
  // 异步|逻辑的地方
  actions: {
    // 用户登录的方法
    async userLogin(data: loginForm) {
      console.log(data);
      let result: any = await reqLogin(data);
      if (result.code == 200) {
        // 请求成功：存储用户token
        this.token = result.data.token;
        // 本地持久化存储
        localStorage.setItem("TOKEN", result.data.token);
        // 能保证当前async函数返回一个成功的promise
        return "ok";
      } else {
        return Promise.reject(new Error(result.data.message));
      }
    },
  },
  getters: {},
});
// 对外暴露
export default useUserStore;
