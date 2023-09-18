<script setup lang="ts">
import { ref } from 'vue';
import { CameraIcon } from '@heroicons/vue/24/solid';
import { IonPage, IonContent, IonFab, IonFabButton, IonLabel, IonSpinner, IonGrid, IonRow, IonCol, IonImg, IonButton } from '@ionic/vue';
import { useScanning } from "./useScanning";
import type { UserPhoto } from "./useScanning";

const photo = ref<UserPhoto>();

const loading = ref<boolean>(false);

const handleUpload = async () => {
  loading.value = true;
  await uploadPhoto()
  loading.value = false;
};

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
@media(min-width:640px){
  .sign-in-form {
    width: 30%;
    display: inline-flex;
    flex-direction: column;
  }
}

.sign-up-link {
  text-align: left;
}

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
