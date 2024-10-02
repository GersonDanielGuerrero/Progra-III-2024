<template>
    <div class="bodi">
        <div class="midiv">
            <CajaTexto v-model="form.nombre" placeholder="Nombres" type="text"/>
            <CajaTexto v-model="form.apellido" placeholder="Apellidos" type="text" />
            <CajaTexto v-model="form.telefono" placeholder="Teléfono" type="tel"/>
            <CajaTexto v-model="form.correo" placeholder="Correo electrónico" type="email"/>
            <CajaTexto v-model="form.contraseña" placeholder="Contraseña" type="password"/>
            <CajaTexto v-model="form.confirmar_contraseña" placeholder="Confirmar contraseña" type="password"/>
            <BotonComp @metodo_click="registrarUsuario">Registrarse</BotonComp>
        </div>
    </div>
</template>

<style scoped>
    
    .bodi{
        background-color: black;
    }
    .midiv{
        width: 50%;
        margin: 0 auto;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

</style>

<!-- C U I D A D I T O -->

<script>
import CajaTexto from "@/components/CajaTexto.vue";
import BotonComp from "@/components/BotonComp.vue";
import ApiService from '@/services/ApiService';

export default {
    name: 'RegistroUsuario',
    components: {
        CajaTexto,
        BotonComp
    },
    data() {
    return {
      form: {
        nombre: "",
        apellido: "",
        telefono: "",
        correo: "",
        contraseña: "",
        confirmar_contraseña: "",
      },
      errores: {},
      msgError: '',
    };
  },
  methods: {
    async registrarUsuario() {
      this.errores = {}; // Limpiar errores previos
      if (this.validarFormulario()) {
        try {
          // Llama al método de la clase ApiService para registrar al usuario
          const response = await ApiService.registrarUsuario(this.form);

          // Si la respuesta es 200, registra al usuario y obtiene el pinche token
          if (response) {
            const respuestaLogin = await ApiService.iniciarSesion({
              correo: this.form.correo,
              password: this.form.contraseña,
            });

            // Si la respuesta del login es exitosa pues almacena el token
            if (respuestaLogin) {
              localStorage.setItem('token', respuestaLogin.token);
              this.$router.push('/pagina-principal'); // Redirige a la página principal (según yo)
            }
          } else {
            this.msgError = 'El correo ya está registrado o los datos no son válidos.';
          }
        } catch (error) {
          this.msgError = error.message; // Guarda el mensaje de error para mostrarlo digo yo
          console.error('Error en el registro o login:', error);
        }
      } else {
        alert(Object.values(this.errores).join('\n'));
      }
    },

    validarFormulario() {
      let esValido = true;
      const camposRequeridos = [
        "nombre",
        "apellido",
        "telefono",
        "correo",
        "contraseña",
        "confirmar_contraseña",
      ];

      camposRequeridos.forEach((campo) => {
        if (this.form[campo].trim().length === 0) {
          this.errores[campo] = `El campo "${this.capitalizarNombreCampo(campo)}" es obligatorio.`;
          esValido = false;
        }
      });

      // Validaciones específicas
      if (this.form.nombre.length < 3 || this.form.nombre.length > 50) {
        this.errores.nombre = "El nombre debe tener entre 3 y 50 caracteres.";
        esValido = false;
      }
      if (this.form.apellido.length < 3 || this.form.apellido.length > 50) {
        this.errores.apellido = "El apellido debe tener entre 3 y 50 caracteres.";
        esValido = false;
      }
      if (!this.validarTelefono(this.form.telefono)) {
        this.errores.telefono = "El teléfono debe tener el formato 0000-0000.";
        esValido = false;
      }
      if (!this.validarCorreo(this.form.correo)) {
        this.errores.correo = "El correo electrónico no es válido.";
        esValido = false;
      }
      if (!this.validarContraseña(this.form.contraseña)) {
        this.errores.contraseña = "La contraseña debe tener entre 6 y 50 caracteres, con al menos una mayúscula, una minúscula y un número.";
        esValido = false;
      }
      if (this.form.contraseña !== this.form.confirmar_contraseña) {
        this.errores.confirmar_contraseña = "Las contraseñas no coinciden.";
        esValido = false;
      }

      return esValido;
    },
    capitalizarNombreCampo(nombreCampo) {
      return nombreCampo.charAt(0).toUpperCase() + nombreCampo.slice(1);
    },
    validarCorreo(correo) {
      const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      return re.test(correo);
    },
    validarTelefono(telefono) {
      const re = /^\d{4}-\d{4}$/;
      return re.test(telefono);
    },
    validarContraseña(contraseña) {
      const re = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{6,50}$/;
      return re.test(contraseña);
    },
  },
};


</script>