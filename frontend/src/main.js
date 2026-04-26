import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // Importujemy naszą mapę

const app = createApp(App)

app.use(router) // Mówimy Vue: "Używaj routera!"
app.mount('#app')