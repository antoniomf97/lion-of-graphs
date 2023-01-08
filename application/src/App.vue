<template>
    <div>
        <MainframeLoG />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MainframeLoG from './components/MainframeLoG.vue';

export default defineComponent({
    name: 'App',
    components: { MainframeLoG }
});
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
</style>
