<script setup lang="ts">
import { ref, computed } from 'vue';
import { IonPage, onIonViewWillEnter, onIonViewWillLeave, IonContent, IonItem, IonLabel } from '@ionic/vue';
import { useScanning } from "./useScanning";
import { DateTime } from 'luxon';
import type { ParsedScan } from "./types";

const yesterday = DateTime.now().minus({ days: 1 })

const scans = ref<ParsedScan[]>([]);
const recentScans = computed(() => {
  if(scans.value.length > 0) {
    return scans.value.filter((scan: ParsedScan) => DateTime.fromFormat(scan.scannedDate, 'yyyy-MM-dd HH:mm:ss z') > yesterday);
  } else {
    return []
  }
})

const olderScans = computed(() => {
  if(scans.value.length > 0) {
    return scans.value.filter((scan: ParsedScan) => DateTime.fromFormat(scan.scannedDate, 'yyyy-MM-dd HH:mm:ss z') < yesterday);
  } else {
    return []
  }
})

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
  <!-- TODO: Clean this up a bit. -->
  <ion-page>
    <ion-content>
      <h2 class="post-type-header">Recent</h2>
      <ion-item class="scan-items">
        <ion-label class="image-container">
          Image
        </ion-label>
        <ion-label class="scanned-at-container">
          Scanned At
        </ion-label>
        <ion-label class="found-image-container">
          Found Image
        </ion-label>
        <ion-label class="title-container">
          Title
        </ion-label>
        <ion-label class="price-container">
          Average Price
        </ion-label>
      </ion-item>
      <ion-item
        v-for="scan in recentScans"
        :key="scan.serpFoundTitle"
        class="scan-items"
      >
        <img
          class="image-container"
          :src="scan.imageUrl"
        >
        <ion-label class="scanned-at-container">
          {{ scan.scannedDate }}
        </ion-label>
        <!--Is it possible to have no visual matches?-->
        <img
          class="found-image-container"
          :src="scan.visualMatches[0].thumbnail"
        >
        <ion-label class="title-container">
          {{ scan.serpFoundTitle }}
        </ion-label>
        <ion-label class="price-container">
          {{ scan.serpFoundPrice }}
        </ion-label>
      </ion-item>
      <div v-if="olderScans.length">
        <h2 class="post-type-header">Older</h2>
        <ion-item class="scan-items">
          <ion-label class="image-container">
            Image
          </ion-label>
          <ion-label class="title-container">
            Title
          </ion-label>
          <ion-label class="price-container">
            price
          </ion-label>
        </ion-item>
        <ion-item
          v-for="scan in olderScans"
          :key="scan.serpFoundTitle"
          class="scan-items"
        >
          <img
            class="image-container"
            :src="scan.imageUrl"
          >
          <ion-label class="title-container">
            {{ scan.serpFoundPrice }}
          </ion-label>
          <ion-label class="title-container">
            {{ scan.serpFoundPrice }}
          </ion-label>
        </ion-item>
      </div>
    </ion-content>
  </ion-page>
</template>

<style scoped lang="scss">
.post-type-header {
  text-align: left;
}

.scan-items {
  text-align: center;
  .image-container, .found-image-container {
    max-height: 300px;
    max-width: 150px;
    padding: 10px;
  }

  .found-image-container {
    border-left: 2px solid grey;
  }
}
</style>
