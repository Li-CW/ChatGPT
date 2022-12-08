<template>
    <ContentBase style="width: min(850px, 100%); margin: 0 auto; margin-top: 60px;">
        <h5 class="card-title" style="text-align:center">ChatGPT(等待大约一分钟)</h5>
        <div class="content">
            <div class="chat-AI">
                <span class="chat-AI-role">AI</span>
                <div class="chat-AI-content">
                    <pre>您好，我是OpenAI开发的chatGPT。您可以在这里和我交流。请在底部输入框输入你的问题。</pre>
                </div>
            </div>
            <div v-for="(quesitons, index) in quesitons" :key="index">
                <div class="chat-people">
                    <div class="chat-AI-content">
                        <pre>{{ quesitons }}</pre>
                    </div>
                    <span class="chat-people-role">你</span>
                </div>
                <div class="chat-AI" v-show="(answers.length > index)">
                    <span class="chat-AI-role">AI</span>
                    <div class="chat-AI-content">
                        <pre>{{answers[index]}}</pre>
                    </div>
                </div>
            </div>
        </div>
        <div class="input-group mb-3 write">
            <input type="text" class="form-control" placeholder="输入对话内容" v-model="question">
            <button type="button" class="btn btn-primary" :class="send_button_class" @click="send_message">{{button_message}}</button>
        </div>

    </ContentBase>

</template>

<script>
import ContentBase from "../../components/ContentBase.vue";
import { ref } from "vue"
import axios from "axios";
import apis from '../service/api_url';
export default {
    name: "ChatGPT",
    setup() {
        const question = ref("");
        const quesitons = ref([]);
        const answers = ref([]);
        const send_button_class = ref("");
        const button_message = ref("发送");
        const send_message = () => {
            if (question.value.trim() !== "") {
                send_button_class.value = "disabled";
                button_message.value = "请等待";
                quesitons.value.push(question.value);
                axios.post(apis.chatGPT, { "question": question.value })
                    .then((response) => {
                        answers.value.push(response.data["result"].trim());
                    }).catch(() => { 
                        answers.value.push("同时问问题的人太多了，我脑子糊涂了，我需要休息 3 分钟。呜呜呜~~~");
                    }).finally(() => { 
                        send_button_class.value = "";
                        button_message.value = "发送";
                    })
                question.value = "";
            }
        }
        return {
            send_message,
            question,
            quesitons,
            answers,
            send_button_class,
            button_message,
        }
    },
    components: {
        ContentBase,
    }
}
</script>

<style>
.content {
    background-color: rgb(240, 236, 236);
    border: 2px solid rgb(199, 193, 193);
    border-radius: 5px;
    margin-bottom: 40px;
}

.chat-AI {
    margin-left: 10px;
    margin-top: 10px;
}

.chat-AI-role {
    height: 60px;
    width: 60px;
    text-align: center;
    line-height: 60px;
    display: inline-block;
    font-size: xx-large;
    border-radius: 50%;
    background-color: rgb(172, 104, 13);
    vertical-align: top;
    margin-right: 5px;
}

.chat-AI-content {
    display: inline-block;
    width: Calc(100% - 150px);
}

.chat-people {
    margin-right: 10px;
    margin-top: 10px;
    text-align: right;
}



.chat-people-content {
    display: inline-block;
    width: Calc(100% - 150px);

}

.chat-people-role {
    height: 60px;
    width: 60px;
    text-align: center;
    line-height: 60px;
    display: inline-block;
    font-size: xx-large;
    border-radius: 50%;
    background-color: rebeccapurple;
    vertical-align: top;
    margin-left: 5px;
}

pre {
    margin-top: 20px;
    white-space: pre-wrap;
    word-wrap: break-word;
    background-color: white;
    border-radius: 6px;
    border: 2px solid rgb(199, 193, 193);
    background-color: aquamarine;
    text-align: left;
}

.write {
    position: fixed;
    width: min(850px, 100%);
    margin: auto;
    bottom: 0;
    z-index: 1000;
}
</style>