import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
// @ts-ignore
import path from "path";
import { createSvgIconsPlugin } from "vite-plugin-svg-icons";
// mock插件提供方法
import { viteMockServe } from "vite-plugin-mock";
// https://vitejs.dev/config/
export default defineConfig(({ command }) => {
  return {
    plugins: [
      vue(),
      createSvgIconsPlugin({
        iconDirs: [path.resolve(process.cwd(), "src/assets/icons")],
        symbolId: "icon-[dir]-[name]",
      }),
      viteMockServe({
        enable: command === "serve", //保证开发阶段可以使用mock接口
      }),
    ],
    resolve: {
      alias: {
        "@": path.resolve("./src"),
      },
    },
    css: {
      preprocessorOptions: {
        scss: {
          javascriptEnable: true,
          additionalData: "@import './src/styles/variable.scss';",
        },
      },
    },
    server: {
      // 设置代理
      proxy: {
        "/api": {
          target: "http://127.0.0.1:5000", // 访问数据的计算机域名
          ws: true, // 是否启用websockets
          changeOrigin: true, //开启代理,
          rewrite: (path) => path.replace(/^\/api/, ''), // 重写代理规则，/api开头，代理到/
        }
      }
    },
  };
});
