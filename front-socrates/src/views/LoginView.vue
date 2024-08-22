<template>
    <div>
        <form @submit.prevent="logIn">
            <input type="text" v-model.trim="username">
            <input type="password" v-model.trim="password">
            <input type="submit">
        </form>
    </div>
</template>

<script setup>

</script>

<style scoped>

</style>