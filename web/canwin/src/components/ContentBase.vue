<template>
    <div class="context-base" id="context-base">
        <slot></slot>
    </div>
</template>

<script>
export default {
    name: 'ContentBase',
    setup() {
        return {
        }
    },
    components: {
    }
}
</script>

<style scoped>
.context-base {
    margin-top: 60px;
    padding-bottom: 100px;

}
</style>
