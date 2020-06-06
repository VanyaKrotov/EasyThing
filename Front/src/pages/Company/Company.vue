<template>
  <div>
    <div v-html="getCompanyValues.description" />
    <router-view></router-view>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Company",
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["getCompanyValues"]),
  },
  methods: {
    ...mapActions(["fetchCompany"]),
  },
  async mounted() {
    const companyId = this.$route.params.id || 0;

    this.fetchCompany({ companyId });
  },
};
</script>

<style scoped></style>
