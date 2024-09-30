<template class = "pagina">
    <div class="container">
        <div class="logo">
            <img src="../../public/imagenes/logo_color.png" alt="Good Burguer Logo" />
        </div>
        <form class="register-form">
            <CajaTexto 
            placeholder="Nombres"
            type="text"
            v-model="form.nombres"
            />

            <CajaTexto
            placeholder="Apellidos"
            type="text"
            v-model="form.apellidos"
            />

            <CajaTexto
            placeholder="Telefono"
            type="tel"
            v-model="form.telefono"
            />

            <CajaTexto
            placeholder="Correo Electronico"
            type="email"
            v-model="form.correo"
            />

            <CajaTexto
            placeholder="Contraseña"
            type="password"
            v-model="form.contraseña"
            />

            <CajaTexto 
            placeholder="Confirmar Contraseña"
            type="password"
            v-model="form.confirmar_contraseña"
            />

            <BotonComp @metodo_click="Registrarse">Registrar</BotonComp>
        </form>
    </div>
</template>

<style scoped>
.pagina{
    background-color: #000;
    padding: 0;
}

.container{
    margin: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #000;
    flex-direction: column;
    text-align: center;
}

.logo img{
    width: 150px;
    margin-bottom: 20px;
}

.register-form{
    width: 400px;
    background-color: #000;
    padding: 20px;
    border-radius: 8px;
}
</style>

<!-- C U I D A D I T O -->

<script>
import BotonComp from '@/components/BotonComp.vue';
import CajaTexto from '@/components/CajaTexto.vue';
export default {
    name: 'RegistroUsuario',
    components: {
        BotonComp,
        CajaTexto
    },
    data() {
        return {
            form:{
                nombres: '',
                apellidos: '',
                correo: '',
                contrasena: '',
                confirmarContrasena: ''
            }
        }
    },
    props: {
        
    },
    methods: {
        clic(){
            alert(this.form.nombres);
        }
    },
    computed: {
        
    },

}
</script>