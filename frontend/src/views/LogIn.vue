<template>
    <div class="login-container">

          <img src="imagenes/imagen de good burger.jpg" alt="imagenes" width="200px">

      <div class="form-wrapper"> 
        <h2>Iniciar sesión</h2>
        <form @submit.prevent="handleSubmit">
          <CajaTexto
            class="caja-texto"
            v-model="correo"
            placeholder="Correo Electrónico"
            type="email"
            required
          />
          <CajaTexto
            class="caja-texto"
            v-model="password"
            placeholder="Contraseña"
            type="password"
            required
          />

            <span>¿Olvidaste tu contraseña?</span>

          
          <BotonComp @metodo_click="iniciar_sesion">Iniciar sesión</BotonComp>
          
          <div class="form-divider">
            <span>¿No tienes una cuenta?</span>
          </div>
          <BotonComp @metodo_click="registrarse">Registrarse</BotonComp>

        </form>
      </div>
    </div>
  </template>

<style scoped>

    *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    outline: none;
    border: none;
    text-decoration: none;
    text-transform: capitalize;
    padding: 20;
    box-sizing: border-box;
    
}


.container{
    text-align: center;

}

form{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}


.form-wrapper{
    margin: auto;
    position: absolute;
    left: 50%;
    top: 56%;
    border-radius: 4px;
    padding: 20px;
    width: 600px;
    transform: translate(-50%,-50%);
    background: rgb(0, 0, 0);
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.form-wrapper h2{
    color: #fff;
    margin-bottom: 20px;
    text-align: center;
}

.form-wrapper form  {
    margin: 25px 0 65px;
}


.form-wrapper :where(label, p, small, a){
    font-size: 0.92rem;
    color: #fff;
}


 .form-divider{
  display: block;
  position: relative;
  align-items: center;
  text-align: center;
  margin: 20px 0;
  color: #ffffff;

 }

.form-container {
    display: inline-flex;
    position: relative;
    color: #fcfcfc;
   
}

.form-divider::after,
.form-divider::before{
    content: "";
    position: absolute;
    width: 300px;
    height: 3px;
    background-color: currentColor; 
   top: 0.7rem
}

.form-divider::before{
    left: -129px;
    }
  
.form-divider::after{
    right: -129px;
}

.form-divider::before
.form-divider::after{
    content: "";
    flex: 1;
    background-color: rgb(255, 249, 249);
    margin: 0 1px;
}

.form-divider span{
    padding: 0 190px;
    font-size: 0.92rem;
    color: rgb(255, 255, 255);

}

.form-control{
    display: flex;
  align-items: center;
  text-align: center;
  margin: 3px 0;
  color: #ffb005;

}

.form-control span{
    width: 1000px;
    text-align: relative;
    margin-right: -319px;
    font-size: 0.92rem;
}
.caja-texto{
    width: 40vw;
    max-width: 600px;
}
</style>

<!-- C U I D A D I T O -->

<script>
import BotonComp from '@/components/BotonComp.vue';
import CajaTexto from '@/components/CajaTexto.vue';
export default {
    name: 'LogIn',
    components: {
        BotonComp,
        CajaTexto
    },
    data() {
        return {

        }
    },
    props: {
        
    },
    methods: {
        
    },
    computed: {
        
    },

}
</script>