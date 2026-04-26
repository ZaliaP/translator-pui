<script setup>
import { ref } from 'vue'
import Sidebar from '../components/Sidebar.vue'

// To nasza symulowana baza danych (Później będziemy to pobierać od Bartka!)
const savedPhrases = ref([
  { id: 1, source: 'Good morning', target: 'Dzień dobry', lang: 'EN 〉 PL' },
  { id: 2, source: 'How much does it cost?', target: 'Ile to kosztuje?', lang: 'EN 〉 PL' },
  { id: 3, source: 'Entschuldigung', target: 'Przepraszam', lang: 'DE 〉 PL' },
  { id: 4, source: 'Where is the bathroom?', target: 'Gdzie jest łazienka?', lang: 'EN 〉 PL' }
])

// Prosta funkcja do usuwania frazy z listy
const removePhrase = (idToRemove) => {
  savedPhrases.value = savedPhrases.value.filter(phrase => phrase.id !== idToRemove)
}
</script>

<template>
  <div class="dashboard-layout">
    
    <Sidebar />

    <main class="dashboard-content">
      <div class="content-header">
        <h1>Zapisane frazy</h1>
        <p>Twoje ulubione i najczęściej używane tłumaczenia.</p>
      </div>

      <div v-if="savedPhrases.length === 0" class="empty-state">
        <span class="icon">📭</span>
        <p>Nie masz jeszcze żadnych zapisanych fraz.</p>
      </div>

      <div v-else class="phrases-grid">
        
        <div v-for="phrase in savedPhrases" :key="phrase.id" class="phrase-card">
          <div class="card-header">
            <span class="lang-badge">{{ phrase.lang }}</span>
            <button @click="removePhrase(phrase.id)" class="delete-btn" title="Usuń">🗑️</button>
          </div>
          <div class="phrase-text source">{{ phrase.source }}</div>
          <div class="phrase-text target">{{ phrase.target }}</div>
        </div>

      </div>
    </main>

  </div>
</template>

<style scoped>
/* Główne ułożenie takie samo jak w Ustawieniach */
.dashboard-layout { display: flex; gap: 2rem; max-width: 1200px; margin: 2rem auto; }
.dashboard-content { flex: 1; display: flex; flex-direction: column; gap: 2rem; }
.content-header h1 { margin: 0 0 0.5rem 0; font-size: 2rem; color: #1a1c35; }
.content-header p { margin: 0; color: #666; }

/* Nowe style dla kart z frazami */
.phrases-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.phrase-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  transition: transform 0.2s, box-shadow 0.2s;
}

.phrase-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 15px rgba(0,0,0,0.08);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.lang-badge {
  background-color: #f0f2ff;
  color: #4a52ff;
  font-weight: bold;
  font-size: 0.8rem;
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
}

.delete-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.1rem;
  opacity: 0.5;
  transition: opacity 0.2s;
}

.delete-btn:hover {
  opacity: 1;
}

.phrase-text {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.phrase-text.source {
  color: #666;
  font-style: italic;
}

.phrase-text.target {
  color: #1a1c35;
  font-weight: bold;
}

.empty-state {
  text-align: center;
  padding: 4rem;
  background: #f9f9fa;
  border-radius: 12px;
  color: #666;
}

.empty-state .icon {
  font-size: 3rem;
  display: block;
  margin-bottom: 1rem;
}
</style>