import { defineStore } from "pinia";

export const useAuthStore = 
defineStore('auth',{
    state: () => ({
        token: null,
}),
actions: {
    setToken(token){
        this.token = token;
        localStorage.setItem('token', token);
        },
        getToken(){
            this.cargarDatos();
            return this.token;
        },
    logout(){
        this.token = null;
        localStorage.removeItem('token');
        },
        cargarDatos(){
            const token = localStorage.getItem('token');
            if(token){
                this.token = token;
            }
            
        }
    }
});