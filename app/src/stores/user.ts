import axios from 'axios';
import { defineStore } from 'pinia'
import { LogOutRequest, LogOutResponse } from '@/api/users/LogOut';

export interface User {
  access_token: string;
}

interface State {
  user: User | null;
}

const LOG_OUT_URL = "https://api.rapidsell.io/users/log_out";

export const useAuthStore = defineStore("authStore", {
  state: (): State => ({
    user: null
  }),
  getters: {
    isLoggedIn: (state) => state.user != null,
  },
  actions: {
    /* Check for token on initial load of the application */
    initializeAuthListener() {
      return new Promise((resolve) => {
        if(localStorage.getItem("access_token")) {
          const access_token: string = localStorage.getItem("access_token") as string;
          const user: User = {access_token}
          this.user = user;
        }
        resolve(true);
      })
    },

    async loginUser(access_token: string) {
      const user: User = { access_token }
      this.user = user;
      localStorage.setItem("access_token", access_token)
    },

    async logOutUser() {
      if(!this.isLoggedIn) return;
      const access_token: string = this.user?.access_token as string;
      const params: LogOutRequest = { access_token }
      const response = await axios.post(LOG_OUT_URL, params);
      const data: LogOutResponse = response.data;

      if (data.success) {
        this.user = null;
        localStorage.removeItem("access_token");
      }
    }
  }
});

