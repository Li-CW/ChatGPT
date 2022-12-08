import { createRouter, createWebHistory } from 'vue-router'
import ChatGPT from "../views/chatGPT/ChatGPT";
const routes = [
    {
        path: "/",
        name: "chatGPT",
        component: ChatGPT,
    },
    {
        path: "/:catchAll(.*)",
        redirect: "/",
    },

];

const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router
