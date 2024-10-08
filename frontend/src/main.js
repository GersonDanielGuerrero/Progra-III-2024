import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from './router'
import { createPinia } from 'pinia' // Corrected import statement
import { useAuthStore } from './stores/auth'

const app = createApp(App);
const pinia = createPinia();
app.use(pinia);
app.use(router);
const authStore = useAuthStore();
authStore.cargarDatos();
app.mount('#app');




