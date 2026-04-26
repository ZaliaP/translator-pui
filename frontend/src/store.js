import { reactive } from 'vue'

// Tworzymy globalny, reaktywny "magazyn" danych
export const authStore = reactive({
  // Na razie wymuszamy status zalogowanego (true), żeby widzieć efekty w Ustawieniach
  isLoggedIn: true, 
  user: {
    name: 'Mateusz', // Tu wstaw swoje imię!
    email: 'mateusz@example.com'
  },
  
  // Funkcje do zmiany stanu
  login() {
    this.isLoggedIn = true
  },
  logout() {
    this.isLoggedIn = false
  }
})