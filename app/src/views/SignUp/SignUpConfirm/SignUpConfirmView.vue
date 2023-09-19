<script setup lang="ts">
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { IonPage, IonContent, IonInput, IonItem, IonList, IonCol, IonRow, IonButton, IonLabel, IonSpinner } from '@ionic/vue';
import { useSignUpConfirm } from "./useSignUpConfirm";
import type { SignUpConfirmRequest } from "@/api/users/SignUpConfirm";

const route = useRoute();
const router = useRouter();

const confirmation_code = ref<string>();

const loading = ref<boolean>(false);

const { signUpConfirm } = useSignUpConfirm();

const callSignUpConfirm = async () => {
  loading.value = true;
  const params: SignUpConfirmRequest = {
    email: String(route.params.email),
    confirmation_code: confirmation_code.value as string,
  };
  await signUpConfirm(params, router);
  loading.value = false;
};
</script>

<template>
  <ion-page class="ion-page">
    <ion-content>
      <form class="sign-up-confirmation-form">
        <ion-list>
          <ion-item>
            <ion-input
              v-model="confirmation_code"
              label="Confirmation Code:"
            />
          </ion-item>
        </ion-list>
        <ion-row responsive-sm>
          <ion-col>
            <ion-button
              :disabled="loading"
              color="primary"
              expand="block"
              @click="callSignUpConfirm()"
            >
              <ion-label class="sign-up-confirm-label">
                Confirm
                <ion-spinner
                  v-if="loading"
                  class="spinner"
                /> 
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
  .sign-up-confirmation-form {
    width: 30%;
    display: inline-flex;
    flex-direction: column;
  }
}

.sign-up-confirm-label {
  display: flex;
  align-items: center;

  .spinner {
    height: 20px;
    width: 20px;
    margin: 0px 5px;
  }
}
</style>