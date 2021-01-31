<template>
  <div id="users">
    <b-table striped hover :items="usersProvider" :fields="fields"></b-table>
  </div>
</template>

<script>
import { api } from "@/common/globals.js";
import axios from "axios";
import { checkLogin } from "@/common/auth.js";

export default {
  name: "Users",
  methods: {
    usersProvider() {
      let token = this.$store.state.access;
      let promise = axios
        .get(api + "users/", { headers: { Authorization: `Bearer ${token}` } })
        .then((response) => {
          console.log(response);
          return response.data.results;
        })
        .catch((error) => {
          console.log(error);
          return [];
        });
      return promise;
    },
  },
  beforeMount() {
    checkLogin(this).catch((error) => {
      console.log(error);
    });
  },
  data() {
    return {fields: ["id", "username", "email", "first_name", "last_name", "is_superuser"],};
  },
};
</script>
