<template>
  <div id="logout">
    <h1>You have been logged out...</h1>
  </div>
</template>

<script>
export default {
  name: "Home",
  methods: {
    doLogout: function() {
      this.$store.dispatch("logout");
      this.interval = setInterval(function() {
        this.$router.replace({ name: "Login" });
        clearInterval(this.interval);
      }.bind(this), 1000);
    },
  },
  mounted() {
    this.doLogout();
  },
};
</script>
