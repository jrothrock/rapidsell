<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { IonPage, IonContent, IonInput, IonItem, IonList, IonCol, IonRow, IonButton, IonLabel, IonSpinner } from '@ionic/vue';
import { useSignUp } from "./useSignUp";
import type { SignUpRequest } from "@/api/users/SignUp";

const router = useRouter();
const { signUp } = useSignUp();

const email = ref('');
const password = ref('');

const loading = ref<boolean>(false);

const callSignUp = async () => {
  loading.value = true;
  const params: SignUpRequest = {
    email: email.value,
    password: password.value
  }
  await signUp(params, router)
  loading.value = false;
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
            <ion-button :disabled="loading" @click="callSignUp()" color="primary" expand="block">
              <ion-label class="sign-up-label">
                Sign Up
                <ion-spinner v-if="loading" class="spinner"></ion-spinner> 
              </ion-label>
            </ion-button>
          </ion-col>
        </ion-row>
      </form> 
    </ion-content>
  </ion-page>
</template>

<style scoped lang="scss">
@media(min-width:640px){
  .sign-up-form {
    width: 30%;
    display: inline-flex;
    flex-direction: column;
  }
}

.sign-up-label {
  display: flex;
  align-items: center;

  .spinner {
    height: 20px;
    width: 20px;
    margin: 0px 5px;
  }
}
</style>
