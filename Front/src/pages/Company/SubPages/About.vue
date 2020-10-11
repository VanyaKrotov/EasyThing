<template>
  <div class="mr10" v-html="description"></div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'About',
  computed: {
    ...mapGetters(['getCompanyValues', 'isLoadingCompany']),
    description: ({ getCompanyValues = {} }) => {
      return (getCompanyValues || {}).description;
    }
  }
};
</script>

<style lang="scss" scoped></style>
