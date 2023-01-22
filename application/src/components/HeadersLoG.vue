<template>
    <header class="log-header">
        <div class="logo-div">
            <img src="../assets/logo.png" alt="Vue logo" class="logo">
            <h1 class="logo-text">Lion Of <br/> Graphs</h1>
        </div>
    </header>
</template>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&display=swap');

.log-header {
    margin-top: 0;
    width: 100%;
    background-color: #1a1a1a;
}

.logo-div {
    display: flex;
    flex-direction: row;
    justify-content: center; 
    align-items: center;
}

.logo {
  width: 100px;
}

.logo-text {
    padding-left: 20px;
    text-align: left;
    color: #A8A193;
    font-family: 'Playfair Display', serif;
    font-size: 250%;
}
</style>