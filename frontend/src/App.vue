<template>
  <div id="app">
    <div id="nav">
      <span v-if="this.$store.state.access">
        <router-link to="/">Home</router-link> |
        <router-link to="/users">Users</router-link> |
        <router-link to="/logout">Logout</router-link>
      </span>
      <span v-if="!this.$store.state.access">
        <router-link to="/login" v-if="this.$store.state.access === null"
          >Login</router-link
        >
      </span>
    </div>
    <b-container class="bv-example-row bv-example-row-flex-cols">
      <router-view />
    </b-container>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
