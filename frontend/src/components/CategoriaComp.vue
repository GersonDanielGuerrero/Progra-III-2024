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
  text-align: center;
}

.category-image {
  width: 100px; 
  height: auto;
}
</style>