<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { IonPage, IonContent, IonInput, IonItem, IonList, IonCol, IonRow, IonButton } from '@ionic/vue';
import { useSignUp } from "./useSignUp";
import type { SignUpRequest } from "@/api/users/SignUp";

const router = useRouter();
const { signUp } = useSignUp();

const email = ref('');
const password = ref('');

const callSignUp = async () => {
  const params: SignUpRequest = {
    email: email.value,
    password: password.value
  }
  await signUp(params, router)
}
</script>

<template>
  <ion-page class="ion-page">
    <ion-content>
      <form class="sign-up-form">
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
            <ion-button @click="callSignUp()" color="light" expand="block">Sign Up</ion-button>
          </ion-col>
        </ion-row>
      </form> 
    </ion-content>
  </ion-page>
</template>

<style scoped>
@media(min-width:640px){
  .sign-up-form {
    width: 30%;
    display: inline-flex;
    flex-direction: column;
  }
}
</style>
