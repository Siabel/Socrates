import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'


export const useMovieStore = defineStore('movies', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const movies = ref([])
  const genres = ref([])
  const comments = ref([])
  const query = ref('')
  const TMDB_API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MTI5YzI3MDdiZGNjODg3ODBiNDI2Mzg3ZDBhMWM4OSIsInN1YiI6IjY1M2IwNmU0NzE5YWViMDBjNDg5NDBlYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3TDMrUHoP81gjcte2F_JsA776OcS1kGmA0gNLEhGx4k'

  // 모든 장르 가지고 오기
  const getGenres = function () {
    axios({
      method: 'get',
      url: `${API_URL}/movies/genres/`
    })
      .then((res) =>{
        genres.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  // 선택된 싫어하는 장르가 포함되지 않은 영화들 가져오기
  const getGenreMovie = function (genre) {
    axios({
      method: 'get',
      url: `${API_URL}/movies/genre/${genre}/`
    })
      .then((res) =>{
        // console.log(res.data)
        movies.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return { TMDB_API_KEY, query, movies, genres, comments, getGenres, getGenreMovie };
}, { persist: true })