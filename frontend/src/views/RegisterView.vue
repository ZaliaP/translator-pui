<script setup>
import { ref } from 'vue'

const username = ref('')
const email = ref('')
const password = ref('')
const passwordConfirm = ref('')

const handleRegister = (e) => {
  e.preventDefault()
  
  if (password.value !== passwordConfirm.value) {
    alert("Hasła nie są identyczne!")
    return
  }

  console.log("Rejestracja:", username.value, email.value, password.value)
  alert("Próba rejestracji (sprawdź konsolę!)")
}
</script>

<template>
  <div class="login-container">
    <div class="login-box">
      <h1 class="title">Zarejestruj się</h1>
      
      <p class="subtitle">
        Masz już konto? 
        <router-link to="/login" class="register-link">Zaloguj się</router-link>
      </p>

      <form @submit="handleRegister" class="login-form">
        <div class="input-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email" placeholder="Email" required>
        </div>

        <div class="input-group">
          <label for="username">Nazwa użytkownika</label>
          <input type="text" id="username" v-model="username" placeholder="Nazwa" required>
        </div>

        <div class="input-group">
          <label for="password">Hasło</label>
          <input type="password" id="password" v-model="password" placeholder="Hasło" required>
        </div>

        <div class="input-group">
          <label for="passwordConfirm">Powtórz hasło</label>
          <input type="password" id="passwordConfirm" v-model="passwordConfirm" placeholder="Powtórz hasło" required>
        </div>

        <button type="submit" class="submit-btn">Zarejestruj się</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
/* Używamy tych samych styli co w LoginView, żeby zachować spójność! */
.login-container { display: flex; justify-content: center; margin-top: 3rem; }
.login-box { background: white; padding: 3rem; width: 100%; max-width: 400px; }
.title { text-align: center; font-size: 1.8rem; margin-bottom: 0.5rem; }
.subtitle { text-align: center; color: #666; margin-bottom: 2rem; }
.register-link { color: #2a2e5d; font-weight: bold; text-decoration: none; }
.register-link:hover { text-decoration: underline; }
.login-form { display: flex; flex-direction: column; gap: 1.2rem; }
.input-group { display: flex; flex-direction: column; gap: 0.3rem; }
.input-group label { font-weight: bold; font-size: 0.95rem; color: #333; }
.input-group input { padding: 0.8rem; border: 1px solid #7c83b8; border-radius: 6px; outline: none; }
.input-group input:focus { border-color: #2a2e5d; box-shadow: 0 0 0 2px rgba(42,46,93,0.1); }
.submit-btn { background-color: #2a2e5d; color: white; border: none; border-radius: 6px; padding: 1rem; font-weight: bold; cursor: pointer; margin-top: 0.5rem; }
.submit-btn:hover { background-color: #1d2042; }
</style>