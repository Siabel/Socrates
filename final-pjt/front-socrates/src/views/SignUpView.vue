<template>
    <div>
        <form @submit.prevent="signUp">
            <input type="text" v-model.trim="username">
            <input type="password" v-model.trim="password1">
            <input type="password" v-model.trim="password2">
            <input type="submit">
      </form>
    </div>
</template>

<script setup>

</script>

<style scoped>

</style>