import { defineStore } from "pinia";

export const useAuthStore = 
defineStore('auth',{
    state: () => ({
        token: null,
        usuario: null,
}),
actions: {
    setToken(token){
        this.token = token;
        localStorage.setItem('token', token);
        },
    setUsuario(usuario){
        this.usuario = usuario;
        localStorage.setItem('usuario', JSON.stringify(usuario));
        },
        getToken(){
            this.cargarDatos();
            return this.token;
        },
    logout(){
        this.token = null;
        this.usuario = null;
        localStorage.removeItem('token');
        localStorage.removeItem('usuario');
        },
        cargarDatos(){
            const token = localStorage.getItem('token');
            if(token){
                this.token = token;
            }
            
        }
    }
});