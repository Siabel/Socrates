<template>
  <form @submit.prevent="createComment" class="create-comment-form">
    <label for="content"></label>
    <input type="text" name="content" id="content" class="input-field" placeholder="댓글 입력" v-model="content">
    <button class="create-comment-btn">댓글 작성</button>
  </form>
</template>

<script setup>
import { useCommentStore } from '@/stores/comments.js'
import { ref } from 'vue';
const store = useCommentStore()
const props = defineProps({
  postPk: Number
})
const content = ref('')
const createComment = function () {
  store.commentCreate(props.postPk, content.value)
  content.value = ''
}
</script>

<style scoped>
.create-comment-form {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px 0;
}
input {
  border: none;
  border-radius: 7px;
  width: 82%;
  height: 40px;
  background-color: rgb(56, 56, 56);
  padding: 0 10px;;
  margin-right: 10px;
}
.input-field::placeholder {
  color: rgb(201, 201, 201); /* 흰색으로 설정 */
  font-size: 15px;
  font-weight: 500;
}

.create-comment-btn {
  border: none;
  background-color: rgb(0, 146, 93);
  border-radius: 7px;
  padding: 3px 8px;
  width: 120px;
  height: 40px;
  margin: 0;
  font-size: 14px;
  font-weight: 700;
}

button:hover {
  background-color: rgb(0, 83, 53);
  transition: background-color 0.3s ease;
}
</style>