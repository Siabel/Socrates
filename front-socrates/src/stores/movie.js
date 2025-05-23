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