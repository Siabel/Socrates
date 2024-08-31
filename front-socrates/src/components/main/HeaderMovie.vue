<template>
  <div>
    <div v-for="(movie, index) in movies" :key="movie.id">
      <!-- 첫 번째 요소를 제외하고 출력 -->
      <div v-if="index == 0" class="header-movie">
        <div class="movie-poster-container" 
        :style="{ backgroundImage: `url('${getMoviePosterUrl(movie.backdrop_path)}')` }">
        </div>

        <div> 
          <div>
            <h2 style="margin:0; margin-bottom: 20px;">당신이 빠져들 수도 있는 영화 :</h2>
          </div>
          <div class="header-movie-header">
            <div>
              <h1 style="margin-top: 0; margin-bottom: 0;">{{ movie.title }}</h1>
              <p style="margin-top: 0; margin-bottom: 0;">{{ getGenres(movie.genre_ids) }} | {{ movie.release_date }}</p>
            </div>
            <button @click="openModal(movies[0])" 
            class="header-movie-detail-button">자세히 보기</button>
          </div>
          <!-- <div class="header-movie-content"> -->
            <!-- <h3>줄거리</h3> -->
            <!-- <p>{{ movie.overview }}</p> -->
          <!-- </div> -->
        </div>
      </div>
    </div>
    <!-- <hr> -->
  </div>
</template>

<script setup>
import { defineProps, computed, onMounted } from 'vue'
import { useMovieStore } from '../../stores/movie';

const MovieStore = useMovieStore()
const props = defineProps({
    movies: {
        type: Array
    },
    openModal: {
        type: Function
    }
})

const getMoviePosterUrl = (posterPath) => {
    if (posterPath) {
        return `https://image.tmdb.org/t/p/original${posterPath}`
    } else {
        // If no poster path is available, you can provide a default image or an empty string
        return 'https://via.placeholder.com/500x750' // Replace with your default image URL
    }}

const genres = computed(() => MovieStore.genres)

const getGenres = (genreIds) => {
  const genreNames = genreIds.map((genreId) => {
    const genre = genres.value.find((g) => g.id === genreId)
    return genre ? genre.name : ''
  })

  return genreNames.join(', ')
}

onMounted(() => {
  MovieStore.getGenres()
})
// console.log(props)

// const headerMovie = props.movies
</script>

<style scoped>
/* .header-movie {
    position: relative;
} */

.movie-poster-container {
    width: 100%;
    height: 0;
    padding-bottom: 56.25%;
    background-size: cover;
    background-position: center;
    position: relative;
}

.movie-poster-container p {
    /* position: absolute; */
    bottom: 0;
    left: 0;
    right: 0;
    /* background-color: rgba(0, 0, 0, 0.7); */
    color: white;
    padding: 10px;
    margin: 0;
    /* z-index: 1; */
}

.movie-poster-container::before {
  content: '';
  background-image: linear-gradient(to bottom, #3b3b3b, transparent);
  position: absolute;
  height: 12%;
  width: 100%;
  /* z-index: 1; */
  pointer-events: none;
}
/* .gradient {
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.00) 0%, #000 17.1%);
  position: absolute;
  z-index: 2;
} */

.header-movie-detail-button {
    background-color: rgb(0, 146, 93);
    border-radius: 8px;
    border-color: transparent;
    height: 46px;
    color: white;
    font-size: 14px;
    font-family: Noto Sans KR;
    font-weight: bold;
    width: 120px;
    cursor: pointer;
}

.header-movie-detail-button:hover {
  background-color: rgb(0, 83, 53);
  transition: background-color 0.3s ease;
    }

.header-movie-header {
  display: flex; 
  align-items: center; 
  justify-content: space-between;
}


</style>