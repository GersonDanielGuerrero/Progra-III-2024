<template>
    <div id="carrusel" class="carrusel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
        <button 
            type="button"
            v-for="(item, index) in intems" 
            :key="index" 
            :data-bs-target="'#carouselIndicators'"
            :data-bs-slide-to="ïndex"
            :class="{ active: index === 0 }"
            aria-current="index === 0 ? 'true' : 'false'"
            :aria-label="`Slide ${index + 1}`">
        </button>
        </div>
        <div class="carousel-inner">
            <div v-for="(item, index) in items" :key="index" :class="['carousel-item', { active: index === 0}]">
                <a :href="item.url_redireccion">
                    <img :src="item.url_foto" class="d-block w-100" alt="Anuncio" />
                </a>
            </div>

        <button 
            class="carousel-control-prev" 
            type="button"
            data-bs-target="#carruselIndicators"
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
            data-bs-target="#carruselIndicators"
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
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 50%;
}

.carousel-indicators button {
    background-color: #FFAD00;
}

</style>

<script>
export default {
    
}
</script>