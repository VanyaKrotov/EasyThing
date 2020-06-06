<template>
  <div v-html="company.description">
    
  </div>
</template>

<script>
import { getRequest } from "../../request-methods";
// import { map } from 'vuex';

export default {
  name: "CompanyProfile",
  data() {
    return {
      company: {},
    };
  },
  async mounted() {
    const companyId = this.$route.params.id;
    try {
      const { company } = await getRequest({
        url: `api/v1/Company/${companyId}/`,
      });

      this.company = company;
    } catch (error) {
      console.error(error);
    }
  },
};
</script>

<style scoped></style>
