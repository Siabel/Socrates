<template>
    <div class="update-profilepage">
      <h1>프로필 업데이트 페이지</h1>
      <form @submit.prevent="updateProfile" class="update-form">
        <div>
        <!-- <label for="newProfileImage">프로필 사진 변경</label> -->
        <!-- <input type="file" id="newProfileImage" ref="profileImageInput" @change="handleProfileImageChange" /><br> -->
        
        <div>
            <!-- <label for="nickname">닉네임 : </label> -->
            <input type="text" name="newNickname" placeholder="닉네임" 
            v-model.trim="nickname" class="input-field">
          </div>
  
        <div>
            <!-- <label for="email">이메일 : </label> -->
            <input type="email" name="newEmail" placeholder="변경할 이메일" 
            v-model.trim="email" class="input-field" style="margin-bottom: 15px;">
          </div>
        
        <!-- <label for="newBirthDate">생일 : </label> -->
        <!-- <input type="date" id="newBirthDate" v-model="newEmail" /><br> -->

        <div>
            <!-- <label for="password">비밀번호 : </label> -->
            <input type="password" name="newPassword1" placeholder="비밀번호" 
            v-model.trim="password1" class="input-field">
          </div>

          <div>
            <!-- <label for="password">비밀번호 확인 : </label> -->
            <input type="password" name="newPassword2" placeholder="비밀번호 확인" 
            v-model.trim="password2" class="input-field" style="margin-bottom: 15px;">
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
        </div>
  
        <button type="signup-btn">프로필 업데이트</button>
      </form>
    </div>
  </template>
  
  <script setup>
import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import axios from 'axios'
  import { useAuthStore } from '@/stores/auth'
  import { useMovieStore } from '@/stores/movie'

  const router = useRouter()
  const Authstore = useAuthStore()
  const MovieStore = useMovieStore()
  const props = defineProps(['formType', 'signUp'])

  const newNickname = ref('')
  const newEmail = ref('')
  const newPassword1 = ref('')
  const newPassword2 = ref('')
  const newBirthDate = ref('')
  const newHateGenres = ref('')
  // const newProfileImage = ref(null)

//   const handleProfileImageChange = (event) => {
//   // 선택된 파일을 저장
//   const file = event.target.files[0]
//   newProfileImage.value = file
// }

  const updateProfile = async () => {
  try {
    // FormData를 사용하여 파일을 서버로 전송
    const formData = new FormData()
    formData.append('nickname', newNickname.value)
    formData.append('email', newEmail.value)
    formData.append('newPassword1', newPassword1.value)
    formData.append('newPassword2', newPassword2.value)
    formData.append('birth_date', newBirthDate.value)
    formData.append('hate_genres', newHateGenres.value)
    // formData.append('profile_image', newProfileImage.value)

    const response = await axios.put(
      `${Authstore.API_URL}/profile/${Authstore.username}/update/`,
      formData,
      {
        headers: {
          'Authorization': `Token ${Authstore.token}`,
          'Content-Type': 'multipart/form-data', // 파일 업로드 시 필수
        },
      }
    )
  
      // 프로필 업데이트가 성공하면 프로필 페이지로 이동
      router.push({ name: 'ProfilePage' })
    } catch (error) {
      console.error('프로필 업데이트에 실패했습니다.', error)
    }
  }

  const selectedGenres = ref([])
  const genres = ref([])

  // 선택된 장르 id값 return
  const isSelectedGenre = (genreId) => {
  return selectedGenres.value.includes(genreId)
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

// 싫어하는 장르 받기

const submitGenre = () => {
  MovieStore.setHateGenres(selectedGenres.value)
  hate_genres.value = MovieStore.hate_genres
  console.log('선택된 장르:', selectedGenres.value)
};

onMounted (() => {
  MovieStore.getGenres()
  genres.value = MovieStore.genres
})

  </script>
  
  <style scoped>
.update-profilepage{
  margin-top: 60px;
}
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
  
  .update-form div,
  .login-form div {
    margin: 10px 0;
    padding: 0;
  }
  .update-form input,
  .login-form input {
    margin: 0;
  }
  </style>