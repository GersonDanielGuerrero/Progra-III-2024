<template>
    <div id="carrusel" class="carrusel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
        <button 
            type="button"
            :data-bs-target="'#carousel'"
            :data-bs-slide-to="0"
            :class="active"
            aria-current="true"
            aria-label="Slide 1">
        </button>
        <button
            type="button"
            :data-bs-target="'#carousel'"
            :data-bs-slide-to="1"
            aria-label="Slide 2">
        </button>
        <button
            type="button"
            :data-bs-target="'#carousel'"
            :data-bs-slide-to="2"
            aria-label="Slide 3">
        </button>
        </div>
        <div class="carousel-inner">
            <div class="carousel-item active">
                <a :href="item.url_redireccion">
                    <img src="" class="d-block w-100" alt="Promocion 1">
                </a>
            </div>
        <div class="carousel-inner">
                <a :href="item.url_redireccion">
                    <img src="" class="d-block w-100" alt="Promocion 2">
                </a>
        </div>
        <div class="carousel-inner">
                <a :href="item.url_redireccion">
                    <img src="" class="d-block w-100" alt="Promocion 3">
                </a>
        </div>
        <button 
            class="carousel-control-prev" 
            type="button"
            data-bs-target="#carrusel"
            data-bs-slide="prev">
        <span
            class="carousel-control-prev-icon"
            aria-hidden="true">
        </span>
        <span
            class="visually-hidden">Anterior
        </span>
        </button>

        <button 
            class="carousel-control-next" 
            type="button"
            data-bs-target="#carrusel"
            data-bs-slide="next">
        <span
            class="carousel-control-next-icon"
            aria-hidden="true">
        </span>
        <span
            class="visually-hidden">Siguiente
        </span>
        </button>

        </div>
        
    </div>
</template>

<style>
.carousel-item img {
    height: 400px;
    object-fit: cover;
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
    background-color: rgba(255, 173, 0, 0.8);
    border-radius: 50%;
    width: 40px;
    height: 40px;
}

.carousel-indicators button {
    background-color: #FFAD00;
    width: 12px;
    height: 12px;
    border-radius: 50%;
}

.carousel-indicators .active {
    background-color: white;
}

</style>

<script>
export default {
    name: 'CarruselComp',
    data (){
        
    }
}
</script>