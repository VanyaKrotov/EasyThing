<template>
  <el-row class="error-container text-center">
    <el-col>
      <PadlockSvg />
    </el-col>
    <el-col>
      <h2>Ошибка доступа!</h2>
      <h4>Данная страница доступна лишь зарегистрированым пользователям</h4>

      <el-tooltip content="вернуться назад" placement="bottom-end">
        <el-button type="primary" circle plain @click="$router.go(-1)"
          ><i class="el-icon-back"
        /></el-button>
      </el-tooltip>
      <router-link to="/registration" style="margin-left: 20px"
        ><el-button type="text">Регистрация</el-button></router-link
      >
      <router-link to="/login" style="margin-left: 20px"
        ><el-button type="text">Войти</el-button></router-link
      >
    </el-col>
  </el-row>
</template>

<script>
import PadlockSvg from "../../images/padlock.svg";

export default {
  name: "AuthenticationError",
  components: {
    PadlockSvg,
  },
};
</script>

<style scoped>
h4,
h2 {
  color: #606266;
}
</style>
