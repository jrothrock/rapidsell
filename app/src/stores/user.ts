import axios from 'axios';
import { defineStore } from 'pinia';
import { LogOutRequest } from '@/api/users/LogOut';

export interface User {
  access_token: string;
  id_token: string;
}

interface State {
  user: User | null;
}

const LOG_OUT_URL = `${import.meta.env.VITE_BASE_URL}/users/log_out`;

export const useAuthStore = defineStore("authStore", {
  state: (): State => ({
    user: null
  }),
  getters: {
    isLoggedIn: (state) => state.user != null,
    getAccessToken: (state) => state.user?.access_token,
    getIdToken: (state) => state.user?.id_token,
  },
  actions: {
    /* Check for token on initial load of the application */
    initializeAuthListener() {
      return new Promise((resolve) => {
        if(localStorage.getItem("id_token")) {
          const access_token: string = localStorage.getItem("access_token") as string;
          const id_token: string = localStorage.getItem("id_token") as string;
          const user: User = {access_token, id_token};
          this.user = user;
        }
        resolve(true);
      });
    },

    async loginUser(access_token: string, id_token: string) {
      const user: User = { access_token, id_token};
      this.user = user;
      localStorage.setItem("access_token", access_token);
      localStorage.setItem("id_token", id_token);
    },

    async logOutUser() {
      if(!this.isLoggedIn) return;
      const access_token: string = this.user?.access_token as string;
      const params: LogOutRequest = { access_token };
      try {
        await axios.post(LOG_OUT_URL, params);
      } finally {
        // If the user has logged into another device, the Auth will be expired
        // and throw a 500. Should clean up on backend.
        this.user = null;
        localStorage.removeItem("access_token");
        localStorage.removeItem("id_token");
      }
    }
  }
});

