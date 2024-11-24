<template>
    <div>
        
    </div>
</template>

<style scoped>

</style>

<script>
// importaciones de componentes

// fin de importaciones de componentes

export default {
    name: 'PaginaVentas',
    data() {
        return {
            ventas:{
                //Datos de ejemplo
                domicilio: 20,
                local: 10,
                ventas_por_producto: [
                    {
                        nombre_producto: 'Producto 1',
                        cantidad_vendida: 10,
                        ganancias: 55.5
                    },
                    {
                        nombre_producto: 'Producto 2',
                        cantidad_vendida: 5,
                        ganancias: 25.5
                    },
                    {
                        nombre_producto: 'Producto 3',
                        cantidad_vendida: 15,
                        ganancias: 75.5
                    }
                ],
                total_ventas:{
                    cantidad_vendida: 30,
                    ganancias: 156.5
                }
            },
            periodoCalculado: 'ultimo mes'
        }
    },
    methods: {

    },
    mounted() {

    },
    watch: {

    }
}


</script>