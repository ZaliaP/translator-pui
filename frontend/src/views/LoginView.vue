<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { authStore } from '../store.js'

const router = useRouter()

// Zmienne do przechowywania tego, co wpiszesz w pola
const username = ref('')
const password = ref('')
const errorMessage = ref('')

const handleLogin = () => {
  // Prosta walidacja – sprawdzamy, czy pola nie są puste
  if (username.value.trim() === '' || password.value.trim() === '') {
    errorMessage.value = 'Wypełnij wszystkie pola, aby się zalogować!'
    return
  }

  // Symulacja logowania (zanim Bartek dopisze prawdziwe API)
  // Wrzucamy do naszego magazynu wpisaną nazwę użytkownika
  authStore.user = { name: username.value }
  authStore.isLoggedIn = true

  // Przekierowujemy z powrotem na stronę główną
  router.push('/')
}
</script>

<template>
  <div class="login-container">
    <div class="login-card">
      <h2>Witaj z powrotem! 👋</h2>
      <p class="subtitle">Zaloguj się, aby uzyskać dostęp do swoich zapisanych fraz.</p>

      <form @submit.prevent="handleLogin" class="login-form">
        <div class="input-group">
          <label for="username">Nazwa użytkownika</label>
          <input 
            type="text" 
            id="username" 
            v-model="username" 
            placeholder="Wpisz swój login..." 
          />
        </div>

        <div class="input-group">
          <label for="password">Hasło</label>
          <input 
            type="password" 
            id="password" 
            v-model="password" 
            placeholder="Wpisz hasło..." 
          />
        </div>

        <p v-if="errorMessage" class="error-msg">{{ errorMessage }}</p>

        <button type="submit" class="btn-submit">Zaloguj się</button>
      </form>

      <div class="register-link">
        Nie masz jeszcze konta? <router-link to="/rejestracja">Zarejestruj się</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 70vh;
}

.login-card {
  background: white;
  padding: 3rem;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.08);
  width: 100%;
  max-width: 400px;
  border: 1px solid #e0e0e0;
}

h2 {
  color: #2a2e5d;
  margin-bottom: 0.5rem;
  text-align: center;
}

.subtitle {
  color: #666;
  text-align: center;
  margin-bottom: 2rem;
  font-size: 0.95rem;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

label {
  font-weight: bold;
  color: #333;
  font-size: 0.9rem;
}

input {
  padding: 0.8rem 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.2s;
}

input:focus {
  border-color: #4a52ff;
}

.error-msg {
  color: #ff4a4a;
  font-size: 0.85rem;
  text-align: center;
  margin: 0;
}

.btn-submit {
  background-color: #4a52ff;
  color: white;
  border: none;
  padding: 1rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 0.5rem;
}

.btn-submit:hover {
  background-color: #3a42d1;
}

.register-link {
  margin-top: 1.5rem;
  text-align: center;
  font-size: 0.9rem;
  color: #666;
}

.register-link a {
  color: #4a52ff;
  text-decoration: none;
  font-weight: bold;
}

.register-link a:hover {
  text-decoration: underline;
}
</style>