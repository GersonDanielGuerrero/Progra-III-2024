<template>
    <div class="map-container">
      <l-map
        :zoom="zoom"
        :center="centro"
        style="height: 400px; width: 100%;"
        @click="clickMapa"
      >
        <l-tile-layer
          :url="tileLayerUrl"
          :attribution="attribution"
        ></l-tile-layer>
        <l-marker
          v-if="posicionMarca"
          :lat-lng="posicionMarca"
          :draggable="true"
          @moveend="marcaMovida"
        ></l-marker>
      </l-map>
      <div class="coordinates">
        <p>Dirección seleccionada: {{ direccion_marca }}</p>
        <p>Coordenadas: Latitud {{ posicionMarca?.lat }}, Longitud {{ posicionMarca?.lng }}</p>
      </div>
    </div>
  </template>

<style>
.map-container {
  width: 70vw;
  height: 70vh;
  margin: 10vh auto;
}
.coordinates {
  margin-top: 10px;
}
</style>


  
  <script>
  import { LMap, LTileLayer, LMarker } from "vue3-leaflet";
  import "leaflet/dist/leaflet.css";
  
  export default {
    name: "PaginaDireccion",
    components: {
      LMap,
      LTileLayer,
      LMarker,
    },
    data() {
      return {
        zoom: 19,
        centro: [13.346994, -88.437800], // Coordenadas iniciales, Good Burger
        posicionMarca: null, // Posición del marcador
        tileLayerUrl: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        direccion_marca: "",
      };
    },
    methods: {
      async clickMapa(event) {
        this.posicionMarca = event.latlng;
        await this.obtenerDireccionMarcada(event.latlng.lat, event.latlng.lng);
      },
      async marcaMovida(event) {
        this.posicionMarca = event.target.getLatLng();
        await this.obtenerDireccionMarcada(this.posicionMarca.lat, this.posicionMarca.lng);
      },
      async obtenerDireccionMarcada(lat, lng) {
        // Esto obtiene el nombre de la direccion en base a las coordenadas
        try {
          // Usa el servicio de geocodificación inversa de OpenStreetMap para obtener la dirección
          const response = await fetch(`https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lng}&format=json`);
          const data = await response.json();
          this.direccion_marca = data.display_name || "Dirección no disponible";
        } catch (error) {
          console.error("Error al obtener la dirección:", error);
        }
      },
    },
  };
  </script>
  
 