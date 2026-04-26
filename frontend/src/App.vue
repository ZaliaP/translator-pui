<template>
  <div class="app-container">
    <Navbar />
    
    <main class="main-content">
      <router-view></router-view> 
    </main>
  </div>
</template>

<script setup>
// Musimy zaimportować nasz klocek, żeby Vue wiedziało skąd go wziąć
import Navbar from './components/Navbar.vue'
</script>

<style>
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
}

.main-content {
  padding: 2rem 4rem;
}
</style>