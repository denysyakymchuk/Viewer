<template>
  <div>
    <component :is="layout">
      <router-view />
    </component>
  </div>
</template>

<script>
import AdminLayout from "@/layout/AdminLayout.vue";
import MainLayout from "@/layout/MainLayout.vue";

export default {
  name: 'App',
  computed: {
    layout() {
      return this.$route.meta.layout === 'admin' ? AdminLayout : MainLayout;
    },
    components: {
      AdminLayout,
      MainLayout,
    }
  }
}
</script>

<style>
body {
  background-image: url("./assets/background2.webp");
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
