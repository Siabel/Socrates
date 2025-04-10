<template>
  <div>
    <div class="comment">
      <div>
        <!-- <span class="comment-id">{{ comment.id }}</span>.  -->
        <span class="comment-content">{{ comment.content }}</span>
      </div>

      <div>
        <button @click="deleteComment" class="delete-comment-btn">댓글 삭제</button>
      </div>
    </div>
  <hr>
  </div>
</template>

<script setup>
import { usePostStore } from '@/stores/posts'
import { useCommentStore } from '@/stores/comments'
import { useRouter } from 'vue-router';

const router = useRouter()
const postStore = usePostStore()
const CommentStore = useCommentStore()

const props = defineProps({
  comment: Object
})

const deleteComment = function () {
  CommentStore.deleteComment(props.comment.id)
  
  // router.push({ name: 'detail', params: {pk: pk} })
  router.go(0)
}
</script>

<style scoped>
.comment {
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.delete-comment-btn {
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

.delete-comment-btn:hover {
  background-color: rgb(128, 128, 128);
  color: white;
  transition: background-color 0.3s ease;
    }
</style>