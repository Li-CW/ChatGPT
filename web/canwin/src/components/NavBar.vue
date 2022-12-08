<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark   fixed-top " style="padding:0px; ;">
        <div class=" container">
            <router-link class="nav-link brand " :to="{ name: 'chatGPT' }" >
                <div class="navbar-brand" style=" font-weight: bold;">ChatGPT</div>
            </router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation" style="margin: 5px;">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="navbar-collapse collapse in justify-content-between" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item" >
                        <router-link class="nav-link nav_item" :to="{ name: 'chatGPT' }"
                            style="font-size: 20px; padding: 10px;">
                            ChatGPT
                        </router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

</template>

<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
export default {
    name: 'NavBar',
    setup() {
        const store = useStore();
        let classfication_acitve = ref(["", ""]);
        const active_nav_item = (index) => {
            for (let i = 0; i < 2; i++) {
                classfication_acitve.value[i] = "";
            }
            classfication_acitve.value[index] = "active";
        }
        return {
            active_nav_item,
            store,
        }
    },
}
</script >


<style lang="less" scoped>
.container {
    margin-top: 0;
    margin-bottom: 0;
    background-color: rgb(35, 35, 35);
}

.navbar-nav {
    >li>a {
        // color: gray;

        &:hover {
            color: aliceblue;
            background-color: black;
        }
    }
}

.active>a {
    color: aliceblue;
    background-color: #080808;
}


.navbar-nav>li {
    padding-left: 0;
    padding-right: 20px;
    font-size: 15px;
}

.popover {
    z-index: 1000000 !important;
}

@media (min-width: 768px) {
    .container {
        width: 750px;
    }
}

@media (min-width: 992px) {
    .container {
        width: 900px;
    }
}

@media (min-width: 1200px) {
    .container {
        width: 1000px;
    }
}

@media (min-width: 1300px) {
    .container {
        width: 1170px;
    }
}

.notify {
    color: gray;
    height: 25px;
    width: 25px;
    margin-top: 12px;

    cursor: pointer;
}

.notify:hover {
    color: aliceblue;

}

.nitify_count {
    display: inline-block;
    color: aliceblue;
    background-color: red;
    height: 15px;
    width: 15px;
    border-radius: 50%;
    font-size: 10px;
    text-align: center;
    font-weight: bolder;
}
</style>