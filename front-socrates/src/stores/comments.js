import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { usePostStore } from './posts.js'
import { useAuthStore } from './auth.js'


export const useCommentStore = defineStore('comments', () => {
  const AuthStore = useAuthStore()
  const postStore = usePostStore()
  const commentCreate = function (pk, content) {
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/community/posts/${pk}/comments/`,
      headers: {
        Authorization: `Token ${AuthStore.token}`
      },
      data: {
        content
      }
    })
    .then(res => postStore.detailPost.comment_set.push(res.data))
    .catch(err => console.log(err))
  }

  const deleteComment = function (pk) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/community/posts/comments/${pk}/`,
      headers: {
        Authorization: `Token ${AuthStore.token}`
      },
      data: {
        pk
      }
    })
  }
  return { commentCreate, deleteComment }
})
