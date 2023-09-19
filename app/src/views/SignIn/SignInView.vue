<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { IonPage, onIonViewWillLeave, IonContent, IonInput, IonItem, IonList, IonCol, IonRow, IonButton, IonLabel, IonSpinner } from '@ionic/vue';
import { useSignIn } from "./useSignIn";
import type { SignInRequest } from "@/api/users/SignIn";


const email = ref<string>();
const password = ref<string>();

const loading = ref<boolean>(false);

const router = useRouter();
const { signIn } = useSignIn();

const callSignIn = async () => {
  loading.value = true;
  const params: SignInRequest = {
    email: email.value as string,
    password: password.value as string,
  };
  await signIn(params, router);
  loading.value = false;
};

onIonViewWillLeave(() => {
  email.value = undefined;
  password.value = undefined;
})
</script>

<template>
  <ion-page class="ion-page">
    <ion-content>
      <form class="sign-in-form">
        <ion-list>
          <ion-item>
            <ion-input
              v-model="email"
              label="Email:"
            />
          </ion-item>
          <ion-item>
            <ion-input
              v-model="password"
              label="Password:"
              type="password"
            />
          </ion-item>
        </ion-list>
        <ion-row responsive-sm>
          <ion-col>
            <ion-button
              :disabled="loading"
              color="primary"
              expand="block"
              @click="callSignIn()"
            >
              <ion-label class="sign-in-label">
                Sign In
                <ion-spinner
                  v-if="loading"
                  class="spinner"
                /> 
              </ion-label>
            </ion-button>
          </ion-col>
        </ion-row>
        <ion-row responsive-sm>
          <ion-col class="sign-up-link">
            <router-link :to="{ name: 'SignUp' }">
              Sign Up
            </router-link>
          </ion-col>
        </ion-row>
      </form>
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

.sign-in-label {
  display: flex;
  align-items: center;

  .spinner {
    height: 20px;
    width: 20px;
    margin: 0px 5px;
  }
}
</style>
