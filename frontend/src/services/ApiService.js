import useAuthStore from '@/stores/auth';

class ApiService {
    constructor(baseURL) {
        this.baseURL = baseURL;
        this.msgError = "";
    }

    // Método para obtener el token del authStore
    obtenerToken() {
        const authStore = useAuthStore();
        return authStore.token;
    }
      // Método para cargar los datos del usuario, direcciones y roles
async cargarDatos() {
    const token = this.obtenerToken(); 
    try {
        
        const respuesta = await fetch(`${this.baseURL}/usuarios/cuenta`, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`, 
                "Content-Type": "application/json",
            },
        });

        if (respuesta.ok) {
            const datos = await respuesta.json();

            const usuario = {
                nombres: datos.usuario.nombres,
                apellidos: datos.usuario.apellidos,
                correo: datos.usuario.correo,
                telefono: datos.usuario.telefono,
            };

            const direcciones = datos.direcciones.map(direccion => ({
                id: direccion.id,
                nombre: direccion.nombre,
                direccion: direccion.direccion,
                predeterminada: direccion.predeterminada,
            }));

            const roles = datos.roles.map(rol => ({
                id: rol.id,
                nombre: rol.nombre,
            }));

            return {
                error: false,
                usuario: usuario,
                direcciones: direcciones,
                roles: roles
            };
        }

        const datos = await respuesta.json();
        this.msgError = datos.mensaje || 'Error al obtener la cuenta';
        return { error: true, mensaje: this.msgError };

    } catch (error) {
        console.error("Error al obtener la cuenta:", error);
        this.msgError = error.message;
        return { error: true, mensaje: error.message };
    }
}

   // Método para actualizar los datos de la cuenta
async actualizarCuenta(datosCuenta) {
    const token = this.obtenerToken();  // Obtener el token
    try {
        const respuesta = await fetch(`${this.baseURL}/usuarios/cuenta`, {
            method: "PUT",
            headers: {
                "Authorization": `Bearer ${token}`,  // Incluir el token en los encabezados
                "Content-Type": "application/json",
            },
            body: JSON.stringify(datosCuenta),
        });

        if (respuesta.ok) {
            const datos = await respuesta.json();
            return { error: false, datos: datos };
        }

        const datos = await respuesta.json();
        this.msgError = datos.mensaje || 'Error al actualizar la cuenta';
        return { error: true, mensaje: this.msgError };

    } catch (error) {
        console.error("Error al actualizar la cuenta:", error);
        this.msgError = error.message;
        return { error: true, mensaje: error.message };
    }
}
      
 // Método para marcar una dirección como predeterminada y actualizar la variable direcciones
async marcarPredeterminada(id) {
    const token = this.obtenerToken(); 
    try {
        
        const response = await fetch(`${this.baseURL}/usuarios/direcciones/predeterminada`, {
            method: 'PUT',
            headers: {
                'Authorization': `Bearer ${token}`, 
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id }), 
        });

        const data = await response.json();

        if (response.ok) {
            
            const direcciones = data.direcciones.map((direccion) => ({
                id: direccion.id,
                nombre: direccion.nombre,
                direccion: direccion.direccion,
                predeterminada: direccion.predeterminada,
            }));
            
            return {
                error: false,
                mensaje: "Dirección marcada como predeterminada",
                direcciones: direcciones 
            };
        }

        return { error: true, mensaje: data.mensaje || "Error al marcar como predeterminada." };

    } catch (error) {
        console.error("Error al marcar como predeterminada:", error);
        return { error: true, mensaje: error.message || "Error al marcar como predeterminada." };
    }
}

    // Método para insertar productos, categorías o anuncios
    async insertarEntidad(entidad, datosEntidad) {
        const token = this.obtenerToken();
        try {
            const formData = new FormData();

            // Añadir los datos de la entidad al FormData
            for (const clave in datosEntidad) {
                formData.append(clave, datosEntidad[clave]);
            }

            const respuesta = await fetch(`${this.baseURL}/${entidad}/`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${token}`, // Enviar token
                },
                body: formData, // Enviar el FormData que contiene los datos y la imagen
            });

            if (respuesta.ok) {
                const datos = await respuesta.json();
                return { error: false, datos: datos };
            }

            const datos = await respuesta.json();
            this.msgError = datos.mensaje || 'Error al insertar';
            return { error: true, mensaje: this.msgError };

        } catch (error) {
            console.error(`Error al insertar ${entidad}:`, error);
            this.msgError = error.message;
            return { error: true, mensaje: error.message };
        }
    }

    // Método para actualizar productos, categorías o anuncios
    async actualizarEntidad(entidad, idEntidad, datosEntidad) {
        const token = this.obtenerToken();
        try {
            const formData = new FormData();

            // Añadir los datos de la entidad al FormData
            for (const clave in datosEntidad) {
                formData.append(clave, datosEntidad[clave]);
            }

            const respuesta = await fetch(`${this.baseURL}/${entidad}/${idEntidad}/`, {
                method: "PUT",
                headers: {
                    "Authorization": `Bearer ${token}`, // Enviar token
                },
                body: formData, // Enviar el FormData que contiene los datos y la imagen
            });

            if (respuesta.ok) {
                const datos = await respuesta.json();
                return { error: false, datos: datos };
            }

            const datos = await respuesta.json();
            this.msgError = datos.mensaje || 'Error al actualizar';
            return { error: true, mensaje: this.msgError };

        } catch (error) {
            console.error(`Error al actualizar ${entidad}:`, error);
            this.msgError = error.message;
            return { error: true, mensaje: error.message };
        }
    }

    // Método para eliminar productos, categorías o anuncios
    async eliminarEntidad(entidad, idEntidad) {
        const token = this.obtenerToken();
        try {
            const respuesta = await fetch(`${this.baseURL}/${entidad}/${idEntidad}/`, {
                method: "DELETE",
                headers: {
                    "Authorization": `Bearer ${token}`, // Enviar token
                },
            });

            if (respuesta.ok) {
                return { error: false, mensaje: `${entidad} eliminado correctamente` };
            }

            const datos = await respuesta.json();
            this.msgError = datos.mensaje || 'Error al eliminar';
            return { error: true, mensaje: this.msgError };

        } catch (error) {
            console.error(`Error al eliminar ${entidad}:`, error);
            this.msgError = error.message;
            return { error: true, mensaje: error.message };
        }
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

            if (respuesta.ok) {
                return { error: false, datos: datos };
            }

            this.msgError = datos.mensaje || 'Error al registrar el usuario';
            return { error: true, mensaje: this.msgError };

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

            if (respuesta.ok) {
                // Guardar el token y redirigir
                const authStore = useAuthStore();
                const usuario = datos.usuario;
                authStore.setToken(datos.token);
                authStore.setUsuario(usuario);
                window.location.href = '/pagina-principal'; // Redirigir a la página principal
                return { error: false, datos: datos };
            }

            this.msgError = datos.mensaje || 'Error al iniciar sesión';
            return { error: true, mensaje: this.msgError };

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

            if (respuesta.ok) {
                return { error: false, datos: datos };
            }

            this.msgError = datos.mensaje || 'Error al obtener productos';
            return { error: true, mensaje: this.msgError };

        } catch (error) {
            console.error("Error al obtener productos:", error);
            this.msgError = error.message;
            return { error: true, mensaje: error.message };
        }
    }
    async obtenerCategorias(){
        try {
            const respuesta = await fetch(`${this.baseURL}/menu/categorias/`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
            });

            const datos = await respuesta.json();

            if (respuesta.ok) {
                return { error: false, datos: datos };
            }

            this.msgError = datos.mensaje || 'Error al obtener productos';
            return { error: true, mensaje: this.msgError };

        } catch (error) {
            console.error("Error al obtener productos:", error);
            this.msgError = error.message;
            return { error: true, mensaje: error.message };
        }
    }
    async obtenerAnuncios(){
        try {
            const respuesta = await fetch(`${this.baseURL}/menu/productos/`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
            });

            
            const datos = await respuesta.json();

            if (respuesta.ok) {
                return { error: false, datos: datos };
            }

            this.msgError = datos.mensaje || 'Error al obtener productos';
            return { error: true, mensaje: this.msgError };

        } catch (error) {
            console.error("Error al obtener productos:", error);
            this.msgError = error.message;
            return { error: true, mensaje: error.message };
        }
    }
}

// Exportar una instancia de la clase con la URL base
export default new ApiService("http://127.0.0.1:8000");

