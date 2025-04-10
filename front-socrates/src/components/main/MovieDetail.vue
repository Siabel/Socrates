<template>
  <div class="modal">
    <!-- <div class="close-bar"> -->
      <!-- <button @click="closeModal" class="close-button">
        <img src="@/assets/X.png" alt="close btn">
      </button> -->
    <!-- </div> -->
    <!-- <h1>영화 상세 모달</h1> -->
    <img :src="getMoviePosterUrl(selectedMovie.backdrop_path)" alt="movie_poster" class="movie-backdrop">
    <div class="movie-detail-content">
      <div class="movie-detail-content-header">
        <h1 class="movie-title">{{ selectedMovie.title }}</h1>
        <p>{{ getGenres(selectedMovie.genre_ids) }} | {{ selectedMovie.release_date }}</p>
      </div>
      <div class="header-movie-content">
        <h3>줄거리</h3>
        <p>{{ selectedMovie.overview }}</p>
      </div>
      <hr>
      <RelatedVideos :selected-movie="selectedMovie"/>
    </div>
  </div>
</template> 

<script setup>
import { defineProps, computed, onMounted } from 'vue'
import RelatedVideos from '@/components/youtube/RelatedVideos.vue'
import { useMovieStore } from '../../stores/movie';

const MovieStore = useMovieStore()

const props = defineProps({
selectedMovie: Object,
closeModal: Function
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
</script>

<style scoped>

.modal {
/* background-color: black; */
border-radius: 10px;
position: fixed;
width: 46%;
min-width: 550px;
max-height: 94%;
top: 50%;
left: 50%;
transform: translate(-50%, -50%);
/* padding: 20px; */
background-color: rgb(0, 0, 0);
box-shadow: 0 0 10px rgba(197, 197, 197, 0.5);
/* text-align: center; */
overflow-y: auto;
z-index: 4;
}

.modal-enter-from, .modal-leave-to {
transform: scale(0);
}

.modal-enter-active, .modal-leave-active {
transition: all 0.5s;
}

.modal-enter-to, .modal-leave-from {
transform: scale(1);
}
.modal::-webkit-scrollbar {
  display: none;
}
.modal img {
width: 100%;
}
.close-bar {
/* position: sticky; */
padding: 10px;
display: flex;
justify-content: end;
background-color: transparent;
z-index: 2;
}
.close-button {
background-color: transparent;
/* position: sticky;  */
border: none;
font-size: 16px;
cursor: pointer;
right: 10px;
/* z-index: 1; */
}

.close-button img {
width: 16px;
position: absolute;
}
.movie-detail-content {
/* margin-top: 250px; */
padding: 30px;
}

.movie-title {
margin: 0;
}

.movie-detail-content-header {
display: flex;
justify-content: space-between;
align-items: center;
}

/* .movie-backdrop {
position: absolute;
top: 0;
} */
</style>