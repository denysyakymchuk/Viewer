<template>
  <div>
    <!--  LEFT PANEL  -->
    <div class="openLeft" @animationend="onAnimationEnd('left')">
      <img src="../assets/panel-left.png" class="panelImage">
    </div>

    <!--  RIGHT PANEL  -->
    <div class="openRight" @animationend="onAnimationEnd('right')">
      <img src="../assets/panel-right.png" class="panelImageR">
    </div>

    <!--  COMPONENTS  -->
    <div>
      <MainView v-if="allAnimationsDone" />
      <VCarousel v-if="allAnimationsDone" />
    </div>

    <!--  BOTTOM PANEL  -->
    <div class="openBottom" @animationend="onAnimationEnd('bottom')">
      <img src="../assets/panel-bottom.png">
    </div>
  </div>
</template>

<script>
import VCarousel from '../components/VCarousel.vue';
import MainView from "@/components/MainView.vue";

export default {
  name: 'App',
  components: {
    VCarousel,
    MainView
  },
  data() {
    return {
      animationLeftDone: false,
      animationRightDone: false,
      animationBottomDone: false,
    };
  },
  computed: {
    allAnimationsDone() {
      return this.animationLeftDone && this.animationRightDone && this.animationBottomDone;
    }
  },
  methods: {
    onAnimationEnd(position) {
      if (position === 'left') {
        this.animationLeftDone = true;
      } else if (position === 'right') {
        this.animationRightDone = true;
      } else if (position === 'bottom') {
        this.animationBottomDone = true;
      }
    }
  }
}
</script>

<style>
img {
  width: 100%;
}

MainView {
  width: 100%;
  height: 100%;
}

/* Animowana lewa panel */
.openLeft {
  top: 0;
  left: -200px;
  position: fixed;
  z-index: 110;
  animation: slideLeft 2s ease-in-out forwards;
}

@keyframes slideLeft {
  from {
    left: -200px;
  }
  to {
    left: 0px;
  }
}

/* Animowana prawa panel */
.openRight {
  top: 0;
  right: -200px;
  position: fixed;
  z-index: 110;
  animation: slideRight 2s ease-in-out forwards;
}

@keyframes slideRight {
  from {
    right: -200px;
  }
  to {
    right: 0px;
  }
}

/* Animowana dolna panel */
.openBottom {
  left: 0;
  bottom: -200px;
  position: fixed;
  animation: slideUp 2s ease-in-out forwards;
}

@keyframes slideUp {
  from {
    bottom: -200px;
  }
  to {
    bottom: -10px;
  }
}

/* Media query for screens with a minimum width of 672px */
@media only screen and (max-width: 672px) {
  .panelImage {
    width: 80px;
    height: 900px;
  }
  .panelImageR {
    width: 60px;
    height: 950px;
  }


}
</style>
