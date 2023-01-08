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
    name: 'MainframeLoG',
    components: { HeadersLoG, ContentLoG }
});
</script>