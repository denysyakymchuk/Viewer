<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <div>
      <model-viewer  :src="this.MAIN_MODEL"
                     :skybox-image="this.MAIN_SKY_BOX_IMAGE"
                     :environment-image="this.MAIN_ENV_IMAGE"
                     :shadow-intensity="this.shadowIntensity"
                     :shadow-softness="this.shadowSoftness"
                     camera-controls
                     touch-action="pan-y">

        <effect-composer render-mode="quality" msaa="8">

          <!--   ВСЕ ДЕЛАЕТ ПИКСЕЛЯМИ   -->
          <pixelate-effect v-if="pixar"></pixelate-effect>

          <!--   OPACITY     -->
          <color-grade-effect :contrast="this.contrast" saturation="-1" :opacity="this.opacity" :blend-mode="this.blendMode" :brightness="this.brightness"></color-grade-effect>

        </effect-composer>

      </model-viewer>
    </div>

    <!--  BOCZNA PANEL   -->
    <div>
      <div class="btn"
      >
        <v-menu
            v-model="menu"
            :close-on-content-click="false"
            location="center"
            max-width="350"
        >
          <template v-slot:activator="{ props }">
            <v-btn
                color="indigo"
                v-bind="props"
            >
              Filters
            </v-btn>
          </template>

          <v-card
              min-width="300"
              color="black"
              style="border-radius: 20px"
          >
            <v-row>
              <v-col cols="12">
                <v-checkbox label="Pixelem" v-model="this.pixar"></v-checkbox>
              </v-col>

              <v-col cols="12">
                <v-slider
                    class="wd-all"
                    v-model="this.brightness"
                    label="Brightness"
                    color="orange"
                    min="-1"
                    max="1"
                    step="0.01"
                    thumb-label="true"></v-slider>
              </v-col>

              <v-col cols="12">
                <v-slider
                    class="wd-all"
                    v-model="this.opacity"
                    label="Opacity"
                    color="orange"
                    min="0"
                    max="1"
                    step="0.01"
                    thumb-label="true"></v-slider>
              </v-col>

              <v-col cols="12">
                <v-slider
                    class="wd-all"
                    v-model="this.contrast"
                    label="Contrast"
                    color="orange"
                    min="0"
                    max="1"
                    step="0.01"
                    thumb-label="true"></v-slider>
              </v-col>

              <v-col cols="12">
                <v-slider
                    v-model="this.shadowSoftness"
                    class="wd-all"
                    label="Shadow softness"
                    color="orange"
                    min="0"
                    max="1"
                    step="0.01"
                    thumb-label="true"></v-slider>
              </v-col>

              <v-col cols="12">
                <v-slider
                    class="wd-all"
                    v-model="this.shadowIntensity"
                    label="Shadow intensity"
                    min="0"
                    max="4"
                    step="0.01"
                    color="orange"
                    thumb-label="true"></v-slider>
              </v-col>

              <v-col cols="12">
                <v-select
                    v-model="this.blendMode"
                    :items="['Default', 'Skip', 'Add', 'Subtract', 'Divide', 'Negation']"
                    variant="primary"
                ></v-select>
              </v-col>

            </v-row>
          </v-card>
        </v-menu>
      </div>
    </div>
    <!--  BOCZNA PANEL   -->
  </div>
</template>

<script>
import '@google/model-viewer'
import '@google/model-viewer-effects'
import { mapActions, mapGetters } from "vuex";


export default {
  name: "MainView",
  data() {
    return {
      pixar: false,
      opacity: 1,
      shadowIntensity: 0,
      shadowSoftness: 0,
      brightness: 0,
      contrast: 0,
      blendMode: 'skip',
      fav: true,
      menu: false,
      message: false,
      hints: true,
    }
  },
  methods: {
    ...mapActions(["GET_MAIN_MODEL"]),
  },
  computed: {
    ...mapGetters(["MAIN_MODEL", "MAIN_SKY_BOX_IMAGE", "MAIN_ENV_IMAGE"]),
  },
}
</script>

<style scoped>

.btn {
  margin-top: 1%;
  margin-right: 2%;
  position: absolute;
  z-index: 1000;
  top: 0;
  right: 0;
}
model-viewer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  aspect-ratio: 16/9;
  border-radius: 0; /* убрать скругление углов, если не нужно */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* тень, если нужно */
  z-index: 0; /* установить необходимый z-index */
}

.wd-all {
  width: 270px;
}

.v-row {
  display: flex;
  flex-wrap: wrap;
  flex: 1 1 auto;
  margin: 0;
}

</style>