<template>
    <div>
        <h1>메인</h1>
        <div class="header-movie">
            <HeaderMovie />
        </div>

        <div class="movie-list">
            <MovieList />
        </div>
    </div>
</template>

<script setup>
import HeaderMovie from '@/components/HeaderMovie.vue';
import MovieList from '@/components/MovieList.vue';


</script>

<style scoped>

</style>