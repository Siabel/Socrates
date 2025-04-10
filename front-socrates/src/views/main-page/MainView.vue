<template>
    <div>
        <!-- <h1>메인</h1> -->
        <div class="header-movie">
            <HeaderMovie 
            :movies="movies"
            :open-modal="openModal" 
            />
        </div>
        <hr>
        <div class="recommend-movies">
            <div style="display: flex;">
                <h2>볼만한 영화</h2>
            </div>
            <div class="card-list">
                <MovieList v-for="(movie, index) in movies"
                :key="movie.id"
                :movie="movie"
                :index="index"
                @click="openModal(movie)"
            />
            </div>
            
            <div v-if="isModalOpen" class="modal-background" @click="closeModal"></div>

            <div v-if="isModalOpen" class="movie-detail-modal">
                <MovieDetail 
                :selected-movie="selectedMovie"
                :close-modal="closeModal"/>
            </div>
        </div>
    </div>
</template>

<script setup>
import HeaderMovie from '@/components/main/HeaderMovie.vue';
import MovieList from '@/components/main/MovieList.vue';
import MovieDetail from '@/components/main/MovieDetail.vue';

import { ref, onMounted } from 'vue'
import axios from 'axios'

const movies = ref(null)
const selectedMovie = ref(null)

// const options = {
//     method: 'GET',
//     url: '',
//     params: {language: 'ko-KR', page: '1'},
//     headers: {
//         accept: 'application/json',
//         // Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ODA1MzYwZTQwMDg2MmUwZDA0OTZkMjA3ZjNjYjVjNiIsInN1YiI6IjY1NGRiMmQxNDFhNTYxMzM2ZDg3M2E4YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6PVdS6zi_zlXOUOCibmZmCtnUoprXVUfbPvitzjdP6I'
//     }
//     };

const TMDB_API_KEY = '7129c2707bdcc88780b426387d0a1c89'

const movieURL = `https://api.themoviedb.org/3/movie/popular?api_key=${TMDB_API_KEY}&language=ko-KR&sort_by=popularity.desc&page=1`

onMounted(() => {
    axios
        .get(movieURL)
        .then((response) => {
            // console.log(response)
            // console.log(response.data.results)
            movies.value = response.data.results
            // console.log(movies)
        }).catch((error) => {
            console.log(error)
        })
    });
// console.log(movies)


const isModalOpen = ref(false);

const openModal = (movie) => {
    selectedMovie.value = movie
    // console.log(selectedMovie.value)
    isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false;
}

</script>

<style scoped>

.header-movie {
    position: relative;
    /* z-index: 1; */
    margin-bottom: 20px;
}

.recommend-movies {
    margin-top: 1rem;
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