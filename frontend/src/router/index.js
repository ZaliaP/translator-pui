import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import SettingsView from '../views/SettingsView.vue'
import PhrasesView from '../views/PhrasesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
  path: '/ustawienia/frazy',
  name: 'phrases',
  component: PhrasesView
},
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/rejestracja',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/ustawienia',
      name: 'settings',
      component: SettingsView
    }
  ]
})

export default router