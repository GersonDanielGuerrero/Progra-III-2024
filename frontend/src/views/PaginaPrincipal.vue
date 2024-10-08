<template>
    <div>
      
    </div>
</template>
 
<style scoped>
   /* Estilos generales */
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background-color: #000;
    color: #ffffff;
}
/* Header */
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background-color: #000;
    border-bottom: 2px solid #fdfdfd46;
}
nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
}

nav ul li a {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
}

.user-actions {
    display: flex;
    gap: 10px;
}

.login-btn {
    background-color: #f6a901;
    color: #000;
    border: none;
    padding: 8px 20px;
    cursor: pointer;
    font-weight: bold;
}
.cart-btn {
    background-color: #000000;
    color: #000;
    border: none;
    padding: 8px 10px;
    cursor: pointer;
    font-weight: bold;
}
.search-btn {
    background-color: #000000;
    color: #000;
    border: none;
    padding: 8px 10px;
    cursor: pointer;
    font-weight: bold;
}

/* Promo */
.promo {
    background-color: #000000f5;
    padding: 40px 20px;
    text-align: center;
}

.promo h2 {
    color: #ffae00;
    font-size: 36px;
    margin-bottom: 10px;
}

.promo p {
    font-size: 24px;
    margin-bottom: 20px;
}

.order-btn {
    background-color: #ffae00;
    color: #000;
    border: none;
    padding: 15px 30px;
    font-size: 18px;
    cursor: pointer;
}

/* Menu */
.menu {
    padding: 20px;
    text-align: center;
}
.menu-title {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    position: relative;
}

.menu-title h2 {
    font-size: 28px;
    color: #fff;
    margin: 0 20px;
}
.menu-title.line {
    content: "";
    height: 20px;
    background-color: #ffae00;
    flex: 1;
}
.menu-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 20px;
}

.menu-item {
    background-color: #2f2e2e;
    padding: 20px;
    text-align: center;
    border-radius: 10px;
}

.menu-item img {
    width: 100px;
    height: 100px;
    object-fit: cover;
    margin-bottom: 10px;
}

.menu-item p {
    color: #fefefe;
    font-size: 18px;
    font-weight: bold;
}
img {
    max-width: 150px;
    padding: both;
    max-height: 290px;
    object-fit: border-box;
    width: default;
    height: default;   
}
</style>

<!-- C U I D A D I T O -->

<script>

export default {
    name: 'PaginaPrincipal',
    components: {
    },
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