<script setup>
// Importujemy nasz nowy klocek
import Sidebar from '../components/Sidebar.vue'
</script>

<template>
  <div class="dashboard-layout">
    
    <Sidebar />

    <main class="dashboard-content">
      <div class="content-header">
        <h1>Ustawienia konta</h1>
        <p>Zarządzaj swoimi danymi i preferencjami tłumacza.</p>
      </div>

      <div class="settings-card">
        <h3>Twoje dane</h3>
        <p>Miejsce na formularz zmiany danych...</p>
      </div>
    </main>

  </div>
</template>

<style scoped>
.dashboard-layout {
  display: flex;
  gap: 2rem;
  max-width: 1200px;
  margin: 2rem auto;
}

.dashboard-content {
  flex: 1; /* Sprawia, że prawa strona zajmuje całą resztę dostępnego miejsca */
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.content-header h1 {
  margin: 0 0 0.5rem 0;
  font-size: 2rem;
  color: #1a1c35;
}

.content-header p {
  margin: 0;
  color: #666;
}

.settings-card {
  background-color: white;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  padding: 2rem;
  min-height: 400px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.02);
}
</style>