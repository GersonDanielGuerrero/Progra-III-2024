import { createRouter, createWebHistory } from "vue-router";

import Registro from "../views/RegistroUsuario.vue";
import Login from "../views/LogIn.vue";
import Principal from "../views/PaginaPrincipal.vue";

const routes = [
    {
        path: "/",
        name: "Principal",
        component: Principal
    },
    {
        path: "/registro",
        name: "Registro",
        component: Registro,
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;