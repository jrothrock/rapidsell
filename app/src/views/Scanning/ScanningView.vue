<script setup lang="ts">
import { ref } from 'vue';
import { IonPage, onIonViewWillEnter, onIonViewWillLeave, IonContent, IonItem, IonLabel } from '@ionic/vue';
import { useScanning } from "./useScanning";
import type { Scan } from "@/api/scanning/Scan";

const scans = ref<Scan[]>([]);

const { listScans } = useScanning();

const loading = ref<boolean>(false);

onIonViewWillEnter(() => {
  loading.value = true;
  listScans(scans);
  loading.value = false;
});

// We need to keep clear the values manually, as the component/page never truly leaves.
// https://ionicframework.com/docs/vue/lifecycle#how-ionic-framework-handles-the-life-of-a-page
onIonViewWillLeave(() => {
  scans.value = [];
});
</script>

<template>
  <ion-page>
    <ion-content>
      <ion-item class="scan-items">
        <ion-label class="image-container">
          Image
        </ion-label>
        <ion-label class="title-container">
          Title
        </ion-label>
      </ion-item>
      <ion-item
        v-for="scan in scans"
        :key="scan.serp_found_title"
        class="scan-items"
      >
        <img
          class="image-container"
          :src="scan.image_url"
        >
        <ion-label class="title-container">
          {{ scan.serp_found_title }}
        </ion-label>
      </ion-item>
    </ion-content>
  </ion-page>
</template>

<style scoped lang="scss">
.scan-items {
  text-align: center;
  .image-container {
    max-height: 300px;
    max-width: 150px;
    padding: 10px;
  }
}
</style>
