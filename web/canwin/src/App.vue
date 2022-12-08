<template>
        <NavBar />
        <router-view :key="$route.fullPath" />
</template>
<script>
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap';
import NavBar from './components/NavBar';
import { useStore } from 'vuex';
export default {
    name: 'App',
    components: {
        NavBar,
    },
    setup() {
        const store = useStore();
        return {
            store,
        }
    }

}

</script>

<style>

</style>
