<template>
    <svg class="svg-class" :class="className">
        <use :href="'#icon-' + iconName"></use>
    </svg>
</template>
<script>
export default {
    name: "SvgIcon",
    props: {
        className: {
            type: String,
            default: ""
        },
        iconName: {
            type: String,
            default: ""
        },
    },
};
</script>
<style scoped>
.svg-class {
    fill: currentColor;
    /* overflow: hidden; */
}
</style>