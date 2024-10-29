// 对外暴露配置路由
export const constantRoute = [
  {
    // 登录
    path: "/login",
    component: () => import("@/views/login/index.vue"),
    name: "login",
    meta: {
      title: "登录",
      hidden: true,
    },
  },
  {
    // 登录成功展示数据的路由
    path: "/",
    component: () => import("@/layout/index.vue"),
    name: "layout",
    meta: {
      title: "",
      hidden: false,
      icon: "",
    },
    redirect: "/home",
    children: [
      {
        path: "/home",
        component: () => import("@/views/home/index.vue"),
        meta: {
          title: "首页",
          hidden: false,
          icon: "HomeFilled",
        },
      },
    ],
  },
  {
    path: "/screen",
    component: () => import("@/views/screen/index.vue"),
    name: "Screen",
    meta: {
      title: "数据智慧台",
      hidden: false,
      icon: "Platform",
    },
  },
  {
    path: "/guanjia",
    component: () => import("@/layout/index.vue"),
    name: "guanjia",
    meta: {
      title: "",
      hidden: false,
      icon: "",
    },
    redirect:'/manager',
    children: [
      {
        path: "/manager",
        component: () => import("@/views/manager/index.vue"),
        meta: {
          title: "数据管家",
          hidden: false,
          icon: "Notebook",
        },
      }]
  },
  {
    path: "/analyse",
    component: () => import("@/layout/index.vue"),
    name: "analyse",
    meta: {
      title: "智能诊断",
      hidden: false,
      icon: "DataLine",
    },
    redirect:'/analyse/reduce',
    children: [
      {
        path: "/analyse/reduce",
        component: () => import("@/views/analyse/reduce/index.vue"),
        meta: {
          title: "特征筛选",
          hidden: false,
          icon: "Filter",
        },
      },
      {
        path: "/analyse/detection",
        component: () => import("@/views/analyse/detection/index.vue"),
        meta: {
          title: "异常检测",
          hidden: false,
          icon: "Aim",
        },
      },
      {
        path: "/analyse/classification",
        component: () => import("@/views/analyse/classification/index.vue"),
        meta: {
          title: "辅助识别",
          hidden: false,
          icon: "View",
        },
      },
    ],
  },
  {
    path: "/404",
    component: () => import("@/views/404/index.vue"),
    name: "404",
    meta: {
      title: "404",
      hidden: true,
    },
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/404",
    name: "Any",
    meta: {
      title: "Any",
      hidden: true,
    },
  },
];
