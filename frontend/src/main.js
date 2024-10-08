import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from './router'
import { createPinia } from 'pinia' // Corrected import statement

const app = createApp(App);
const pinia = createPinia();
app.use(pinia); 

app.use(router).mount('#app');




