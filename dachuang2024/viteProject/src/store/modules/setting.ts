import {defineStore} from "pinia";

let useLayoutSettingStore=defineStore('SettingStore',{
  state:()=>{
    return{
      fold:false,
      refsh:false,
    }
  }
})

export default useLayoutSettingStore