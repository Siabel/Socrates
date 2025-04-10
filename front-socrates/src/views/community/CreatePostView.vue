<template>
  <div class="create-post-page">
    <h1>게시글 작성</h1>
    <form @submit.prevent="createPost" class="post-form">
      <label for="category" class="form-label">카테고리 선택:</label>
      <select name="category" id="category" v-model="category" class="form-select">
        <option
          v-for="category in categoryStore.categoryList"
          :key="category.id"
          :value="category.id"
        >
          {{ category.name }}
        </option>
      </select>

      <label for="title" class="form-label">제목:</label>
      <input type="text" name="title" v-model="title" class="form-input">

      <label for="content" class="form-label">내용:</label>
      <textarea name="content" id="content" cols="40" rows="10" v-model="content" class="form-textarea"></textarea>

      <button class="submit-button">게시글 생성</button>
    </form>
      
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCategoryStore } from '@/stores/categories'
import { usePostStore } from '@/stores/posts'
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()

const title = ref('')
const content = ref('')
const category = ref(1)
const postStore = usePostStore()
const categoryStore = useCategoryStore()
onMounted(() => {
  categoryStore.getCategoryList()
})

const createPost = function () {
  const post = {
    category: category.value,
    title: title.value,
    content: content.value,
  }
  postStore.createPost(post)
  router.push({name: 'Community'})
}
</script>

<style scoped>
.create-post-page {
  width: 100%;
  margin: 0 auto;
  margin-top: 60px;
  padding: 0;

}

.post-form {
  margin-top: 3rem;
  background-color: #000000;
  border-radius: 5px;
  padding: 0;
}

.form-label {
  font-size: 16px;
  display: block;
  margin-bottom: 8px;
  background-color: #000000;
  margin: 15px 0;
}

.form-select,
.form-input,
.form-textarea {
  width: calc(100% - 20px); /* 전체 너비에서 padding 값 빼기 */
  padding: 10px;
  font-size: 14px;
  border: 1px solid #525252;
  border-radius: 5px;
  margin-bottom: 10px;
  background-color: #000000;
  box-sizing: border-box; /* padding 값이 너비에 포함되도록 box-sizing 설정 */

}

.submit-button {
  width: calc(100% - 20px); /* 전체 너비에서 padding 값 빼기 */
  /* display: block; */
  height: 50px;
  /* padding: 10px; */
  background-color: rgb(0, 146, 93);
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  font-family: Noto Sans KR;
  font-weight: 600;
  transition: background-color 0.2s;
  margin: 10px 0;

}

.submit-button:hover {
  background-color: rgb(0, 83, 53);
  transition: background-color 0.3s ease;
}
</style>