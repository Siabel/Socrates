<template>
    <div style="margin-top: 40px;">
        <h3>관련 유튜브 영상</h3>
        <div class="video-card-list">
            <!-- <p>{{ props.selectedMovie.id }}</p> -->
            <!-- <div class="videoDiv marginMid">
                <iframe width="560" height="315" :src="videoUrl" frameborder="0" allowfullscreen></iframe>
            </div> -->
            <VideoCard v-for="(video, index) in videos"
            :key="video.id"
            :video="video"
            :index="index"
            />
        </div>
    </div>
</template>

<script setup>
import VideoCard from '@/components/youtube/VideoCard.vue'

import { ref, watch } from 'vue'
import axios from 'axios'

const props = defineProps({
    selectedMovie: Object,
})

const apiKey = 'AIzaSyDHTIoqsmHl70-Xp2Wu7AkMpWcZ0XI9ebs'
// const videoId =  ref(null)
// const videoUrl = ref(null)
const videos = ref(null)
const movieTitle = props.selectedMovie.title

// movieTitle을 관찰하며 바뀔 때마다 데이터 로드
watch(() => movieTitle, async (newMovieTitle) => {
  await loadMovieData(newMovieTitle)
}, { immediate: true })

// 영화 데이터와 관련 영상을 로드
async function loadMovieData(movieTitle) {
  try {
    const response = await axios({
      method: 'get',
      url: `https://www.googleapis.com/youtube/v3/search`,
      params: {
        part: 'snippet',
        q: `${movieTitle}`,
        type: 'video',
        key: apiKey
      }
    })
    console.log(response.data.items)
    videos.value = response.data.items

    // videoId.value = response.data.items[0].id.videoId
    // videoUrl.value = `https://www.youtube.com/embed/${videoId.value}`
  } catch (err) {
    console.error("YouTube API 요청 중 오류 발생: ", err)
  }
}
</script>

<style scoped>
/* .videoDiv {
    display: flex;
    justify-content: center;
}

.videoDiv iframe {
    border-radius: 10px;
} */
.video-card-list {
    margin: 20px 0;
    display: flex;
    align-content: start;
    gap: 6px;
    /* width: 100%; */
    flex-wrap: wrap;
    justify-content: space-between;
    }
.video-card {
  margin-top: 10%;
    border: 1px solid black;
    border-radius: 5%;
    /* width: 60%; */
    width: calc(50% - 5px);
    /* margin-bottom: 10px; */
    text-align: center;
    }

</style>