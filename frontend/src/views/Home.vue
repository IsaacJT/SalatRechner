<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
  </div>
</template>

<script>
import { checkLogin } from "@/common/auth.js";
export default {
  name: "Home",
  components: {},
  beforeMount() {
    checkLogin(this).catch((error) => {
      console.log(error);
    });
  },
};
</script>
