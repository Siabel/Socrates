<template>
    <div>
        <!-- <h2>자유 게시판</h2> -->

        <ul>
            <div v-for="post in store.postList"
                :key="post.pk"
                :post="post"
                @click="goDetail(post.pk)"
                class="post"
            >
                <div v-if="post.category.id == 1">
                    <!-- <p>{{ post }}</p> -->
                    <h3 v-if="post.pk < 10"> 0{{ post.pk }}번글 | {{ post.title }}</h3>
                    <h3 v-else> {{ post.pk }}번글 | {{ post.title }}</h3>
                    <hr>
                </div>
            </div>
        </ul>
    </div>
  </template> 
  
  <script setup>
  import { RouterLink } from 'vue-router'
  import { onMounted } from 'vue'
  import { usePostStore } from '@/stores/posts'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  const store = usePostStore()
  
  onMounted(() => {
    store.getPostList()
  })
  
  
  const goDetail = (pk) => {
    router.push({name:'detail', params:{pk: pk}})
  }
  
  </script>
  
  <style scoped>
  </style>