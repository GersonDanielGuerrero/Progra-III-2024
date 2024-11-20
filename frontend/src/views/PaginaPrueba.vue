<template>
    <div class = "container">
        <div class="row">
            <div class ="comp1 col-md-4" v-if="comp1permitido && (pantallaGrande || componenteMostrado==1)">
                <BotonComp class ="cliente" v-for="i in 40" :key="i"> Cliente Numero {{ i }}</BotonComp>
            </div>
            <div class = "comp2 col-md-8 col-lg-8 col-sm-12" v-if ="componenteMostrado==2 || pantallaGrande">

            </div>
        </div>
        <BotonComp v-if="comp1permitido && !pantallaGrande" @click="cambiarComponente">{{ componenteMostrado }}</BotonComp>
    </div>
</template>

<style>
.row{
height: 60vh;
margin: auto;
margin-top: 80px;
}
.comp1{
    height: 100%;
    border: 4px solid #ffad00;
    color: #ffad00;
    font-family: 'Arial-Black';
    padding: 20px;
    overflow-y: auto;
    scrollbar-color: #ffad00 #444 ;
    font-size: 12px;
}
.comp2{
    height: 100%;
    border: 4px solid purple;
}
.cliente{
    margin: 10px;
}
.cliente :hover {
    font-size: 14px;
}
</style>

<script>
import BotonComp from '@/components/BotonComp.vue';

export default {
    components:{
        BotonComp,
    },
    name: 'PaginaPrueba',
    data() {
        return {
            comp1permitido:true,
            componenteMostrado:2,
        }
    },
    computed:{
        pantallaGrande(){
            return window.innerWidth >= 768;
        }
    },
    methods: {
        cambiarComponente(){
            if (this.componenteMostrado==1){
                this.componenteMostrado=2;
            }
            else{
                this.componenteMostrado=1;
            }
        }
    },
}
</script>