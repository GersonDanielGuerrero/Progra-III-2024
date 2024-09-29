<template>
    <div class="input-group">
    <input 
        v-bind="$attrs"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
    />
    <img class="icono" :src="icono" v-if="icono">
    </div>
</template>

<style scoped>
*{
    font-family: "Arial Black", Gadget, sans-serif;
}
.input-group {
position: relative;
margin-bottom: 15px;
width: 100%;
}

.input-group input {
width: 100%;
padding: 10px;
padding-right: 40px;
background-color: rgba(255, 255, 255, 0.3);
border-radius: 5px;
border: none;
color: #000;
}

.input-group input::placeholder {
color: #ffad00;
}

.icono {
height: 30px;
width: 30px;
position: absolute;
right: 10px;
top: 50%;
transform: translateY(-50%);
color: #ffad00;
}

</style>

<!-- C U I D A D I T O -->

<script>
export default {
    name: 'CajaTexto',
    data() {
        return {
        }
    },
    props: {
        modelValue: {
            type: String,
            default: ''
        },
        icono: {
            type: String,
            Required: false
        }
    },
    methods: {
        
    },
    computed: {
        
    },

}
</script>