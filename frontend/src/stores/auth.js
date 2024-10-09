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
            const usuario = localStorage.getItem('usuario');
            if(usuario){
                this.usuario = JSON.parse(usuario);
            }
        }
    }
});