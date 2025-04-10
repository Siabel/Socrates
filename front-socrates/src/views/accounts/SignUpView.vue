<template>
    <div class="signup-page">
      <h1 style="margin-top: 100px;">회원가입</h1>
      <AuthForm 
      formType="signup"
      :sign-up="signUp"/>
    </div>
  </template>
  
<script setup>
import AuthForm from '@/components/accounts/AuthForm.vue'

const props = defineProps(['formType', 'signUp'])

  
  </script>
  
  <style>
  .signup-page {
  text-align: center;
  margin-bottom: 40px;
}
  </style>
  