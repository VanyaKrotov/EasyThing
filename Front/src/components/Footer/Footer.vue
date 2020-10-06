<template>
  <el-footer>
    <el-row :gutter="20">
      <el-col :span="16"><div class="grid-content bg-purple">1</div></el-col>
      <el-col :span="8"><div class="grid-content bg-purple">2</div></el-col>
    </el-row>
  </el-footer>
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style scoped>
.el-footer {
  color: #00181f;
  border-top: solid 1px #e6e6e6 
}


</style>
