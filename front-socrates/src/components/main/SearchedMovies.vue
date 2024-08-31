<template>
    <div>

      <img :src="getMoviePosterUrl(movie.poster_path)" alt="movie_poster" class="movie-poster">
        <p>{{ movie.title }}</p>
    </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  movie: Object
})

const getMoviePosterUrl = (posterPath) => {
    if (posterPath) {
        return `https://image.tmdb.org/t/p/original${posterPath}`
    } else {
        // If no poster path is available, you can provide a default image or an empty string
        return 'https://via.placeholder.com/500x750' // Replace with your default image URL
    }}
</script>

<style scoped>

</style>