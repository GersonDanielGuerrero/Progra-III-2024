<template>
    <BarraMenu/>
    <div class="customer-service">
    <div class="header">
      <h2>Atención al Cliente</h2>
      <p>Bienvenidos. Atención al cliente. <span class="highlight">¿Qué le podemos ayudar?</span></p>
      <div class="preguntas">
      <p>Recomendaciones con preguntas y hacen seguido los clientes.</p>
      </div>
    </div>
    <div class="questions">
      <div class="question-item" v-for="(question, index) in questions" :key="index">
        <span>{{ question }}</span>
        <span class="actions">
          <span class="icon">▼</span>
          <button @click="editarLogo" class="edit-logo-btn">✏️</button>
        </span>
      </div>
    </div>
    <div class="AÑADIR">
    <Botoncomp> AÑADIR PREGUNTA </Botoncomp>
    </div>
  </div>
  </template>
  
 
<style scoped>
customer-service {
  text-align: center;
  width: 400px;
  margin: auto;
  background-color: #000;
  color: #fff;
  padding: 20px;
  border-radius: 10px;
  min-height: 100vh;
}

.header h2 {
  margin-bottom: 5px;
  color: #ffad00;
}
.header 
{
  margin-bottom: 20px;
  color: #ffad00;
}
.preguntas {
  margin-bottom: 20px;
  color: #ffffff;
}

.highlight {
  color: #ffad00;
}

.questions {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 40px;
  margin: 10px 180px;
}

.question-item {
  background-color: #000;
  border: 2px solid #ffad00;
  color: #fff;
  padding: 10px;
  border-radius: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.actions {
  display: flex;
  gap: 5px;
}

.icon, .edit {
  color: #ffad00;
  cursor: pointer;
}

.AÑADIR {
    background-color: #ffad00;
  color: #000;
  padding: 0 16px; 
  font-size: 0.9em; 
  border-radius: 5px;
  width: auto; 
  display: inline-block; 
  margin: 0 auto; 
  text-align: center;
  background-color: #000000;
  color: #ffffff;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;

}
.edit-logo-btn {
  background-color: transparent;
  color: #fff;
  border: none;
  cursor: pointer;
  font-size: 18px;
}

</style>

<script>
import BarraMenu from '@/components/BarraMenu.vue';
import Botoncomp from '@/components/BotonComp.vue';
export default {
    name: 'PreguntasFrecuentes',
    components: {
     BarraMenu,
     Botoncomp

    },
    data() {
        return{
            questions: [
        "¿A qué hora abre el local?",
        "¿Hasta dónde llegan los envíos?",
        "Pregunta de ejemplo",
        "Pregunta de ejemplo",
        "Pregunta de ejemplo",
        "Pregunta de ejemplo"
      ]
    };
  },
  methods: {
    addQuestion() {
      alert("Nueva pregunta agregada");
        }

    }
}
</script>