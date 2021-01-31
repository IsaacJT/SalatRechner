import { api } from "@/common/globals.js"
import axios from "axios";

export async function checkLogin(vue) {
  let accessToken = vue.$store.state.access;
  let refreshToken = vue.$store.state.refresh;
  try {
    if (!accessToken || !refreshToken) {
      throw new Error("Not logged in");
    }
    axios.post(api + "token/verify/", { token: accessToken })
      .catch((err) => {
        console.log(err);
        /* Token might be expired; try to renew */
        axios.post(api + "token/refresh/", { refresh: refreshToken })
          .then((response) => {
            console.log("Successfully refresh login token");
            vue.$store.dispatch("login", { access: response.data.access, refresh: refreshToken });
          })
          .catch((refreshErr) => {
            console.log(refreshErr);
            /* TODO check this case */
            throw new Error("Invalid refresh token");
          });
      });
  } catch (e) {
    console.log(e);
    this.$store.dispatch("logout");
    this.$router.push({ name: "Login" });
  }
}