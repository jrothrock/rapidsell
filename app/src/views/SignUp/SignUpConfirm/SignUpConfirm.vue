<script setup lang="ts">
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { IonPage, IonContent, IonInput, IonItem, IonList, IonCol, IonRow, IonButton } from '@ionic/vue';
import { useSignUpConfirm } from "./useSignUpConfirm";
import type { SignUpConfirmRequest } from "@/api/users/SignUpConfirm";

const route = useRoute();
const router = useRouter();

const confirmation_code = ref('');

const { signUpConfirm } = useSignUpConfirm();

const callSignUpConfirm = async () => {
  const params: SignUpConfirmRequest = {
    email: String(route.params.email),
    confirmation_code: confirmation_code.value
  }
  await signUpConfirm(params, router)
}
</script>

<template>
  <ion-page class="ion-page">
    <ion-content>
      <form class="sign-up-confirmation-form">
        <ion-list>
          <ion-item>
            <ion-input label="Confirmation Code:" v-model="confirmation_code"></ion-input>
          </ion-item>
        </ion-list>
        <ion-row responsive-sm>
          <ion-col>
            <ion-button @click="callSignUpConfirm()" color="light" expand="block">Confirm</ion-button>
          </ion-col>
        </ion-row>
      </form> 
    </ion-content>
  </ion-page>
</template>

<style scoped>
@media(min-width:640px){
  .sign-up-confirmation-form {
    width: 30%;
    display: inline-flex;
    flex-direction: column;
  }
}
</style>