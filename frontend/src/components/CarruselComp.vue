<template>
<div class="carousel">
        <div class="carousel-slides" >
        <button class="prev" @click="prevSlide">←</button>
        <div class="slide">
            <a :href="anuncios[currentSlide].url_redireccion">
                <img class="img-anuncio" :src="anuncios[currentSlide].url_foto" alt="Anuncio">
            </a>
        </div>
        <button class="next" @click="nextSlide">→</button>
    </div>
</div>
</template>

<style scoped>
.carousel {
  width: 100%;
  height: 400px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border: 1px solid #ffad00;
}
.carousel-slides {
    width: 80%;
    height: 100%;
  display: flex;
  transition: fade 0.5s;
}
.slide, .img-anuncio,a{
  min-width: 100%;
  height: 100%;
}
.prev,
.next {
    width: 10%;
    height: 100%;
  background: #ffad00;
  color: black;
  border: none;
  cursor: pointer;
  padding: 10px;
  border: 1px solid #ffad00;
}


</style>
<script>
export default {
    
    name: 'CarruselComp',
    data (){
        return{
        currentSlide: 1,
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
        };
    },
    methods: {
    nextSlide() {
      this.currentSlide = (this.currentSlide + 1) % this.anuncios.length;
    },
    prevSlide() {
      this.currentSlide = (this.currentSlide - 1 + this.anuncios.length) % this.anuncios.length;
    },
    },
    mounted() {
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