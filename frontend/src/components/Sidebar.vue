<script setup>
import { authStore } from '../store.js'
import { useRouter } from 'vue-router'

const router = useRouter()

const handleLogout = () => {
  // 1. Zmieniamy stan w globalnej pamięci na wylogowany
  authStore.logout() 
  // 2. Wyrzucamy użytkownika z Ustawień na stronę główną
  router.push('/')   
}
</script>

<template>
  <aside class="sidebar">
    <nav class="menu">
      <router-link to="/ustawienia" class="menu-item active">
        <span class="icon">⚙️</span> Ustawienia konta
      </router-link>
      
      <router-link to="/ustawienia/frazy" class="menu-item">
        <span class="icon">📝</span> Zapisane frazy
      </router-link>
      
      <router-link to="/ustawienia/jezyki" class="menu-item">
        <span class="icon">🌎</span> Zapisane języki
      </router-link>
    </nav>

    <button class="logout-btn" @click="handleLogout">
      <span class="icon">🚪</span> Wyloguj się
    </button>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 280px;
  background-color: #1a1c35; /* Ciemny granat */
  border-radius: 12px;
  padding: 2rem 1rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 600px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.menu {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  color: #a0a4cc;
  text-decoration: none;
  font-weight: bold;
  border-radius: 8px;
  transition: all 0.2s;
}

.menu-item:hover {
  background-color: #2a2e5d;
  color: white;
}

/* Styl dla aktualnie wybranej zakładki */
.menu-item.active {
  background-color: #4a52ff;
  color: white;
}

.icon {
  font-size: 1.2rem;
}

.logout-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background-color: transparent;
  color: #ff4a4a;
  border: 1px solid #ff4a4a;
  padding: 1rem;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.2s;
}

.logout-btn:hover {
  background-color: #ff4a4a;
  color: white;
}
</style>