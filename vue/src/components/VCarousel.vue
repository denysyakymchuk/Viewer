<template>
  <div class="pos">
    <carousel :items-to-show="6">

      <slide v-for="slide in MODELS" :key="slide.path" class="slide">
        <model-viewer class="ww"
                      @click="setMainModel(slide.path, slide.path_skybox_image, slide.path_env_image);"
                      :src="slide.path">

        </model-viewer>
      </slide>

      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
  </div>
</template>

<script>
import '@google/model-viewer'
import 'vue3-carousel/dist/carousel.css';
import {mapActions, mapGetters} from "vuex";


import {Carousel, Slide, Pagination, Navigation} from 'vue3-carousel';

export default {
  name: 'VCarousel',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  data() {
    return {
      baseModel: {

      },
    };
  },
  methods: {
    setMainModel(path, skyBoxImage, envImage) {
      this.GET_MAIN_MODEL({path, skyBoxImage, envImage})
    },
    ...mapActions(["GET_MODELS", "GET_MAIN_MODEL"]),
  },
  computed: {
    ...mapGetters(["MODELS"]),
  },
  async mounted() {

    await this.GET_MODELS()

    const baseModel = {
      path: this.MODELS[0].path,
      skyBoxImage: this.MODELS[0].path_skybox_image,
      envImage: this.MODELS[0].path_env_image
    }
    await this.GET_MAIN_MODEL(baseModel)
  }
}
</script>

<style scoped>
@media only screen and (max-width: 672px) {
  .ww {
    height: 150px;
  }
}

model-viewer {
  width: 100%;
  height: 100%;
}

.slide {
  height: 150px;
  width: 150px;
  margin: 1%;
}

.pos {
  width: 100%;
  max-width: 1400px;
  margin: auto;
  position: fixed;
  bottom: 5%;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
}
</style>
