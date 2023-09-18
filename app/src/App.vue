<script setup lang="ts">
  import { IonApp, IonRouterOutlet } from '@ionic/vue'
  import Menu from "@/components/MenuComponent.vue";
</script>

<template>
  <ion-app>
    <Menu />
    <ion-router-outlet id="main-content" />
  </ion-app>
</template>

<style scoped lang="scss">
.ios {
  #main-content {
    top: 100px;
  }
}

#main-content {
  top: 70px;
  display: flex;
  margin: 0px 5%;
}
</style>
