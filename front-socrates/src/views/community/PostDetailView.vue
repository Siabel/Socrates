<template>
  <div class="container">
    <div class="post-details">
    
      <div class="post-detail-header">
        
        <div class="post-info">
          <h1 class="post-title"> {{ store.detailPost.title }}</h1>
        </div>
        
        <div class="post-dates">
          <p class="created-date">작성일: {{ store.detailPost.created_date }}</p>
          <p class="updated-date">수정일: {{ store.detailPost.updated_at }}</p>
        </div>
        
      </div>

      <hr class="highlight-hr">
      
      <div class="post-detail-content">
        <p class="post-content">{{ store.detailPost.content }}</p>
      </div>

      <div class="post-detail-buttons">
        <button @click="updatePost" class="update-post-btn">게시글 수정</button>
        <button @click="deletePost" class="delete-post-btn">게시글 삭제</button>
      </div>

      <hr>
      <CommentCreate 
      :postPk="store.detailPost.id"
      />

      <hr>

      <CommentList
      v-for="comment in store.detailPost.comment_set"
      :key="comment.id"
      class="comment-item"
      :comment="comment"
      />
    </div>  
  </div>
</template>

<script setup>
import CommentCreate from '@/components/community/CommentCreate.vue';
import CommentList from '@/components/community/CommentList.vue';
import { onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { usePostStore } from '@/stores/posts';

const router = useRouter()
const route = useRoute()
const store = usePostStore()

onMounted(() => {
  store.getDetailPost(route.params.pk)
})

const updatePost = function () {
  router.push({ name: 'postUpdate'})
}

const deletePost = function () {
  const pk = store.detailPost.id
  store.deletePost(pk)
  router.push({ name: 'posts' })
}
</script>


<style scoped>
.container {
  margin-top: 100px;
  width: 100%;
}

.post-detail-header {
  display: flex;
  justify-content: space-between;
}
.post-details {
  width: 100%;
  margin: 0 auto;
  padding: 20px;
}

.highlight-hr {
  border-top: 2px solid rgb(139, 139, 139); /* 두껍게 변경 */
  margin: 0;
  
}
.post-detail-buttons {
  display: flex;
  justify-content: flex-end;
  gap:0.5rem;
  margin: 10px 0;
}
.update-post-btn {
  border: none;
  border-radius: 8px;
  background-color: rgb(0, 146, 93);
  width: 120px;
  height: 40px;
  cursor: pointer;
  padding: 0;
  color: white;
  font-size: 14px;
  font-family: Noto Sans KR;
  font-weight: bold;
}


.delete-post-btn {
    border: 1px solid rgb(124, 124, 124);
    border-radius: 8px;
    background-color: transparent;
    height: 40px;
    color: rgb(207, 207, 207);
    font-size: 14px;
    font-family: Noto Sans KR;
    font-weight: bold;
    width: 120px;
}

.update-post-btn:hover {
  background-color: rgb(0, 83, 53);
  transition: background-color 0.4s ease;
}

.delete-post-btn:hover {
  background-color: rgb(128, 128, 128);
  color: white;
  transition: background-color 0.3s ease;
}
</style>