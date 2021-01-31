<template>
  <div class="weekdetails">
    <h4>Expenses</h4>
    <b-table ref="expensesTable" striped hover :items="expensesProvider" :fields="expenseFields">
      <template #cell(show_comment)="row">
        <b-button size="sm" @click="row.toggleDetails" class="mr-2">
          {{ row.detailsShowing ? "Hide" : "Show" }} Comment
        </b-button>
      </template>

      <template #row-details="row">
        <b-card>
          <b-form-textarea
            placeholder="Comment..."
            v-model="row.item.comments"
            :ref="'expenseComment_' + row.item.id"
          ></b-form-textarea>
          <br />
          <b-button class="float-right btn-success" @click="updateExpenseComment(row.item, $event)">Update</b-button>
        </b-card>
      </template>

      <template #custom-foot>
        <b-tr>
          <b-td><b-form-select v-model="newExpenseUser" :options="users"></b-form-select></b-td>
          <b-td><b-form-input v-model="newExpenseAmount" placeholder="Amount..."></b-form-input></b-td>
          <b-td><b-button class="float-right btn-success" @click="addExpense()">Add</b-button></b-td>
        </b-tr>
      </template>
    </b-table>

    <br />

    <h4>Days</h4>
    <b-tabs justified card>
      <b-tab v-for="i in getTabs()" :key="'dyn-tab-' + i.day_name" :title="i.day_name">
        <DayDetails :url="i.url" />
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
import axios from "axios";
import { api } from "@/common/globals.js";
import DayDetails from "@/components/DayDetails.vue";

export default {
  name: "WeekDetails",
  props: {
    url: String,
  },
  data() {
    return {
      days: [],
      expenses: [],
      expenseFields: ["username", "amount_euro", "show_comment"],
      newExpenseUser: null,
      newExpenseAmount: null,
      users: [],
    };
  },
  beforeMount() {
    return this.update();
  },
  methods: {
    update() {
      let vue = this;
      let token = this.$store.state.access;
      let promise = axios
        .get(vue.$props.url, { headers: { Authorization: `Bearer ${token}` } })
        .then((response) => {
          vue.$data.days = response.data.days;
          vue.$data.expenses = response.data.expenses;
          vue.$refs.expensesTable.refresh();
        })
        .then(function() {
          vue.getUsers();
        })
        .catch((error) => {
          console.log(error);
        });
      return promise;
    },
    getTabs() {
      return this.$data.days;
    },
    expensesProvider() {
      return this.$data.expenses;
    },
    updateExpenseComment(item, event) {
      let token = this.$store.state.access;
      event.target.disabled = true;
      axios
        .patch(item.url, { comments: item.comments }, { headers: { Authorization: `Bearer ${token}` } })
        .then(function() {
          event.target.disabled = false;
        })
        .catch((error) => {
          console.log(error);
          event.target.disabled = false;
        });
    },
    getUsers() {
      let vue = this;
      let token = this.$store.state.access;
      let promise = axios
        .get(api + "users/", { headers: { Authorization: `Bearer ${token}` } })
        .then((response) => {
          vue.$data.users = response.data.results.map((x) => x.username);
        })
        .catch((error) => {
          console.log(error);
          vue.$data.users = [];
        });
      return promise;
    },
    addExpense() {
      // TODO
      // let vue = this;
      // let token = this.$store.state.access;
      // let promise = axios
      //   .post(api + "expenses/", {}, { headers: { Authorization: `Bearer ${token}` } })
      //   .then((response) => {
      //     vue.$data.users = response.data.results.map((x) => x.username);
      //   })
      //   .catch((error) => {
      //     console.log(error);
      //     vue.$data.users = [];
      //   });
      // return promise;
    },
  },
  components: {
    DayDetails,
  },
};
</script>
