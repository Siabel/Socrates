import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/main-page/MainView.vue'
import OnBoardingView from '@/views/main-page/OnBoardingView.vue'
import TestView from '@/views/main-page/TestView.vue'
import SearchMoviesView from '@/views/main-page/SearchMoviesView.vue'

import LoginView from '@/views/accounts/LogInView.vue'
import SignUpView from '@/views/accounts/SignUpView.vue'
import ProfilePage from '@/views/accounts/ProfilePage.vue'
import UpdateProfile from '@/views/accounts/UpdateProfile.vue'

import CategoryCreateView from '@/views/community/CategoryCreateView.vue'
import CommunityView from '@/views/community/CommunityView.vue'
import CreatePostView from '@/views/community/CreatePostView.vue'
import PostDetailView from '@/views/community/PostDetailView.vue'
import PostUpdateView from '@/views/community/PostUpdateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'OnBoarding',
      component: OnBoardingView
    },
    {
      path: '/main',
      name: 'Main',
      component: MainView
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUpView
    },
    {
      path: '/community',
      name: 'Community',
      component: CommunityView
    },
    {
      path: '/test',
      name: 'Test',
      component: TestView
    },

    // Community Router
    {
      path: '/category',
      name: 'category',
      component: CategoryCreateView
    },
    {
      path: '/create',
      name: 'CreatePost',
      component: CreatePostView
    },
    {
      path: '/detail/:pk',
      name: 'detail',
      component: PostDetailView
    },
    {
      path: '/update/:pk',
      name: 'postUpdate',
      component: PostUpdateView
    },

  
    // 프로필 페이지
    {
      path: '/profile',
      name: 'ProfilePage',
      component: ProfilePage
    },
    // 프로필 수정
    {
      path: '/profile/edit',
      name: 'UpdateProfile',
      component: UpdateProfile
    },
    {
      path: '/search',
      name: 'SearchMoviesView',
      component: SearchMoviesView
    },
    // 404 Not Found Error
    // {
    //   path: '/errors/404NotFound',
    //   name: 'NotFound404',
    //   component: NotFound404
    // },
  ]
})


import { useAuthStore } from '@/stores/auth'

router.beforeEach((to, from) => {
  const store = useAuthStore()
  if ((to.name === 'Main'|| 
  to.name === 'ProfilePage' || 
  to.name === 'Test' || 
  to.name === 'CreatePost') && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'Login' }
  }
  if ((to.name === 'SignUp' || to.name === 'Login' || to.name === 'OnBoarding') && (store.isLogin)) {
    return { name: 'Main' }
  }
})

export default router