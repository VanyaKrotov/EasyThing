<template>
  <div v-loading="isLoadingUser" id="app">
    <Header />
    <BodyContainer>
      <el-main>
        <!-- <keep-alive> -->
        <router-view></router-view>
        <!-- </keep-alive> -->
      </el-main>
    </BodyContainer>
    <!-- <Footer /> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import Header from './components/Header/Header';
import BodyContainer from './components/BodyContainer/BodyContainer';

export default {
  name: 'App',
  components: {
    Header,
    BodyContainer
  },
  computed: {
    ...mapGetters(['isLoadingUser'])
  },
  async mounted() {}
};
</script>

<style>
:root {
  --primary_text: #303133;
  --regular_text: #606266;
  --secondary_text: #909399;
}
* {
  font-family: 'Nunito Sans', sans-serif;
  font-weight: 500;
}

.ymap-container {
  height: 100%;
}

.container-map {
  width: 100%;
  height: 500px;
}

html,
body,
#app {
  width: 100%;
  height: 100%;
}

body {
  margin: 0px;
}

a {
  text-decoration: none;
}

.mlr1 {
  margin-left: 10px;
  margin-right: 10px;
}

.time {
  font-size: 13px;
  color: #999;
  margin-top: 4px;
}

.mtb1 {
  margin-top: 10px;
  margin-bottom: 10px;
}

.mtb05 {
  margin-top: 5px;
  margin-bottom: 5px;
}

.mlr05 {
  margin-left: 5px;
  margin-right: 5px;
}

.settings-controls {
  text-align: right;
}

.link {
  transition: 150ms;
  color: rgb(121, 187, 255);
}

.f12 {
  font-size: 12px;
}

.container {
  max-width: 400px;
  margin: 10px auto;
}

.link:hover {
  transition: 150ms;
  color: rgb(83, 168, 255);
}

.text-center {
  text-align: center;
}

.title {
  color: var(--primary_text);
}

.text-right {
  text-align: right;
}

.link-item {
  display: inline-block;
  height: 100%;
  color: #409eff;
}

.s_20x20 {
  width: 20px;
  height: 20px;
}

.fixed-button-right_bottom {
  position: fixed;
  right: 40px;
  bottom: 40px;
}

.el-drawer *:focus {
  outline: none;
}

.el-drawer__body {
  overflow-y: auto;
}
</style>
