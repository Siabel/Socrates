<template>
  <div v-if="index !==4" class="video-card">
    <iframe :src="`https://www.youtube.com/embed/${props.video.id.videoId}`" frameborder="0" allowfullscreen></iframe>
    <p>{{ video.snippet.title }}</p> 
  </div>
</template>

<script setup>

const props = defineProps({
  video: Object,
  index: Number
})


</script>

<style scoped>
iframe {
  border-radius: 4%;
  width: 100%;
  height: 90%;
}
</style>