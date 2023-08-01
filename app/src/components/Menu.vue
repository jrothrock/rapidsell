<script setup lang="ts">
  import { IonButtons, IonFooter, IonContent, IonHeader, IonMenu, IonMenuButton, IonTitle, IonToolbar } from '@ionic/vue';
  import { menuController } from "@ionic/vue";
  import { useAuthStore } from '@/stores';
  import { useRouter } from 'vue-router';

  const store = useAuthStore();
  const router = useRouter();

  const callLogOutUser = async () => {
    await store.logOutUser();
    router.push({name: "SignIn"})
    menuController.toggle();
  };
</script>

<template>
  <ion-menu content-id="main-content" id="menu-content">
    <ion-header>
      <ion-toolbar>
        <ion-title>Menu Content</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
      
    </ion-content>
    <ion-footer>
        <a v-if="store.isLoggedIn" @click="callLogOutUser()">Log Out</a>
    </ion-footer>
  </ion-menu>
  <ion-content id="menu-header">
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-menu-button></ion-menu-button>
        </ion-buttons>
        <ion-title>RapidSell</ion-title>
      </ion-toolbar>
    </ion-header>
  </ion-content>
</template>

<style scoped lang="scss">
.ios { 
  #menu-header {
    top: 40px;
  }

  #menu-content {
    top: 40px;
  }
}

#menu-header {
  max-height: 70px;
}
</style>