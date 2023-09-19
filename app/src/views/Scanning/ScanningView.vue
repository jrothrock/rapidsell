<script setup lang="ts">
import { ref } from 'vue';
import { CameraIcon } from '@heroicons/vue/24/solid';
import { IonPage, onIonViewWillLeave, IonContent, IonFab, IonFabButton, IonLabel, IonSpinner, IonGrid, IonRow, IonCol, IonImg, IonButton } from '@ionic/vue';
import { useScanning } from "./useScanning";
import type { UserPhoto } from "./useScanning";

const photo = ref<UserPhoto>();

const loading = ref<boolean>(false);

const handleUpload = async () => {
  loading.value = true;
  await uploadPhoto();
  loading.value = false;
};


// We need to keep clear the values manually, as the component/page never truly leaves.
// https://ionicframework.com/docs/vue/lifecycle#how-ionic-framework-handles-the-life-of-a-page
onIonViewWillLeave(() => {
  photo.value = undefined;
})

const { takePhoto, uploadPhoto } = useScanning(photo);
</script>

<template>
  <ion-page>
    <ion-content>
      <ion-grid>
        <ion-row>
          <ion-col
            v-if="photo"
          >
            <ion-img
              class="display-image"
              :src="photo.dataUrl"
            />
          </ion-col>
        </ion-row>
      </ion-grid>

      <ion-button
        v-if="photo"
        :disabled="loading"
        @click="handleUpload()"
      >
        <ion-label class="photo-upload-label">
          Upload Photo
          <ion-spinner
            v-if="loading"
            class="spinner"
          /> 
        </ion-label>
      </ion-button>

      <ion-fab
        vertical="bottom"
        horizontal="center"
      >
        <ion-fab-button @click="takePhoto()">
          <camera-icon class="icon" />
        </ion-fab-button>
      </ion-fab>
    </ion-content>
  </ion-page>
</template>

<style scoped lang="scss">
.icon {
  height: 70%
}

.photo-upload-label {
  display: flex;
  align-items: center;

  .spinner {
    height: 20px;
    width: 20px;
    margin: 0px 5px;
  }
}

.display-image {
  height: 300px;
}
</style>
