<template>
    <div>
        <HeadersLoG />
        <ContentLoG />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import HeadersLoG from './HeadersLoG.vue';
import ContentLoG from './ContentLoG.vue';


export default defineComponent({
    name: 'App',
    components: { HeadersLoG, ContentLoG }
});
</script>