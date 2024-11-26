<template>
    <BarraMenu/>
    <div class="pagina-usuarios">
        <div class="contenedor">
            <div class="sidebar bg-secondary"></div>

            <div class="contenido">
                <h2 class="text-center mb-4">Gestión de usuarios de empleados</h2>

                <div class="lista-usuarios">
                    <div 
    v-for="usuario in usuarios" 
    :key="usuario.id" 
    class="usuario-card shadow-sm p-3 mb-3 bg-dark text-white rounded"
>
    <div class="d-flex justify-content-between align-items-center">
        <div>
            <h5 class="mb-1 nombre-usuario">{{ usuario.nombre }}</h5>
        </div>
        <div class="d-flex align-items-center">
            <p class="correo-usuario mb-0 me-2">{{ usuario.correo }}</p>
            <button 
                class="btn btn-outline-warning btn-sm"
                @click="editarRolesUsuario(usuario.id)"
            >
                ✏️
            </button>
        </div>
    </div>

    <div class="roles mt-1">
        <strong>Roles:</strong>
        <span 
            v-for="(rol, index) in usuario.roles" 
            :key="index" 
            class="badge-custom me-1"
        >
            {{ rol }}
        </span>
    </div>
</div>
</div>
        <div class=" text-center mt-4">
                <BotonComp
                @metodo_click="verInformacion">Ver Informacion sobre los roles
                </BotonComp>

                <BotonComp
                @metodo_click="registrarUsuario">Añadir usuario
                </BotonComp>
        </div>

            </div>
        </div>
    </div>
</template>

<style scoped>
.pagina-usuarios {
    display: flex;
    height: 100vh;
    overflow: hidden;
}

.contenedor {
    display: flex;
    width: 100%;
}

.sidebar {
    width: 18%; 
    background-color: #2b2b2b; 
    height: 75%; 
    margin: 40px 0;
    border-radius: 8px;
    margin-left: 15px;
}

.contenido {
    flex: 1;
    padding: 20px;
    color: #fff;
    overflow-y: auto;
}

.contenido h2 {
    font-weight: bold;
}

.contenido h5 {
    font-weight: bold;
    text-align: left;
}

.contenido p {
    text-align: right;
}

.lista-usuarios {
    max-width: 800px;
    margin: 0 auto;
}

.usuario-card {
    display: flex;
    flex-direction: column;
}

.nombre-usuario {
    font-size: 1rem;
    font-weight: bold;
    color: #fff; 
    word-break: break-word; 
}

.correo-usuario {
    font-size: 1rem;
    color: #fff;
    word-break: break-word; 
}

.roles {
    margin-top: 5px;
    display: flex;
}

.badge-custom {
    display: inline-block;
    padding: 0.3rem 0.7rem;
    border-radius: 12px;
    color: #FFF;
    font-size: 0.8rem;
    display: flex;
    border: 1px solid #ffad00;
    background-color: rgba(255, 255, 255, 0.1);
}

.badge-custom + .badge-custom {
    margin-left: 0.5rem;
}

.text-center button {
    font-size: 1rem;
    font-weight: bold;
    color: #000;
    background-color: #ffad00;
    border: none;
}

.text-center button:hover {
    background-color: #e69500;
}

.text-center button:not(:last-child) {
    margin-right: 10px; 
}

.correo-usuario {
    font-size: 0.9rem;
    color: #fff;
    word-break: break-word; 
}

.roles strong {
    color: #fff;
    margin-right: 5px;
}

.text-center {
    display: flex;
    justify-content: center;
    gap: 10px;
}

</style>

<script>
//importaciones de componentes

//fin de importaciones
import BarraMenu from '@/components/BarraMenu.vue';
import BotonComp from '@/components/BotonComp.vue';
import alertify from 'alertifyjs';
import 'alertifyjs/build/css/alertify.css';
export default {
    name: 'PaginaUsuarios',
    components: {
        BarraMenu,
        BotonComp,
    },
    data() {
        return {
            //variables
            usuarios: [
                {
                    id: 1,
                    nombre: 'Juan Pablo Pérez López',
                    correo: 'juanperez@goodburger.com',	
                    roles: ['Atención al cliente'],
                },
                {
                    id: 2,
                    nombre: 'Rigoberto Bartolomeo Benavides de la Concepción',
                    correo: 'rigobertobartolomeobenavidez@goodburger.com',
                    roles: ['Atención al cliente','Gestión de menú','Ventas y pedidos'], 
                },
                {
                    id: 3,
                    nombre: 'María Fernanda de la Trinidad',
                    correo: 'marifer@goodburger.com',
                    roles: ['Gestión de menú','Ventas y pedidos'],
                }
            ],
        }
    },
    methods: {
        //metodos
        abrirListaRoles(){
            alertify.success('Llamando al método: Abrir lista de roles');
        },
        editarRolesUsuario(id){
            alertify.success('Editar: '+id);
        },
        añadirUsuario(){
            alertify.success('Llamando al método: Añadir usuario');
        }
    },
}

</script>