<template>
    <div class="workspace-plot-div">
        <label>Upload Data File
            <input type="file" @change="handleFileUpload( $event )"/>
        </label>
        <button v-on:click="submitFiles('plotter')" class="build-button">Submit Plotter</button>
        <button v-on:click="submitFiles('fitter')" class="build-button">Submit Fitter</button>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
    name: "UploadFile", 
    components: {  },
    data(){
        return {
            file : null as File | null
        }
    },
    methods: {
        handleFileUpload(event: Event) {
            const target = (event.target as HTMLInputElement);
            this.file = target.files? target.files[0]: null;
        },
        submitFiles(service: string) {
            const formData = new FormData();

            if (!this.file) {
                console.log('No file provided.');
                return;
            }

            formData.append('rawData', this.file);
        
            const options = JSON.stringify({
                color: "#0000FF",
                title: {
                    label: "This is the title",
                    color: "#666666",
                    fontsize: 24
                },
                xlabel: 'X Label',
                ylabel: 'Y Label'
            });
            formData.append('rawOptions', options);

            if(service == "fitter") {
                const func = "$f(x) = x^2$";
                formData.append('rawFunc', func);
            }

            const baseUrl = "http://localhost:8081/";
            axios.post(baseUrl + service,
                formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }
            ).then(function(){
                console.log('Successfully uploaded file.');
            })
            .catch(function(){
                console.log('Some error occured.');
            });
        },
    }
})
</script>

<style>
.workspace-plot-div {
    width: 100%;
    background-color: #A8A193;
}

.plot-img {
    margin: 0px;
    width: 60%;
    border-radius: 0px;
}

.build-button {
    height: 30px;
    width: 150px;
    border-radius: 5px;
    border: 0;
    margin: 10px;
}

.submit-div {
    background: red;
    position: relative;
}
</style>