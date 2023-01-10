<template>
    <form>
        <label>{{ label }}</label>
        <input type="text" :placeholder=defaultValue class="button"/>
    </form>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: "UploadFile", 
    components: { },
    data(){
        return {
            title: 'This is the title' as string
        }
    },
    props: ['label', 'defaultValue'],
});
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&family=Playfair+Display:wght@900&display=swap');

form {
    max-width: 400px;
    padding: 1%;
    margin: 1%;
    border-radius: 5px;
    text-align: left;
    background: #F5FAFE;
    display: flex;
    align-items: center;
}

label {
    font-family: 'Open Sans', sans-serif;
    color: #1a1a1a;
    display: inline-block;
    margin: 0px 10px 0px 10px;
    font-size: 100%;
    text-transform: uppercase;
    font-weight: bold;
    letter-spacing: 1px;
}

input {
    font-family: 'Open Sans', sans-serif;
    width: 70%;
    font-size: 100%;
    border: 0px;
    border-bottom: 1px solid #A8A193;
    background: transparent;
    color: #1a1a1a;
}
</style>