<template>
    <div class="mother-container">
      <div class="logo">
        <RouterLink :to="{ name: 'Main'}">
          <img src="@/assets/SOCRATES-Logo.png" alt="로고 이미지"/>
        </RouterLink>
      </div>
  
      
      <div v-if="isNavBarVisible" class="nav-bar">
        <!-- <RouterLink :to="{ name: 'OnBoarding'}">OnBoarding</RouterLink> | -->
        <!-- <RouterLink :to="{ name: 'SignUp'}" class="text-with-shadow">회원가입</RouterLink> | 
        <RouterLink :to="{ name: isLogin ? null : 'Login'}" @click="ChangeLog" class="text-with-shadow">
          {{ isLogin ? '로그아웃' : '로그인' }}
        </RouterLink> | -->
        <RouterLink :to="{ name: 'Test'}" class="text-with-shadow">너 자신을 알라</RouterLink> |  
        <RouterLink :to="{ name: 'Community'}" class="text-with-shadow">커뮤니티</RouterLink> |
        <RouterLink :to="{ name: 'SearchMoviesView'}" class="text-with-shadow">검색</RouterLink> |
        <RouterLink v-if="isLogin" :to="{ name: 'OnBoarding'}" @click="ChangeLog" class="text-with-shadow">
          로그아웃
        </RouterLink>
        <!-- <button @click="deleteUser">회원탈퇴</button> -->
      </div>
          
      <div class="profile">
        <RouterLink :to="{ name: 'ProfilePage'}">
          <img src="@/assets/profile.png" style="width:40px" alt="">
          <!-- <img :src="profileImageUrl || defaultProfileImageUrl"  -->
          <!-- alt="프로필 이미지"  -->
          <!-- class="profile-image" /> -->
        </RouterLink>
      </div>

      <!-- <div v-if="isSearchOpen" class="search-background" @click="closeSearch"> -->
        <!-- <img src="@/assets/onboarding-background-1.jpg" alt="" style="width:100%; height:100%" > -->
      <!-- </div> -->

      <!-- <div v-if="isSearchOpen">
          <SearchMovie 
          :close-modal="closeSearch"/>
      </div> -->

      <RouterView />  
    </div>
    <!-- <OnBoardingView :is-nav-bar-visible="isNavBarVisible"/> -->
  </template>
  
<script setup>
// import OnBoardingView from '@/views/main-page/OnBoardingView.vue';

import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { onMounted, computed , ref} from 'vue'

import { defineProps } from 'vue';

// 부트스트랩 CDN
// import 'bootstrap/dist/css/bootstrap.min.css';
// import 'bootstrap/dist/js/bootstrap.bundle.min.js';
const isSearchOpen = ref(false)

const isNavBarVisible = ref(true)

const closeSearch = () => {
  isSearchOpen.value = false;
  console.log(isSearchOpen.value)
}

const props = defineProps(['isNavBarVisible'])

// onMounted(() => {
//   isNavBarVisible.value = false;
// });

const router = useRouter()
const Authstore = useAuthStore()

const isLogin = computed(() => {
  return Authstore.isLogin
})


// const profileImageUrl = computed(() => Authstore.profile_imageUrl || Authstore.defaultProfileImageUrl.value);

const ChangeLog = () => {
  if (isLogin.value) {
    Authstore.logOut()
    router.push({ name: 'OnBoarding'})
  } else {
    router.push({ name: 'Login' })
  }
}

const deleteUser = () => {
  if (isLogin.value) {
    store.deleteUser();
  } else {
    // 로그인 상태가 아니라면 회원탈퇴를 할 수 없음을 알림
    window.alert('로그인 상태가 아닙니다.');
  }
}

const openSearch = (movie) => {
    // selectedMovie.value = movie
    isSearchOpen.value = true
    console.log(isSearchOpen.value)
}





</script>

<style >
  /* @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;&display=swap'); */
  .mother-container {
    background-color: black;
    width: 50%;
    margin: auto;
    /* text-align: center; */
    display: flex;
    justify-content: center;
    /* align-content: center; */
  }

  .profile-image {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  }

  body * {
    color: rgb(255, 255, 255);
  }

  .nav-bar {
    display: flex;
    margin: 22px auto;
    position: absolute;
    margin-bottom: 20px;
    z-index: 1;
    gap: 30px;
    /* box-shadow: 0 0 10px black; */
  }
  
  .text-with-shadow {
    font-size: 14px;
    font-weight: 600;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    font-family: 'Poppins', sans-serif;
    text-decoration: none;
    }

  .profile {
    display: inline-block; 
    position: absolute;
    right: 30px;
    top: 15px;
  }

  .logo {
    display: inline-block;
    position: absolute;
    left: 40px;
    top: 20px;
  } 

  .logo img {
    width: 130px;
  }

  * {
    font-family: 'Noto Sans KR', sans-serif;
  }

  hr {
    height: 0.1px;
    background-color: #7e7e7e;
    border: none;
  }

  .card-list {
        margin-top: 10px;
        display: flex;
        gap: 2.1%;
        width: 100%;
        flex-wrap: wrap;
        /* justify-content: space-between; */
  }
  
  .card {
    border: none;
    border-radius: 4px;
    width: 23%;
    margin-bottom: 10px;
    text-align: center;
    transition: transform 0.4s ease;
    cursor: pointer;
    }
  
  .card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(197, 197, 197, 0.5);
  }
  
  .movie-poster {
      border-radius: 0.5rem;
      width: 100%;
      object-fit: contain;
  }

  .search-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7); /* 배경 색상과 투명도 조절 */
  z-index: 1;
  cursor: pointer;
}
</style>
