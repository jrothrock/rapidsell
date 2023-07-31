<script setup lang="ts">
  import { IonApp, IonRouterOutlet } from '@ionic/vue'
  import Menu from "./components/Menu.vue";
</script>

<template>
  <ion-app>
    <Menu></Menu>
    <ion-router-outlet id="main-content" />
  </ion-app>
</template>

<style scoped>
#main-content {
  top: 70px;
  display: flex;
  margin: 0px 5%;
}
</style>
