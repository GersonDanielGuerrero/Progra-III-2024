<template>
  <BarraMenu />
  <div class="customer-service">
    <div class="header">
      <h2>Atención al Cliente</h2>
      <p>
        Bienvenidos. Atención al cliente.
        <span class="highlight">¿Qué le podemos ayudar?</span>
      </p>
      <div class="pregunta">
        <p>Recomendaciones con preguntas y hacen seguido los clientes.</p>
      </div>
    </div>

    <div class="preguntas">
      <div class="preguntas-item" v-for="pregunta in preguntas" :key="pregunta.id">
 
  <div class="pregunta-header">
    <span class="texto-pregunta">{{ pregunta.pregunta }}</span>
    <div class="acciones">
      <span class="icon" @click="toggleRespuesta(pregunta.id)">▼</span>
      <button @click="editarPregunta(pregunta.id)" class="edit-logo-btn">✏️</button>
    </div>
  </div>
 
  <div class="respuesta" v-if="pregunta.mostrarRespuesta">
    {{ pregunta.respuesta }}
  </div>
</div>
    </div>

    <div class="AÑADIR">
      <Botoncomp> AÑADIR PREGUNTA </Botoncomp>
    </div>
  </div>
</template>
  
 
<style scoped>
.preguntas-item {
  background-color: #000;
  border: 2px solid #ffad00; 
  color: #fff;
  padding: 20px;
  border-radius: 5px;
  margin-bottom: 10px;
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
.pregunta {
  margin-bottom: 20px;
  color: #ffffff;
}

.highlight {
  color: #ffad00;
}

.preguntas {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 40px;
  margin: 10px 180px;
}

.preguntas-item {
  background-color: #000;
  border: 2px solid #ffad00; 
  color: #fff;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 10px;
}


.pregunta-header {
  display: flex;
  justify-content: space-between; 
  align-items: center; 
}

.texto-pregunta {
  flex-grow: 1; 
  margin-right: 10px;
  text-align: left;
}


.acciones {
  display: flex;
  gap: 10px;
}

.respuesta {
  margin-top: 10px; 
  text-align: left;
  border: 2px solid #ffad00; 
  background-color: #000000; 
  padding: 10px;
  border-radius: 5px;
}

.actions {
  display: flex;
  gap: 5px;
  justify-content: space-between;
}

.icon, .edit {
  color: #ffad00;
  cursor: pointer;
}

.close-btn {
  background-color: #ffad00;
  color: #000;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
}

.AÑADIR {
    background-color: #ffad00;
  color: #000;
  padding: 0 10px; 
  font-size: 0.9em; 
  border-radius: 50px;
  width: auto; 
  display: inline-block; 
  margin: 10px auto; 
  text-align: center;
  background-color: #000000;
  color: #ffffff;
  padding: 10px 20px;
  border-radius: 10px;
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
import ApiService from '@/services/ApiService';
export default {
    name: 'PreguntasFrecuentes',
    components: {
     BarraMenu,
     Botoncomp

    },
    data() {
        return{
            preguntas: [
              {
                id: 1,
                pregunta: '¿A que hora abre el local?',
                respuesta: 'Abrimos a las 8:00 AM'
              },
              {
                id: 2,
                pregunta: '¿Hasta donde llegan los envios?',
                respuesta: 'Enviamos a todo el país'
              },
              {
                id: 3,
                pregunta: 'Pregunta de ejemplo 3',
                respuesta: 'Respuesta de ejemplo 3'
              },
              {
                id: 4,
                pregunta: 'Pregunta de ejemplo 4',
                respuesta: 'Respuesta de ejemplo 4'
              }
      ]

    };
  },
  methods: {
    async cargarPreguntas() {
      try {
        const respuesta = await ApiService.obtenerPreguntas();
        if (!respuesta.error) {
          this.preguntas = respuesta.datos.map(pregunta => ({
            ...pregunta,
            mostrarRespuesta: false 
          })); } else {
          console.error(respuesta.mensaje);
        }
      } catch (error) {
        console.error("Error al cargar preguntas frecuentes:", error);
      }
    },
    toggleRespuesta(id) {
      const pregunta = this.preguntas.find(p => p.id === id);
      if (pregunta) {
        pregunta.mostrarRespuesta = !pregunta.mostrarRespuesta;
      }
    },
    editarLogo() {
      console.log('Editar logo');
    }
  },
  async mounted() {
    await this.cargarPreguntas();
}
};
</script>