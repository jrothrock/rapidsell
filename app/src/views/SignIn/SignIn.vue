<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { IonPage, IonContent, IonInput, IonItem, IonList, IonCol, IonRow, IonButton } from '@ionic/vue';
import { useSignIn } from "./useSignIn";
import type { SignInRequest } from "@/api/users/SignIn";


const email = ref('');
const password = ref('');

const router = useRouter();
const { signIn } = useSignIn();

const callSignIn = async () => {
  const params: SignInRequest = {
    email: email.value,
    password: password.value
  }
  await signIn(params, router)
}
</script>

<template>
  <ion-page class="ion-page">
    <ion-content>
      <form class="sign-in-form">
        <ion-list>
          <ion-item>
            <ion-input label="Email:" v-model="email"></ion-input>
          </ion-item>
          <ion-item>
            <ion-input label="Password:" v-model="password" type="password"></ion-input>
          </ion-item>
        </ion-list>
        <ion-row responsive-sm>
          <ion-col>
            <ion-button @click="callSignIn()" color="light" expand="block">Sign In</ion-button>
          </ion-col>
        </ion-row>
        <ion-row responsive-sm>
          <ion-col class="sign-up-link">
            <router-link to="/sign_up">Sign Up</router-link>
          </ion-col>
        </ion-row>
      </form>
    </ion-content>
  </ion-page>
</template>

<style scoped>
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
</style>
