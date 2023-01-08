<template>
    <div id="log-content" class="content">
        <div id="log-content-mainframe" class="mainframe">
            <div id="log-content-mainframe-workspace" class="workspace-div">
                <WorkspacePlot />
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import WorkspacePlot from './WorkspacePlot.vue';

export default defineComponent({
    name: 'ContentLoG',
    components: { WorkspacePlot } ,
});
</script>

<style>
.content {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin-top: 70px;
}

.mainframe {
    border-radius: 10px;
    background-color: #1a1a1a;
    width: 90%;
    height: 80%;
    display: flow-root;
}

.buttons-div {
    display: flex;
    align-content: left;
    height: 50px;
}

.workspace-div {
    display: flex;
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
    background-color: #F5FAFE;
    height: 510px;
}


.workspace-options-div {
    width: 100%;
    background-color: #A8A193;
}

</style>