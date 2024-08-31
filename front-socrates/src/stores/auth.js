import axios from 'axios'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'


export const useAuthStore = defineStore('auth', () => {
  // profile 이미지 지정
  const defaultProfileImageUrl = ref('src/assets/default-profile-image.png');
  const profile_imageUrl = ref(null)
  const profileData = ref([])
  const setprofile_imageUrl = (url) => {
    profile_imageUrl.value = url || defaultProfileImageUrl
  }
  
  // 각 사용자의 정보를 저장하기 위해 정의
  const user = ref(null)
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)

  const isLogin = computed(() => {
    return token.value !== null
  })
  
  const signUp = function (payload) {
    const { 
      username, password1, password2, email, fullname, nickname, birth_date, hated_genres
    } = payload

    axios({
      method: 'post',
      url: `${API_URL}/api/v1/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
        email, 
        nickname,
        fullname,
        birth_date,
        hated_genres,
      }
    })
    .then((res) => {
      user.value = res.data
      window.alert('환영합니다!! 회원가입이 완료되었습니다!!')
      const password = password1
      logIn({ username, password })
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        router.push({ name: 'Main' })
      })
      .catch((err) => {        
        window.alert('등록되지 않은 아이디이거나, 틀린 비밀번호 입니다.')
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'OnBoarding' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getMyProfile = function () {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/profile/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
    })
    .then((res) => {
      console.log(res)
      profileData.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const UpdateProfile = function () {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/profile/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
    })
    .then((res) => {
      console.log(res)
      profileData.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  return { signUp, logIn, logOut, isLogin, token, API_URL, user, profileData,
    defaultprofile_imageUrl: defaultProfileImageUrl, profile_imageUrl, getMyProfile, setprofile_imageUrl,}
}, { persist: true })