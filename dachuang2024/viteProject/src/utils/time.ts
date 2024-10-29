// 封装一个函数，获取时间
export const getTime = () => {
  let message = "";
  let hours = new Date().getHours();
  if (hours >= 6 && hours <= 9) {
    message = "早上好";
  } else if (hours <= 12) {
    message = "上午好";
  } else if (hours <= 18) {
    message = "下午好";
  } else if (hours <= 24) {
    message = "晚上好";
  } else {
    message = "夜深了";
  }
  return message;
};
