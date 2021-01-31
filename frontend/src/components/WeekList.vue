<template>
  <div class="weeklist">
    <b-table striped hover :items="weeksProvider" :fields="fields">
      <template #cell(show_details)="row">
        <b-button size="sm" @click="row.toggleDetails" class="mr-2">
          {{ row.detailsShowing ? "Hide" : "Show" }} Details
        </b-button>
      </template>

      <template #row-details="row">
        <b-card>
          <WeekDetails :url="row.item.url" />
        </b-card>
      </template>

      <template #cell(start_date)="row">
        {{ getStartDate(row.item.week, row.item.year) }}
      </template>

      <template #cell(end_date)="row">
        {{ getEndDate(row.item.week, row.item.year) }}
      </template>
    </b-table>
  </div>
</template>

<script>
import { api } from "@/common/globals.js";
import axios from "axios";
import WeekDetails from "@/components/WeekDetails.vue";

export default {
  name: "WeekList",
  methods: {
    weeksProvider() {
      let token = this.$store.state.access;
      let promise = axios
        .get(api + "weeks/", { headers: { Authorization: `Bearer ${token}` } })
        .then((response) => {
          return response.data.results;
        })
        .catch((error) => {
          console.log(error);
          return [];
        });
      return promise;
    },
    getDate(week, year) {
      let date = new Date(year, 0, 1);
      date.setDate(date.getDate() + week * 7 - date.getDay() + 1);
      return date;
    },
    getStartDate(week, year) {
      let d = this.getDate(week, year);
      return d.toDateString();
    },
    getEndDate(week, year) {
      let d = this.getDate(week, year);
      d.setDate(d.getDate() + 4);
      return d.toDateString();
    },
  },
  data() {
    return {
      fields: ["week", "year", "start_date", "end_date", "show_details"],
    };
  },
  components: {
    WeekDetails,
  },
};
</script>
