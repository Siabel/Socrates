<template>
  <div class="container">
    <div>
      <h1>게시판</h1>
    </div>
    
    <!-- <h2>게시글 목록 페이지</h2> -->

    <hr class="community-header-hr">
    <div class="community-header">
      <div>
        <button @click="selectCommunityCategory(1)" 
        class="community-btn"
        :class="{'active' : isFreeActive, 'deactive' : _isFreeActive }">자유게시판
        </button>

        <button @click="selectCommunityCategory(2)" 
        class="community-btn"
        :class="{'active' : isQuestionActive,  'deactive' : _isQuestionActive  }">질문게시판
        </button>

        <button @click="selectCommunityCategory(3)" 
        class="community-btn"
        :class="{'active' : isReviewActive,  'deactive' : _isReviewActive  }">리뷰게시판
      </button>

      </div>
      <RouterLink :to="{name:'CreatePost'}"><button class="create-post-btn">게시글 생성</button></RouterLink>
    </div>
    <hr class="community-header-hr">
    
    <FreePosts v-if="CommunityCategoryID===1"/>
    <QuestionsPosts v-if="CommunityCategoryID===2"/>
    <ReviewsPosts v-if="CommunityCategoryID===3"/>
  
  </div>
</template>

<script setup>
import FreePosts from '@/components/community/FreePosts.vue';
import QuestionsPosts from '@/components/community/QuestionsPosts.vue';
import ReviewsPosts from '@/components/community/ReviewsPosts.vue';
// import PostList from '@/components/community/PostList.vue'
import { useRouter } from 'vue-router'
import { usePostStore } from '@/stores/posts'
import { onMounted, ref, watch } from 'vue'

// const router = useRouter()
const Poststore = usePostStore()

console.log(Poststore.postList)

onMounted(() => {
  Poststore.getPostList()
})

const CommunityCategoryID = ref(1)
const isFreeActive = ref(true)
const isQuestionActive = ref(false)
const isReviewActive = ref(false)
const _isFreeActive = ref(false)
const _isQuestionActive = ref(true)
const _isReviewActive = ref(true)

const selectCommunityCategory = function (id) {
  CommunityCategoryID.value = id

  isFreeActive.value = id === 1;
  isQuestionActive.value = id === 2;
  isReviewActive.value = id === 3;

  _isFreeActive.value = id !== 1;
  _isQuestionActive.value = id !== 2;
  _isReviewActive.value = id !== 3;

  // console.log(isFreeActive.value, isQuestionActive.value, isReviewActive.value)
}

// watch(() => CommunityCategoryID, function () {
//   console.log(CommunityCategoryID)
// })


</script>

<style scoped>
.container {
  margin-top: 60px;
  width: 100%;
}

.community-header {
  /* border: 1px solid rgb(0, 146, 93); */
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.community-btn {
  border: none;
  /* border-radius: 8px; */
  /* background-color: black; */
  width: 120px;
  height: 50px;
  cursor: pointer;
  padding: 0;
  color: white;
  font-size: 14px;
  font-family: Noto Sans KR;
  font-weight: bold;
}

.community-btn:hover {
  background-color: rgb(0, 146, 93);
  transition: background-color 0.4s ease;
}
.create-post-btn {
    background-color: rgb(0, 146, 93);
    border-radius: 8px;
    border-color: transparent;
    height: 40px;
    color: white;
    font-size: 14px;
    font-family: Noto Sans KR;
    font-weight: bold;
    width: 120px;
    cursor: pointer;
}

.create-post-btn:hover {
  background-color: rgb(0, 83, 53);
  transition: background-color 0.3s ease;
    }

.community-header-hr {
  border-top: 2px solid rgb(139, 139, 139); /* 두껍게 변경 */
  margin: 0;
  
}

.active {
  background-color: rgb(0, 146, 93);
}

.deactive {
  background-color: transparent
}
</style>

<style>
ul {
  padding: 0;
}

.post {
  cursor: pointer;
}
</style>