class ApiService {
    constructor(baseURL) {
      this.baseURL = baseURL;
      this.msgError = ""; 
    }
  
    async registrarUsuario(datosUsuario) {
      try {
        const respuesta = await fetch(`http://127.0.0.1:8000//usuarios/registro/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(datosUsuario),
        });
  
        if (respuesta.status === 400) {
          const errorData = await respuesta.json();
          this.msgError = errorData.mensaje; 
          alert(respuesta.status+": "+errorData.mensaje+"\n"+errorData);
          return null; 
        }
  
        if (respuesta.status === 200) {
          const usuarioRegistrado = await respuesta.json(); 
          return usuarioRegistrado; 
        }
  
        throw new Error("Error en el registro"); 
      } catch (error) {
        console.error("Error al registrar el usuario:", error);
        this.msgError = error.message; 
        return null; 
      }
    }
  
    async iniciarSesion(credenciales) {
      try {
        const respuesta = await fetch(`http://127.0.0.1:8000//usuarios/login/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(credenciales),
        });
  
        if (respuesta.status === 200) {
          return await respuesta.json(); 
        }
        else{
          const errorData = await respuesta.json();
          this.msgError = errorData.mensaje; 
          alert(respuesta.status+": "+errorData.mensaje+"\n"+errorData);
        }
  
        throw new Error("Error al iniciar sesión"); 
      } catch (error) {
        console.error("Error al iniciar sesión:", error);
        this.msgError = error.message; 
        return null; 
      }
    }
  }
  
  // Exportar una instancia de la clase con la URL base
  export default new ApiService("api");