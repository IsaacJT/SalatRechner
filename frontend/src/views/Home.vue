<template>
  <div class="home">
    <WeekList />
  </div>
</template>

<script>
import { checkLogin } from "@/common/auth.js";
import WeekList from "@/components/WeekList.vue";
export default {
  name: "Home",
  beforeMount() {
    return checkLogin(this);
  },
  components: {
    WeekList,
  },
};
</script>
