<template>
   <div class="menu-categories">
    <div class="category" v-for="category in categories" :key="category.name">
      <img :src="category.image" alt="category.name" class="category-image" />
      <h3>{{ category.name }}</h3>
    </div>
  </div>
</template>

<style scoped>
<script>
export default {
  data() {
    return {
      categories: [
        {
          name: 'Burgers',
          image: 'ruta/a/tu/imagen/burgers.png' 
        },
        {
          name: 'Snacks',
          image: 'ruta/a/tu/imagen/snacks.png' 
        },
        {
          name: 'Bebidas',
          image: 'ruta/a/tu/imagen/bebidas.png' 
        },
        {
          name: 'Combos',
          image: 'ruta/a/tu/imagen/combos.png' 
        },
        {
          name: 'Promociones',
          image: 'ruta/a/tu/imagen/promociones.png' 
        }
      ]
    };
  }
};
</script>

<style>
.menu-categories {
  display: flex;
  justify-content: space-around;
  margin: 20px;
}

.category {
  text-align: center;
}

.category-image {
  width: 100px; 
  height: auto;
}
</style>


<script>
export default {
    name: 'CategoriaComp',
    data() {
        return {
            
        }
    },
    props: {
        
    },
    methods: {
        
    },
    computed: {
        
    },

}

</script>