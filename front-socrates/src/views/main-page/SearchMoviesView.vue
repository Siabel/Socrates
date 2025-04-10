<template>
  <div>
    <div class="search-bar">
      <form class="d-flex" @submit.prevent="searchMovies">
        <input v-model="query" class="search-input" type="search" placeholder="영화 검색" aria-label="Search">
        <button class="search-button" type="submit">검색</button>
      </form>
    </div>

    <div v-if="movies.length > 0" class="card-list">
    <!-- <h2>검색 결과</h2> -->
    <!-- {{ movies }} -->
      <SearchedMovies v-for="movie in movies" 
      :key="movie.id" 
      :movie="movie" 
      @click="openModal(movie)"
      class="card"/>
    </div>
    <div v-else>
      <p style="margin-top: 220px;">검색 결과가 없습니다.</p>
    </div>

    <div v-if="isModalOpen" class="modal-background" @click="closeModal"></div>

    <div v-if="isModalOpen" class="movie-detail-modal">
        <MovieDetail 
        :selected-movie="selectedMovie"
        :close-modal="closeModal"/>
    </div>
  </div>
</template>

<script setup>
import MovieDetail from '@/components/main/MovieDetail.vue';
import SearchedMovies from '@/components/main/SearchedMovies.vue';

import { ref, computed, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import { useMovieStore } from '../../stores/movie'

const router = useRouter()

const selectedMovie = ref(null)
const isModalOpen = ref(false)
const query = ref('')
const MovieStore = useMovieStore()
const movies = computed(() => MovieStore.movies)


const openModal = (movie) => {
    selectedMovie.value = movie
    // console.log(selectedMovie.value)
    isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false;
}

const searchMovies = () => {
// 기본 URL
let apiUrl = `https://api.themoviedb.org/3/search/movie`;

// query 값이 존재하면 URL에 추가
const queryParams = {
  include_adult: false,
  language: 'ko-KR',
  page: 1,
};
if (query.value.trim() !== '') {
  queryParams.query = query.value.trim();
}

const clearQuery = () => {
  query.value = ''
}

onBeforeUnmount(() => {
  // 페이지를 떠날 때 query 초기화
  clearQuery();
});


const options = {
  method: 'GET',
  headers: {
    accept: 'application/json',
    Authorization: `Bearer ${MovieStore.TMDB_API_KEY}`,
  },
};

// URL에 쿼리 파라미터 추가
const queryString = Object.entries(queryParams)
  .map(([key, value]) => `${key}=${encodeURIComponent(value)}`)
  .join('&');

apiUrl += `?${queryString}`;

console.log(apiUrl); // 이 부분을 추가

fetch(apiUrl, options)
  .then(response => response.json())
  .then(data => {
    console.log(data.results)
    MovieStore.movies = data.results
  })
  .catch(err => {
    console.error(err);
  });
};



</script>

<style scoped>
.search-bar{
  text-align: right;
  display:inline-block;
}
.search-bar {
/* background-color: black; */
border-radius: 10px;
position: absolute;
/* width: 46%; */
/* min-width: 550px; */
/* max-height: 94%; */
top:15%;
left: 50%;
transform: translate(-50%, -50%);
/* padding: 20px; */
background-color: rgb(0, 0, 0);
/* box-shadow: 0 0 10px rgba(197, 197, 197, 0.5); */
/* text-align: center; */
overflow-y: auto;
z-index: 4;
box-shadow: 0 0 20px rgba(228, 228, 228, 0.6);
}

.search-input {
border: none;
height: 40px;
width: 376px;
background-color: black;
padding: 10px;
}
.search-button {
border: none;
height: 40px;
width: 80px;
background-color:rgb(0, 146, 93);
color: white;
cursor: pointer;
}

.search-button:hover {
background-color:rgb(0, 83, 53);
transition: background-color 0.3s ease;
}

.card-list {
  margin-top: 200px;
}

.modal-background {
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