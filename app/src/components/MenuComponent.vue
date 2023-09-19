<script setup lang="ts">
  import { IonButtons, IonFooter, IonList, IonItem, IonContent, IonHeader, IonMenu, IonMenuButton, IonTitle, IonToolbar } from '@ionic/vue';
  import { menuController } from "@ionic/vue";
  import { useAuthStore } from '@/stores';
  import { useRouter } from 'vue-router';

  const store = useAuthStore();
  const router = useRouter();

  const callLogOutUser = async () => {
    await router.push({name: "SignIn"});
    await menuController.toggle();
    await store.logOutUser();
  };
</script>

<template>
  <ion-menu
    id="menu-content"
    content-id="main-content"
  >
    <ion-header>
      <ion-toolbar>
        <ion-title>Menu Content</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
      <ion-list v-if="store.isLoggedIn">
        <ion-item>
          <a
            @click="router.push({name : 'Scanning'}); menuController.toggle()"
          >
            <p>Scanning</p>
        </a>
        </ion-item>
      </ion-list>
      <p v-if="!store.isLoggedIn">
        Login/Signup to access the other pages.
      </p>
    </ion-content>
    <ion-footer id="menu-footer">
      <a
        v-if="store.isLoggedIn"
        @click="callLogOutUser()"
      >
        Log Out
      </a>
      <router-link
        v-if="!store.isLoggedIn"
        :to="{ name: 'SignIn' }"
      >
        <p>Log In</p>
      </router-link>
    </ion-footer>
  </ion-menu>
  <ion-content id="menu-header">
    <ion-header>
      <ion-toolbar>
        <ion-buttons>
          <ion-menu-button />
          <span class="title-router-container">
            <router-link :to="{ name: 'Home'}">
              <ion-title>RapidSell</ion-title>
            </router-link>
          </span>
        </ion-buttons>
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

  #menu-footer {
    bottom: 40px;
  }
}

.title-router-container {
  flex-grow: 1;

  a {
    display: inline-flex;
    position: relative;
    left: -24px;
  }
}

#menu-header {
  max-height: 70px;
}
</style>