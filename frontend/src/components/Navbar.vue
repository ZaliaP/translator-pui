<template>
  <nav class="navbar">
    <div class="logo">
      <router-link to="/" class="logo-link">
        <span class="icon">📖</span>
        <span class="brand-name">Super Tłumacz</span>
      </router-link>
    </div>
    
    <div class="nav-links">
      <router-link to="/rejestracja" class="nav-text">Rejestracja</router-link>
      <router-link to="/login" class="btn-login">Zaloguj się</router-link>
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
</style>