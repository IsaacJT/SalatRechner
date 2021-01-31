<template>
  <b-card-text>
  {{this.$props.url}}
  </b-card-text>
</template>

<script>
import axios from "axios";

export default {
  name: "DayDetails",
  props: {
    url: String,
  },
  data() {
    return {
      day: {},
    };
  },
  mounted() {
    let vue = this;
    let token = this.$store.state.access;
    let promise = axios
      .get(vue.$props.url, { headers: { Authorization: `Bearer ${token}` } })
      .then((response) => {
          vue.$data.day = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
    return promise;
  },
};
</script>
