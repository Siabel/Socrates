<template>
  <div class="profile-page">
    <h1>프로필 페이지</h1>
    <div>
      <img src="@/assets/socrates-png.png" alt="socrates img" class="socrates-img">

      <h3 style="margin-top:120px">더 나은 서비스를 위해 준비중입니다.</h3>
      <!-- <img v-if="getImageUrl" src="getImageUrl" alt="프로필 이미지" class="profile-image profile-container" /> -->
      <!-- <img v-else src="/default-profile-image.png" alt="기본 프로필 이미지" class="profile-image profile-container" /> -->
      <!-- <h2>{{ Authstore.profileData }}을 알라</h2> -->
      <!-- <p>성함 : {{ profile.fullname }}</p> -->
      <!-- <p>태어난 날 : {{ profile.birth_date }}</p> -->
      <!-- <p>이메일 : {{ profile.email }}</p> -->
      <!-- <p>자신을 알기 시작한 날 : {{ profile.date_joined }}</p> -->
      <!-- <div>
        <p> 싫어하는 장르 : {{ profile.hate_genres }}</p>
        <button>장르 변경</button>
      </div> -->
      <div style="display: flex; justify-content: center; gap:10px">

        <div>
          <button class="update-user-btn" @click="goToUpdateProfile">프로필 업데이트</button>
        </div>
        <div>
          <button class="delete-user-btn" @click="deleteUser">회원 탈퇴</button>
        </div>  
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, watchEffect } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import axios from 'axios'

const router = useRouter()
const Authstore = useAuthStore()
const profile = ref(null)

const getImageUrl = ref(null)

// console.log(profile)
const goToUpdateProfile = () => {
  router.push({ name: 'UpdateProfile' })
}

// 프로필 이미지 불러오기
// const fname = ref("Vue")

// function getImageUrl(name) {
  //   return new URL(`/src/assets/images/${name}.png`, import.meta.url).href;
  // }
  
  // 회원 탈퇴
  const deleteUser = () => {
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/delete/`,
      headers: {
        Authorization: `Token ${Authstore.token}` 
      },
    })
    .then((res) => {
      window.alert('회원탈퇴가 완료되었습니다.')
      Authstore.logOut() // 회원탈퇴 후 로그아웃 처리
    })
    .catch((err) => {
      console.error('회원탈퇴 실패:', err)
    })
  }
  
  watchEffect(() => {
    Authstore.getMyProfile()
    getImageUrl.value = profile.profile_image
    profile.value = Authstore.profileData
    console.log(profile)
})

</script>

<style scoped>
.profile-page {
  margin-top: 80px;
  text-align: center;
}

.socrates-img {
  position: absolute;
  right: 10%;
  top: 30%;
  width: 400px;
}
.update-user-btn {
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


.delete-user-btn {
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

.update-user-btn:hover {
  background-color: rgb(0, 83, 53);
  transition: background-color 0.4s ease;
}

.delete-user-btn:hover {
  background-color: rgb(128, 128, 128);
  color: white;
  transition: background-color 0.3s ease;
}
</style>