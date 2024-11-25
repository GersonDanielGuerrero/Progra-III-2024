<template>
    <div>
        
    </div>
</template>

<style scoped>

</style>

<script>
//importaciones de componentes

//fin de importaciones
import alertify from 'alertifyjs';
import 'alertifyjs/build/css/alertify.css';
export default {
    name: 'PaginaUsuarios',
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