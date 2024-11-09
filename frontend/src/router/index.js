import { createRouter, createWebHistory } from "vue-router";

import Login from "../views/LogIn.vue";
import Principal from "../views/PaginaPrincipal.vue";
import RegistroUsuario from "../views/RegistroUsuario.vue";
import PaginaMenu from "../views/PaginaMenu.vue";
import PaginaDireccion from "../views/PaginaDireccion.vue";

const routes = [
    {
        path: "/",
        name: "Principal",
        component: Principal
    },
    {
        path: "/registro",
        name: "Registro",
        component: RegistroUsuario,
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
    },
    {
        path: "/menu",
        name: "Menu",
        component: PaginaMenu,
    },
    {
        path: "/direccion",
        name: "Direccion",
        component: PaginaDireccion,
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;