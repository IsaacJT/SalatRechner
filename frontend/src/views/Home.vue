<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Home />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Home from '@/components/Home.vue'; // @ is an alias to /src

export default defineComponent({
  name: 'Home',
  components: {
    Home,
  },
});
</script>
