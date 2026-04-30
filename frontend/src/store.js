import { reactive } from 'vue'

// "reactive" sprawia, że Vue śledzi każdą zmianę w tym obiekcie
export const authStore = reactive({
  isLoggedIn: false,
  user: {
    name: ''
  },
  
  // Funkcja wylogowywania (przyda nam się do przycisku w Sidebarze)
  logout() {
    this.isLoggedIn = false
    this.user = { name: '' }
  }
})