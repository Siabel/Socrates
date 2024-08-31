<template>
    <div class="container">
        <!-- <h1>서비스 소개 페이지</h1> -->
        <div class="onboarding-background">
          <img src="@/assets/onboarding-background-1.jpg" alt="">
        </div>

        <div class="onboarding-header">
            <div class="logo">
                <img src="@/assets/SOCRATES-Logo.png" alt="로고 이미지"/>
            </div>

            <div>
                <RouterLink :to="{ name: 'SignUp'}">
                  <button class="signup-btn">회원가입</button>
                </RouterLink> 
            </div>

        </div>

        <div class="onboarding-content" >
          <div class="onboarding-ment-container" :class="{ 'active': isMentVisible }">
            <h1 class="onboarding-ment">내가 도대체 어떤 영화를 <br> 좋아하는지 모르겠다면.. </h1>
          </div>
          
          <div class="onboarding-ment-container-2" :class="{ 'active': isMentVisible }">
            <h1 class="onboarding-ment">SOCRATES를 통해 <br> 자신의 영화 취향을 <br> 찾아가보세요.</h1>
          </div>

          <div style="margin-top: 40px;" class="onboarding-ment-container" :class="{ 'active': isMentVisible }">
            <RouterLink :to="{ name: 'Login'}" @click="ChangeLog">
              <button class="login-btn">소크라테스 로그인</button>
            </RouterLink>
          </div>

          <div>
            <img src="@/assets/socrates-png.png" alt="socrates img" class="socrates-img">
          </div>
          
          <div style="margin-top: 90%;" class="onboarding-ment-container" :class="{ 'active': isMentVisible }">
            <p style="margin-bottom: 10px;" class="onboarding-ment">소크라테스는 말했습니다.</p>
            <h1 style="margin-top: 0;"  class="onboarding-ment"> "너 자신을 알라"</h1>
          </div>
          

          <div style="margin-top: 40px;" class="onboarding-ment-container-2" :class="{ 'active': isMentVisible }">
            <p class="onboarding-ment">나 자신을 이해하는 것은 <br> 삶에 있어 굉장히 중요합니다.</p>
          </div>

          <div style="margin-top: 40px;" class="onboarding-ment-container" :class="{ 'active': isMentVisible }">
            <p class="onboarding-ment">당신은 SOCRATES를 통해 <br> 어떤 영화를 즐기는지 <br>찾게 될 것이며,</p>
          </div>
          
          <div style="margin-top: 40px;" class="onboarding-ment-container-2" :class="{ 'active': isMentVisible }">
            <h2 class="onboarding-ment" style="margin: 0;">나아가 자기 자신을</h2>
            <h1 style="margin-top: 5px;" class="onboarding-ment">더욱 잘 이해하게 될 것입니다.</h1>
          </div>
        </div>
    </div>
    <!-- <RouterView /> -->
</template>

<script setup>
import { useRouter, RouterView, RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { onMounted, computed , ref} from 'vue'
import { defineProps } from 'vue';

const props = defineProps(['isNavBarVisible'])

// onMounted(() => {
//   isNavBarVisible.value = false;
// });

const router = useRouter()
const Authstore = useAuthStore()
const isLogin = computed(() => {
  return Authstore.isLogin
})


const logoImageUrl = '@/assets/SOCRATES-Logo.png'
// const profileImageUrl = computed(() => Authstore.profile_imageUrl || Authstore.defaultProfileImageUrl.value);

const ChangeLog = () => {
  if (isLogin.value) {
    Authstore.logOut()
    window.alert('로그아웃 되었습니다')
    console.log('로그아웃', isLogin.value)
    router.push({ name: 'OnBoarding'})
  } else {
    router.push({ name: 'Login' })
    console.log('로그인', isLogin.value)

  }
}

const deleteUser = () => {
  if (isLogin.value) {
    store.deleteUser();
  } else {
    // 로그인 상태가 아니라면 회원탈퇴를 할 수 없음을 알림
    window.alert('로그인 상태가 아닙니다.');
  }
}

const isMentVisible = ref(false);

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

const handleScroll = () => {
  const onboardingMentContainer = document.querySelector('.onboarding-ment-container');
  const onboardingMentContainerRect = onboardingMentContainer.getBoundingClientRect();

  // 적절한 위치에서 클래스 추가/제거
  if (onboardingMentContainerRect.top < window.innerHeight * 0.75 && onboardingMentContainerRect.bottom > 0) {
    isMentVisible.value = true;
  } else {
    isMentVisible.value = false;
  }
};
</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
}
.socrates-img {
  position: absolute;
  right: 15%;
  top: 100%;
  width: 400px;
}
.onboarding-header {
    position: absolute;
    background-color: black;
    width: 100%;
    height: 50px;
    z-index: 2;
}
.onboarding-content {
    margin-top: 50%;
    text-align: center;
    z-index: 3;
}
.onboarding-background {
  z-index: 0;
  position: absolute;
}
.onboarding-background img{
  width:100%
}
.login-btn {
  background-color: rgb(0, 146, 93);
  border-radius: 8px;
  border-color: transparent;
  height: 60px;
  width: 280px;
  color: white;
  font-size: 18px;
  font-family: Noto Sans KR;
  font-weight: 600;
  cursor: pointer;

}

.signup-btn {
    background-color: rgb(0, 146, 93);
    border-radius: 8px;
    border-color: transparent;
    height: 40px;
    width: 120px;
    color: white;
    font-size: 14px;
    font-family: Noto Sans KR;
    font-weight: bold;
    display: inline-block; 
    position: absolute;
    right: 30px;
    top: 10px;
    cursor: pointer;
}

.login-btn:hover,
.signup-btn:hover {
  background-color: rgb(0, 83, 53);
  transition: background-color 0.3s ease;
    }
.onboarding-ment {
  margin: 20px 0;
}

.onboarding-ment-container {
  transform: translateY(0);
  transition: transform 0.5s ease;
}

.onboarding-ment-container.active {
  transform: translateY(-30px); /* 적절한 값으로 조절 */
}
.onboarding-ment-container-2 {
  transform: translateY(0);
  transition: transform 1s ease;
}

.onboarding-ment-container-2.active {
  transform: translateY(-20px); /* 적절한 값으로 조절 */
}


</style>