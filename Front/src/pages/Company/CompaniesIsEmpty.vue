<template>
  <el-card class="error-container" shadow="always">
    <h3>У вас нет компаний</h3>
    <div class="center">
      <el-button type="primary" plain
        ><i class="el-icon-plus" /> Зарегистрировать компанию</el-button
      >
    </div>
  </el-card>
</template>

<script>
export default {
  name: "CompaniesIsEmpty",
};
</script>

<style scoped>

h3 {
  text-align: center;
  font-family: "DM Mono", monospace;
}
</style>
