<template>
    <div class="login-container">
      <nav>
        <a href="#">
          <img src="imagenes/imagen de good burger.jpg" alt="imagenes" width="200px">
        </a>
      </nav>
      <div class="form-wrapper"> 
        <h2>Iniciar sesión</h2>
        <form @submit.prevent="handleSubmit">
          <CajaTexto
            v-model="text"
            placeholder="Correo Electrónico"
            type="text"
            required
          />
          <CajaTexto
            v-model="password"
            placeholder="Contraseña"
            type="password"
            required
          />
  
          <div class="form-control">
            <span>¿Olvidaste tu contraseña?</span>
          </div>
          
          <BotonComp @click="handleLogin">Iniciar sesión</BotonComp>
          
          <div class="form-divider">
            <span>¿No tienes una cuenta?</span>
          </div>
          <BotonComp @click="handleRegister">Registrarse</BotonComp>

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

body{
  background-color: #000000;
  margin: 0;
  padding: 0;
  height: 100vh;
  width: 100vw;
}

body::before{
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    opacity: 0.5;
    width: 100%;
    height: 100%;
}

.container{
    text-align: center;

}

nav{
    display: flex;
    justify-content: center;
    text-align: center;
    align-items: center;
    padding: 30px 20px ;
}

nav img{
    height: 90px;
    width: 200px;
    margin-left: 10px;
    display: block;
}

.fora-wrapper{
    position: absolute;
    left: 50%;
    top: 56%;
    border-radius: 4px;
    padding: 20px;
    width: 600px;
    transform: translate(-50%,-50%);
    background: rgb(0, 0, 0)

}

.fora-wrapper h2{
    color: #fff;
    margin-bottom: 20px;
    text-align: center;
}

.fora-wrapper form  {
    margin: 25px 0 65px;
}

form .form-control{
    height: 50px;
    position: relative;
    margin-bottom: 16px;

}

 .form-control input{
   height: 100%;
   width: 100%;
   left: 200%;
    background: hsla(0, 0%, 36%, 0.49);
    border: none;
    outline: none;
    border-radius: 4px;
    color: #fbfbfb;
    font-size: 1rem;
    padding: 0 20px;

}

.form-control input:is(:focus, :valid){
    background: hsla(0, 6%, 80%, 0.164);
    padding: 16px 20px 0;

}

.form-control label{
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    color: #ffb005;
    font-size: 1rem;
    pointer-events: none;
    transition: all 0.1 ease;
}

.fora-wrapper input:is(:focus, :valid) ~ label{
    font-size: 0.75rem;
    color: rgb(255, 255, 255);
   transform: translateY(-130%);


}

form button{
    width: 60%; 
    display: block;
    margin: auto;
    padding: 9px 0;
    font-size: 1rem;
    background-color : #ffb005;
    color: #000000;
    border-radius: 4px;
    border: none;
    outline: none;
    cursor: pointer;
    transition: .1s ease;

}

form button:hover{
    background-color: #4444;
    color: #fffefe;
}

.fora-wrapper a{
    text-decoration: none;
}

.fora-wrapper a:hover{
    text-decoration: underline;
}

.fora-wrapper :where(label, p, small, a){
    font-size: 0.92rem;
    color: #fff;
}

form .form-help{
    display: flex;
    justify-content: space-between;
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