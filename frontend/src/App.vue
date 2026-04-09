<template>
  <div class="translator-container">
    <h2>Nasz Super Tłumacz</h2>
    
    <input 
      v-model="textToTranslate" 
      type="text" 
      placeholder="Wpisz słowo..." 
    />

    <select v-model="targetLang">
      <option value="en">Angielski</option>
      <option value="de">Niemiecki</option>
      <option value="es">Hiszpański</option>
    </select>

    <button @click="sendTranslationRequest">Tłumacz!</button>

    <div v-if="translatedText">
      <h3>Wynik z serwera:</h3>
      <p>{{ translatedText }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

// To są nasze zmienne (stan aplikacji)
const textToTranslate = ref('')
const targetLang = ref('en')
const translatedText = ref(null)

// Funkcja, która odpala się po kliknięciu przycisku
const sendTranslationRequest = async () => {
  try {
    // Pakujemy nasze dane do obiektu
    const payload = {
      text: textToTranslate.value,
      lang: targetLang.value
    }
    console.log("Wysyłam JSON do backendu:", payload)

    // UWAGA: Tu wpiszesz adres URL, który poda Ci kolega od Backendu!
    // Na razie to przykładowy lokalny adres.
    const response = await axios.post('http://localhost:3000/api/translate', payload)
    
    // Zapisujemy odpowiedź z serwera, żeby wyświetliła się na ekranie
    // Zakładamy, że backend odeśle nam JSON-a np. { "translatedText": "Hello" }
    translatedText.value = response.data.translatedText
    
    console.log("Otrzymałem odpowiedź JSON:", response.data)

  } catch (error) {
    console.error("Błąd komunikacji z serwerem:", error)
  }
}
</script>

<style>
/* Trochę najprostszego CSS, żeby nie bolały oczy */
.translator-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 300px;
  margin: 50px auto;
  font-family: sans-serif;
}
input, select, button {
  padding: 10px;
  font-size: 16px;
}
</style>