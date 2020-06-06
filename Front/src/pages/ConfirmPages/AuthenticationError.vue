<template>
  <el-card class="error-container" shadow="always">
    <link
      href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Mono:wght@500&display=swap"
      rel="stylesheet"
    />
    <h3>Данная страница доступна лишь зарегистрированым пользователям</h3>
    <div class="center">
      <el-button type="success" plain @click="$router.go(-1)"
        ><i class="el-icon-back" /> Вернутся назад</el-button
      >
      <router-link to="/login" style="margin-left: 10px;"
        ><el-button type="primary" plain>Войти</el-button></router-link
      >
    </div>
  </el-card>
</template>

<script>
export default {
  name: "AuthenticationError",
};
</script>

<style scoped>
h3 {
  text-align: center;
}
</style>
