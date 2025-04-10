<template>
    <!-- 로그인 폼 -->
    <div v-if="formType === 'login'" class="login-form">
        <form @submit.prevent="logIn">

          <div>
            <!-- <label for="username">Username:</label> -->
            <input type="text" name="username" placeholder="아이디" 
            v-model.trim="username" class="input-field">
          </div>

          <div>
            <!-- <label for="password">Password:</label> -->
            <input type="password" name="password" placeholder="비밀번호" 
            v-model.trim="password" class="input-field">
          </div>

          <div style="margin-top: 20px;">
            <button class="login-btn">로그인</button>
          </div>

          <div style="margin-top:20px; display: flex;" >
            <label for="birth_date">아직 회원이 아니신가요?</label>
          </div>

          <div>
            <button @click="goToSignUp" class="signup-btn">회원가입</button>
          </div>

        </form>
    </div>

    <!-- 회원가입 폼 -->
    <div v-else-if="formType === 'signup'">
        <form @submit.prevent="handleSubmit" class="signup-form">

          <div>
            <!-- <label for="username">아이디 : </label> -->
            <input type="text" name="username" placeholder="아이디" 
            v-model.trim="username" class="input-field" style="margin-bottom: 15px;">
          </div>

          <div>
            <!-- <label for="password">비밀번호 : </label> -->
            <input type="password" name="password1" placeholder="비밀번호" 
            v-model.trim="password1" class="input-field">
          </div>

          <div>
            <!-- <label for="password">비밀번호 확인 : </label> -->
            <input type="password" name="password2" placeholder="비밀번호 확인" 
            v-model.trim="password2" class="input-field" style="margin-bottom: 15px;">
          </div>
          
          <div>
            <!-- <label for="nickname">닉네임 : </label> -->
            <input type="text" name="nickname" placeholder="닉네임" 
            v-model.trim="nickname" class="input-field">
          </div>
          
          <!-- <div>
            <label for="profile_path">프로필 이미지 : </label>
            <input type="file" @change="handleFileChange">
          </div> -->

          <div>
            <!-- <label for="fullname">이름 : </label> -->
            <input type="text" name="fullname" placeholder="이름" 
            v-model.trim="fullname" class="input-field">
          </div>

          <div>
            <!-- <label for="email">이메일 : </label> -->
            <input type="email" name="email" placeholder="이메일" 
            v-model.trim="email" class="input-field" style="margin-bottom: 15px;">
          </div>
          
          <div style="display: flex;" >
            <label for="birth_date">생년월일</label>
          </div>
          
          <div>
            <input type="date" name="birth_date" placeholder="생년월일" 
            v-model.trim="birth_date" class="input-field">
          </div>

          
          <div>
            <div style="display: flex; margin-top: 20px;">
              <label for="hate_genres">선호하지 않는 장르 선택 :</label>
            </div>

            <div class="genre-container">
              <form @submit.prevent="submitGenre" class="genre-form">
                <div v-for="genre in genres" :key="genre.id" class="genre">
                  <input type="button" @click="toggleGenre(genre.id)" 
                  :class="{ active: isSelectedGenre(genre.id) }"
                  class="genre-input"
                  :value="genre.name">
                  <!-- {{ genre.name }} -->
                </div>
              </form>
            </div>
          </div>
          <button class="signup-btn">회원가입</button>
        </form>
        
      </div>
    </template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useMovieStore } from '@/stores/movie'
import { useRouter } from 'vue-router';


const AuthStore = useAuthStore()
const MovieStore = useMovieStore()
const props = defineProps(['formType', 'signUp'])
const router = useRouter()

// 회원가입 시 이용할 변수들
const username = ref('')
const password = ref('')
const password1 = ref('')
const password2 = ref('')
const email = ref('')
const birth_date = ref('')
const fullname = ref('')
const nickname = ref('')
const hate_genres = ref('')
const profile_path = ref(null)


// 이미지 파일 가져오기
// const handleFileChange = (event) => {
//   const file = event.target.files[0]
//   console.log(event.target)
//   profile_path.value = file
// }

// 싫어하는 장르 고르기
const selectedGenres = ref([])
const genres = ref([])

onMounted (() => {
  MovieStore.getGenres()
  genres.value = MovieStore.genres
})

const goToSignUp = function () {
  router.push('SignUp')
}

// 장르가 선택되었는지 여부를 판단하는 함수
// genreId가 배열에 없다면 index가 -1이 나옴
const toggleGenre = (genreId) => {
  const index = selectedGenres.value.indexOf(genreId)
  if (index === -1) {
    selectedGenres.value.push(genreId)
  } else {
    selectedGenres.value.splice(index, 1)
  }
}

// 선택된 장르 id값 return
const isSelectedGenre = (genreId) => {
  return selectedGenres.value.includes(genreId)
}

// 회원가입
const signUp = function() {
  // 재확인 비밀번호가 다를 때
  if (password1.value !== password2.value) {
      console.log('비밀번호 확인이 일치하지 않습니다.')
      return
  }
  const payload = { 
      username: username.value, 
      password1: password1.value, 
      password2: password2.value,
      email: email.value,
      nickname: nickname.value,
      birth_date: birth_date.value,
      fullname: fullname.value,
      profile_path: profile_path.value,
      hate_genres: hate_genres.value.split(',').join(','),
    }
    AuthStore.signUp(payload)
  }

// 싫어하는 장르 받기
const submitGenre = () => {
  MovieStore.setHateGenres(selectedGenres.value)
  hate_genres.value = MovieStore.hate_genres
  console.log('선택된 장르:', selectedGenres.value)
};

// 버튼 하나로 2개의 submit event를 실행하기 위해서
const handleSubmit = function (){
  signUp()
  submitGenre()
}

// 로그인
  const logIn = () => {
    const payload = { 
      username: username.value,
      password: password.value 
    }
    AuthStore.logIn(payload)
}


</script>

<style scoped>

input {
  border: none;
  border-radius: 7px;
  width: 360px;
  height: 36px;
  background-color: rgb(56, 56, 56);
  padding: 3px 8px;
}
.input-field::placeholder {
  color: rgb(201, 201, 201); /* 흰색으로 설정 */
  font-size: 15px;
  font-weight: 500;
}

button {
  border: none;
  background-color: rgb(0, 146, 93);
  border-radius: 7px;
  padding: 3px 8px;
  width: 376px;
  height: 44px;
  font-size: 15px;
  font-weight: 700;
}
.genre-container {
  width: 376px;
}
.genre-form {
  width: 376px;
  display: flex;
  flex-wrap: wrap;
  /* justify-content: space-between; */
}
.genre {
  display: inline-block;
  width: 25%;
  margin: 0;
  height: 30px
}
.genre-input {
  width: 90%;
  display: flex;
  justify-content: center;
  border-radius: 5px;
}
.genre-input:hover,
button:hover {
  background-color: rgb(182, 33, 6);
  transition: background-color 0.3s ease;
}
.active {
  background-color: rgb(182, 33, 6);
  color: #fff;
}
.signup-btn {
  margin-top: 10px;
}
.signup-btn:hover,
.login-btn:hover {
  background-color: rgb(0, 83, 53);
  transition: background-color 0.3s ease;
}

.signup-form div,
.login-form div {
  margin: 10px 0;
  padding: 0;
}
.signup-form input,
.login-form input {
  margin: 0;
}
</style>