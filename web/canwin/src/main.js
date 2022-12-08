import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import "./assets/js/svg";
import "@/assets/scss/font.css"
import "@/assets/css/base.css"
import '@/assets/css/markDown.css';
import SvgIcon from "@/components/Svgicon"
import "@/assets/css/animation.css";

// import VueWechatTitle from "vue-wechat-title";

var url = window.location.href;
url = url.split(window.location.host)[1]
createApp(App)
  .use(store)
  .use(router)
  .component("svg-ion", SvgIcon)
  .mount("#app")
  .$router.push(url);
