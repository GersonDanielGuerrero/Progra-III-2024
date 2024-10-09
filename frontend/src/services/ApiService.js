class ApiService {
    constructor(baseURL) {
      this.baseURL = baseURL;
      this.msgError = ""; 
    }
  
    async registrarUsuario(datosUsuario) {
      try {
        const respuesta = await fetch(`${this.baseURL}/usuarios/registro/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(datosUsuario),
        });
        
        const datos = await respuesta.json();

        if (respuesta.status === 400) {
          return { error: true, mensaje: datos};
        }
  
        if (respuesta.status === 200) {
          return { error: false, datos: datos };
        }
  
        throw new Error("Error en el registro"); 
      } catch (error) {
        console.error("Error al registrar el usuario:", error);
        this.msgError = error.message; 
        return { error: true, mensaje: error.message };
      }
    }
  
    async iniciarSesion(credenciales) {
      try {
        const respuesta = await fetch(`${this.baseURL}/usuarios/login/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(credenciales),
        });
  
        const datos = await respuesta.json();

        if (respuesta.status === 200) {
          // Guardar el token y redirigir
          localStorage.setItem('token', datos.token);
          window.location.href = '/pagina-principal'; // Redirigir a la página principal
          return { error: false, datos: datos };
        }

        this.msgError = datos.mensaje;
        return { error: true, mensaje: datos.mensaje };
        
      } catch (error) {
        this.msgError = error.message;
        return { error: true, mensaje: error.message };
      }
    }
    async obtenerProductos(categoria, filtro = "") {
      try {
        const queryParams = filtro ? `?categoria=${categoria}&filtro=${filtro}` : `?categoria=${categoria}`;
        const respuesta = await fetch(`${this.baseURL}/menu/productos/${queryParams}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });
  
        const datos = await respuesta.json();
  
        if (respuesta.status === 200) {
          return { error: false, datos: datos };
        }
  
        this.msgError = datos.mensaje;
        return { error: true, mensaje: datos.mensaje };
  
      } catch (error) {
        console.error("Error al obtener productos:", error);
        this.msgError = error.message;
        return { error: true, mensaje: error.message };
      }
    }
  }
  
  // Exportar una instancia de la clase con la URL base
  export default new ApiService("http://127.0.0.1:8000");
