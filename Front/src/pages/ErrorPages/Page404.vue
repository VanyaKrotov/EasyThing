<template>
  <el-card class="error-container" shadow="always">
    <h1>Opps!☹</h1>
    <h2>Ошибка 404: Страница не найдена!</h2>
    <div class="center">
      <el-button type="success" plain @click="$router.go(-1)"
        ><i class="el-icon-back" /> Вернутся назад</el-button
      >
      <el-button type="warning" plain
        ><i class="el-icon-warning-outline" /> Написать в
        техподдержку</el-button
      >
    </div>
  </el-card>
</template>

<script>
export default {
  name: "Page404",
};
</script>

<style scoped>
h1,
h2 {
  text-align: center;
  font-family: "DM Mono", monospace;
}

h1 {
  font-size: 60px;
}

.center {
  text-align: center;
}
</style>
