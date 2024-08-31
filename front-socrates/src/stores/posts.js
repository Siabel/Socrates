import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useAuthStore } from './auth'

export const usePostStore = defineStore('post', () => {
    const AuthStore = useAuthStore()
    const postList = ref([])
    const categoryList = ref([])
    const API_URL = 'http://127.0.0.1:8000'

    const getPostList = function () {
      axios({
        method: 'get',
        url: `${API_URL}/community/posts/`,
        // headers: {
        //   Authorization: `Token ${AuthStore.token}`
        // },
      })
      .then(res => postList.value = res.data)
      // .then(res => console.log(res))
      .catch(err => console.log(`${AuthStore.token}`))
    }

    const detailPost = ref([])

    const getDetailPost = function (pk) {
        axios({
          method: 'get',
          url: `${API_URL}/community/posts/${pk}/`,
          headers: {
            Authorization: `Token ${AuthStore.token}`
          },
        })
        .then(res => detailPost.value = res.data)
        .then(res => console.log(detailPost))
        .catch(err => console.log(err))
    }

    const createPost = function ({ category, title, content }) {
        axios({
          method: 'post',
          url: `${API_URL}/community/posts/`,
          headers: {
            Authorization: `Token ${AuthStore.token}`
          },
          data: {
            category,
            title,
            content
          }
        })
        .then((res) => {          
          console.log(res)
        })
      .catch(err => console.log(err));
    }

    const updatePost = function ({title, content, pk}) {
        axios({
          method: 'put',
          url: `${API_URL}/community/posts/${pk}/`,
          headers: {
            Authorization: `Token ${AuthStore.token}`
          },
          data: {
            title,
            content,
          }
        })
        .then((res) => {
          getDetailPost(pk)
        })
        .catch(err => console.log(err));
    }

    const deletePost = function (pk) {
        axios({
          method: 'delete',
          url: `http://127.0.0.1:8000/community/posts/${pk}/`,
          data: {
            pk
          }
        })
        .then((res) => {
          getPostList()
          router.push({ name: 'Category' })
        })
    }
    
    return { postList, categoryList, getPostList, detailPost, getDetailPost, createPost, updatePost, deletePost }
})