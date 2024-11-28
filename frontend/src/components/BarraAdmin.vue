<template>
    <div class="sidebar">
      <ul>
        <li>
          <a href="#">
            <i class="bi bi-cash-stack icon"></i>
            Ventas
          </a>
        </li>
        <li>
          <a href="#" class="active">
            <i class="bi bi-people icon"></i>
            Usuarios
          </a>
        </li>
        <li>
          <a href="#">
            <i class="bi bi-tag icon"></i>
            Descuentos
          </a>
        </li>
        <li>
          <a href="#">
            <i class="bi bi-shop icon"></i>
            Ingredientes
          </a>
        </li>
      </ul>
    </div>
  </template>
  
  <style scoped>
  .sidebar {
    width: 200px;
    background-color: #000;
    color: #fff;
    height: 100vh;
    padding: 20px 0;
    font-family: Arial, sans-serif;
  }
  
  .sidebar ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .sidebar li {
    margin: 15px 0;
  }
  
  .sidebar a {
    text-decoration: none;
    color: #fff;
    display: flex;
    align-items: center;
    padding: 10px 20px;
    border-left: 4px solid transparent;
    transition: all 0.3s ease;
  }
  
  .sidebar a:hover {
    background-color: rgba(255, 255, 255, 0.1);
    border-left: 4px solid #ffad00;
  }
  
  .sidebar a.active {
    background-color: rgba(255, 255, 255, 0.1);
    border-left: 4px solid #ffad00;
  }
  
  .icon {
    margin-right: 10px;
    font-size: 20px;
    color: #ffad00;
  }
  </style>
  
  <script>
  export default {
    name: "Sidebar",
  };
  </script>

<script>
export default {
    name: 'BarraAdmin',
    data() {
        return{

        }
    },
    methods: {
        
    },
}

</script>