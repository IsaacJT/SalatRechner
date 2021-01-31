<template>
  <div class="login">
    <h1>Login</h1>

    <b-form @submit="login">
      <b-form-group
        id="username-group"
        label="Username"
        label-for="username-input"
      >
        <b-form-input
          type="text"
          name="username"
          id="username-input"
          v-model="input.username"
          placeholder="Username"
          v-on:keyup.enter="login()"
          required
        />
      </b-form-group>

      <b-form-group
        id="password-group"
        label="Password"
        label-for="password-input"
      >
        <b-form-input
          type="password"
          name="password"
          id="password-input"
          v-model="input.password"
          placeholder="Password"
          v-on:keyup.enter="login()"
          required
        />
      </b-form-group>
      <b-button type="button" v-on:click="login()" :disabled="busy"
        >Login</b-button
      >
    </b-form>
    <br />
    <h2>{{ message }}</h2>
  </div>
</template>

<script>
import { api } from "@/common/globals.js";
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      input: {
        username: "",
        password: "",
      },
      message: "",
      busy: false,
    };
  },
  methods: {
    doLogin(username, password) {
      let vue = this;
      axios
        .post(api + "token/", { username: username, password: password })
        .then(function(response) {
          vue.$store.dispatch("login", response.data);
          vue.busy = false;
          vue.$router.replace({ name: "Home" });
        })
        .catch(function(error) {
          if (error.response.data.detail) {
            vue.message = error.response.data.detail;
          } else {
            vue.message = error;
          }
          vue.busy = false;
        });
    },
    login() {
      if (this.input.username != "" && this.input.password != "") {
        this.busy = true;
        this.doLogin(this.input.username, this.input.password);
      } else {
        this.message = "Please enter a username and password";
      }
    },
    redirectIfLoggedIn() {
      if (this.$store.state.access !== null) {
        this.$router.replace({ name: "Home" });
      }
    },
  },
  mounted() {
    this.redirectIfLoggedIn();
  },
};
</script>

<style scoped>
#login {
  width: 500px;
  border: 1px solid #cccccc;
  background-color: #ffffff;
  margin: auto;
  margin-top: 200px;
  padding: 20px;
}
</style>
