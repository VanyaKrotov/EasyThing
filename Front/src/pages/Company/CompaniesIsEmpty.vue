<template>
  <div class="center-container">
    <h3>Список компаний пуст</h3>
    <div class="center">
      <el-button type="primary" plain @click="$router.push('/company/create')"
        ><i class="el-icon-plus" /> Зарегистрировать компанию</el-button
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "CompaniesIsEmpty",
};
</script>

<style scoped>
h3 {
  text-align: center;
  color: #909399;
}

.center-container {
  margin: 300px auto;
}
</style>
