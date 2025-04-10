<template>
  <div class="container">
    <div style="display: flex;">
      <h1 style="margin-top: 20px; margin-bottom: 0;">너 자신을 알라</h1>
    </div>
    <div>
      <p style="margin-top: 5px;">맘에 드는 영화를 골라 자신을 더 깊이 알아가보세요.</p>
    </div>
    <div class="card-list">
      <div v-for="movie in movies" 
      :key="movie.id"
      class="card">
      <!-- {{ movie.genre_ids }} -->
      <img :src="getMoviePosterUrl(movie.poster_path)" alt="movie_poster" class="movie-poster">
      <p>{{ movie.title }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const movies = ref([]);
const TMDB_API_KEY = '7129c2707bdcc88780b426387d0a1c89';

const getMovies = async () => {
  const totalPages = 5; // 표시할 총 페이지 수
  const requests = [];

  // 여러 페이지의 데이터를 가져오기 위한 각 페이지의 axios 요청 생성
  for (let pageNum = 1; pageNum <= totalPages; pageNum++) {
    const movieURL = `https://api.themoviedb.org/3/movie/popular?api_key=${TMDB_API_KEY}&language=ko-KR&sort_by=popularity.desc&page=${pageNum}`;
    requests.push(axios.get(movieURL));
  }

  try {
    // 각 페이지의 데이터를 병렬로 요청하고 결과를 합침
    const responses = await Promise.all(requests);
    const allMovies = responses.flatMap(response => response.data.results);
    movies.value = shuffle(allMovies);
  } catch (error) {
    console.error(error);
  }
};

onMounted(() => {
  getMovies();
});

function shuffle(array) {
  // Fisher-Yates 섞기 알고리즘
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

const getMoviePosterUrl = (posterPath) => {
  if (posterPath) {
    return `https://image.tmdb.org/t/p/original${posterPath}`;
  } else {
    return 'https://via.placeholder.com/500x750'; // Replace with your default image URL
  };
}

// Function to load more movies with a new page number
const loadMoreMovies = () => {
  getMovies();
};
</script>

<style scoped>
.container {
  margin-top: 50px;
}
.card-list {
        margin-top: 20px;
        display: flex;
        gap: 10px;
        width: 100%;
        flex-wrap: wrap;
        justify-content: space-between
}
</style>