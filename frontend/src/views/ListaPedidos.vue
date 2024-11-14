<template>
    <div>
        
    </div>
</template>

<style scoped>

</style>

<script>
//Importaciones de componentes


//Fin de importaciones de componentes
export default {
    name: 'ListaPedidos',
    data() {
        return {
            pedidos:[
                {
                    id: 1,
                    fecha: '2024-11-11 11:11:11',
                    nombre_cliente: 'Juan Perez',
                    tipo: 'Domicilio',
                    direccion: '8va Calle poniente, Barrio La Parroquia, Santa Elena',
                    cantidad_productos: 2,
                    total: 12.50,
                },
                {
                    id: 2,
                    fecha: '2024-11-11 12:44:11',
                    nombre_cliente: 'Maria Lopez',
                    tipo: 'Local',
                    direccion: '4ta Avenida Sur, Barrio El Calvario, Santa Elena',
                    cantidad_productos: 1,
                    total: 5.50,
                },
            ],
            pedidosFiltrados: [
                {
                    id: 1,
                    fecha: '2024-11-11 11:11:11',
                    nombre_cliente: 'Juan Perez',
                    tipo: 'Domicilio',
                    direccion: '8va Calle poniente, Barrio La Parroquia, Santa Elena',
                    cantidad_productos: 2,
                    total: 12.50,
                },
                {
                    id: 2,
                    fecha: '2024-11-11 12:44:11',
                    nombre_cliente: 'Maria Lopez',
                    tipo: 'Local',
                    direccion: '4ta Avenida Sur, Barrio El Calvario, Santa Elena',
                    cantidad_productos: 1,
                    total: 5.50,
                },
            ],
        };
    },
}
</script>