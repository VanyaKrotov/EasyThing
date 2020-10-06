<template>
  <el-row class="text-center">
    <el-col>
      <Error404 />
    </el-col>
    <el-col>
      <h2>Эх... ☹</h2>
      <h4>Страница не найдена!</h4>
      <el-tooltip content="Вернуться назад" placement="bottom-end">
        <el-button type="primary" plain circle @click="$router.go(-1)"
          ><i class="el-icon-back"
        /></el-button>
      </el-tooltip>
    </el-col>
  </el-row>
</template>

<script>
import Error404 from "../../images/error_404.svg";

export default {
  name: "Page404",
  components: {
    Error404,
  },
};
</script>

<style scoped>
h4,
h2 {
  color: #606266;
}

.center {
  text-align: center;
}
</style>
