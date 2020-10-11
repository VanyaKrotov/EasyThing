<template>
  <el-row :gutter="20" class="mtb1">
    <ServiceCard
      v-for="service in services"
      :key="`service-${service.id}`"
      :service="service"
    />
  </el-row>
</template>

<script>
import { mapGetters } from 'vuex';
import ServiceCard from '../../Service/ServiceCard';
export default {
  name: 'Services',
  components: {
    ServiceCard
  },
  computed: {
    ...mapGetters(['getCompanyValues']),
    services: ({ getCompanyValues = {} }) => getCompanyValues.services || []
  }
};
</script>

<style scoped></style>
