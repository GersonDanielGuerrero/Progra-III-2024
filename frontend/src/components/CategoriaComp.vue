<template>
    <div class="category">
      <img :src="categoria.imagen" :alt="categoria.nombre" class="category-image" />
      <h3>{{ categoria.nombre }}</h3>
    </div>
</template>

<script>

export default {
  name: 'CategoriaComp',
  data() {
    return {

    };
  },
  props: {
     categoria: {
      type: Object,
      required: true
    }
  },
};
</script>

<style scoped>

.category {
  position: relative;
  border-radius: 10px;
  text-align: center;
  color: white;
  
}

.category h3 {
  position: absolute;
  top: 55px;
  left: 50%;
  transform: translate(-50%, -299%);
}

.category-image {
  width: 50px; 
  height: 50px;
  object-fit: cover;   
  border-radius: 500px;
  margin-bottom: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  width: 149px;
  height: auto;
}
</style>