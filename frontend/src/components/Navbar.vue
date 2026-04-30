<script setup>
import { authStore } from '../store.js'
</script>

<template>
  <nav class="navbar">
    <div class="logo">
      <router-link to="/" class="logo-link">
        <span class="icon">📖</span>
        <span class="brand-name">Super Tłumacz</span>
      </router-link>
    </div>
    
    <div class="nav-links">
      <!-- Jeśli użytkownik NIE JEST zalogowany -->
      <template v-if="!authStore.isLoggedIn">
        <router-link to="/rejestracja" class="nav-text">Rejestracja</router-link>
        <router-link to="/login" class="btn-login">Zaloguj się</router-link>
      </template>

      <!-- Jeśli użytkownik JEST zalogowany -->
      <template v-else>
        <router-link to="/ustawienia" class="nav-text user-profile">
          Cześć, {{ authStore.user.name }}! 
          <!-- dynamicznie pobieramy pierwszą literę imienia do avatara -->
          <span class="avatar">{{ authStore.user.name?.charAt(0).toUpperCase() || 'U' }}</span>
        </router-link>
      </template>
    </div>
  </nav>
</template>

<style scoped>
/* Scoped oznacza, że te style działają TYLKO w tym komponencie */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 4rem;
  border-bottom: 1px solid #e0e0e0;
  font-family: Arial, sans-serif;
}

.logo-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  color: #000;
  font-weight: bold;
  font-size: 1.2rem;
}

.icon {
  background-color: #2a2e5d;
  color: white;
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.nav-text {
  text-decoration: none;
  color: #333;
  font-weight: bold;
  font-size: 0.9rem;
}

.btn-login {
  background-color: #2a2e5d;
  color: white;
  text-decoration: none;
  padding: 0.6rem 1.5rem;
  border-radius: 6px;
  font-weight: bold;
  font-size: 0.9rem;
  transition: background-color 0.3s;
}

.btn-login:hover {
  background-color: #1d2042;
}

/* --- NOWE STYLE DLA ZALOGOWANEGO UŻYTKOWNIKA --- */
.user-profile {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  color: #2a2e5d;
  transition: opacity 0.2s;
}

.user-profile:hover {
  opacity: 0.8;
}

.avatar {
  background-color: #4a52ff;
  color: white;
  width: 35px;
  height: 35px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  font-weight: bold;
  font-size: 1rem;
}
</style>