<template>
<div class="carousel-container" @mouseover="limpiarIntervalo(slideInterval)" @mouseout="slideInterval = setearIntervalo(nextSlide, 5000)">
        <div class="carousel">
            <div class="carousel-item" v-for="(anuncio) in anuncios" :key="anuncio.id">
                <a :href="anuncio.url_redireccion">
                    <img :src="anuncio.url_foto" :alt="'Promo' ">
                </a>
            </div>
        </div>

        <div class="controls">
            <button id="prevBtn" @click="prevSlide">❮</button>
            <button id="nextBtn" @click="nextSlide">❯</button>
        </div>

        <div class="indicators">
            <span v-for="(anuncio) in anuncios" :key="anuncio.id" :class="['dot', { active: currentIndex === anuncio.id }]" @click="showSlide(anuncio.id)"></span>
        </div>
    </div>
</template>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}


.carousel-container {
    position: relative;
    width: 70%;
    max-width: 900px;
    max-height: 400px;
    overflow: hidden;
    margin: auto;
    border-radius: 10px;
}

.carousel {
    display: flex;
    transition: transform 0.5s ease-in-out;
}

.carousel-item {
    width: 100%;
    flex: 1 0 100%;
}

.carousel img {
    width: 100%;
    height: auto;
    border-radius: 10px;
}

.controls {
    position: absolute;
    top: 44%;
    width: 100%;
    display: flex;
    justify-content: space-between;
    transform: translateY(-50%);
    padding: 0 20px;
}

.controls button {
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
    font-size: 18px;
    border-radius: 50%;
}

.indicators {
    text-align: center;
    margin-top: 10px;
}

.dot {
    height: 12px;
    width: 12px;
    margin: 0 5px;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 50%;
    display: inline-block;
    cursor: pointer;
}

.dot.active {
    background-color: #ffad00;
}
</style>

<script>
export default {
    
    name: 'CarruselComp',
    data (){
        return{
        anuncios: [
            {
                id: 1,
                url_foto: "https://proyectodb.blob.core.windows.net/imgs/Burger_cheesebacon.jpeg",
                url_redireccion: "/menu?categoria=Burgers"
            },
            {
                id: 2,
                url_foto: "https://proyectodb.blob.core.windows.net/imgs/Limonada_fresa.jpeg",
                url_redireccion: "/menu?categoria=Bebidas"
            },
            {
                id: 3,
                url_foto: "https://proyectodb.blob.core.windows.net/imgs/Combo_estudiante.jpeg",
                url_redireccion: "/menu?categoria=Combos"
            },
            {
                id: 4,
                url_foto: "https://proyectodb.blob.core.windows.net/imgs/Nachos.jpeg",
                url_redireccion: "/menu?categoria=Snacks"
            }
        ],
        currentIndex: 0,
        dots: document.querySelectorAll('.dot'),
        slides: document.querySelectorAll('.carousel-item'),
        slideInterval: null,
        };
    },
    methods: {
        showSlide(index) {
            this.currentIndex = index;
        },
        nextSlide(){
            this.currentIndex = (this.currentIndex + 1) % this.slides.length;
            this.showSlide(this.currentIndex);
        },
        prevSlide() {
            this.currentIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length;
            this.showSlide(this.currentIndex);
        },
        limpiarIntervalo(intervalo) {
            clearInterval(intervalo);
        },
        setearIntervalo(funcion, tiempo) {
            return setInterval(funcion, tiempo);
        }
    },
    mounted() {
        this.slideInterval = setInterval(this.nextSlide, 5000); 
    },
};


/*
let currentIndex = 0;
const slides = document.querySelectorAll('.carousel-item');
const dots = document.querySelectorAll('.dot');

function showSlide(index) {
    currentIndex = index;
    const totalSlides = slides.length;
    const offset = -100 * index;
    document.querySelector('.carousel').style.transform = `translateX(${offset}%)`;

    dots.forEach(dot => dot.classList.remove('active'));
    dots[index].classList.add('active');
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    showSlide(currentIndex);
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    showSlide(currentIndex);
}

document.getElementById('nextBtn').addEventListener('click', nextSlide);
document.getElementById('prevBtn').addEventListener('click', prevSlide);

dots.forEach((dot, index) => {
    dot.addEventListener('click', () => showSlide(index));
});

let slideInterval = setInterval(nextSlide, 5000); 

document.querySelector('.carousel-container').addEventListener('mouseover', () => {
    clearInterval(slideInterval); 
});

document.querySelector('.carousel-container').addEventListener('mouseout', () => {
    slideInterval = setInterval(nextSlide, 5000); 
});

window.onload = () => {
    showSlide(0);
};
*/

</script>