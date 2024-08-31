<template>
  <div class="login-page">
    <div class="login-header">
    </div>

    <div class="login-page">
      <h1 style="margin-top: 100px;">SOCRATES 로그인</h1>
      <AuthForm 
      formType="login"/>
    </div>
  </div>
</template>
  
<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import AuthForm from '@/components/accounts/AuthForm.vue'

const store = useAuthStore()
const username = ref(null)
const password = ref(null)
  
const logIn = function () {
const payload = {
    username: username.value,
    password: password.value
    }
store.logIn(payload)
}

</script>

<style scoped>
.login-page {
  text-align: center;
}

.login-header {
    position: absolute;
    background-color: black;
    width: 100%;
    height: 100px;
    z-index: 2;
}
</style>