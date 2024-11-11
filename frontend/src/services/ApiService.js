import {useAuthStore} from '@/stores/auth';

class ApiService {
    constructor(baseURL) {
        this.baseURL = baseURL;
        this.msgError = "";
    }

    // Método para obtener el token del authStore
    obtenerToken() {
        const authStore = useAuthStore();
        return authStore.getToken();
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
                authStore.setToken(datos.access);
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

    // Método para guardar una dirección (POST o PUT según la acción)
    async guardarDireccion(direccion, accion, id = null) {
        let url = '';
        let metodo = '';

        if (accion === 'añadir') {
            url = `${this.baseURL}/usuarios/direcciones/`;
            metodo = 'POST';
        } else if (accion === 'editar' && id) {
            url = `${this.baseURL}/usuarios/direcciones/${id}`;
            metodo = 'PUT';
        }

        try {
            const token = this.obtenerToken();
            const response = await fetch(url, {
                method: metodo,
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json' 
                    },
                body: JSON.stringify(direccion),
            });

            if (!response.ok) {
                const errorData = await response.json();
                this.msgError = errorData.message || 'Error al guardar la dirección';
                throw new Error(this.msgError);
            }

            return await response.json();
        } catch (error) {
            console.error('Error en guardarDireccion:', error);
            throw error;
        }
    }

    // Método para cargar datos de una dirección (GET)
    async cargarDatos(id) {
        const url = `${this.baseURL}/usuarios/direcciones/${id}`;

        try {
            const token = this.obtenerToken();
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json' 
                },
            });

            if (!response.ok) {
                const errorData = await response.json();
                this.msgError = errorData.message || 'Error al cargar la dirección';
                throw new Error(this.msgError);
            }

            return await response.json();
        } catch (error) {
            console.error('Error en cargarDatos:', error);
            throw error;
        }
    }
}

// Exportar una instancia de la clase con la URL base
export default new ApiService("http://127.0.0.1:8000");

