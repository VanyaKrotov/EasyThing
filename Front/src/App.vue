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
import { mapActions, mapGetters } from "vuex";
import Header from "./components/Header/Header";
import BodyContainer from "./components/BodyContainer/BodyContainer";

export default {
  name: "App",
  components: {
    Header,
    BodyContainer,
  },
  methods: {
    ...mapActions(["authUser"]),
  },
  computed: {
    ...mapGetters(["isLoadingUser"]),
  },
  async mounted() {
    this.authUser();
  },
};
</script>

<style>
* {
  font-family: "Nunito Sans", sans-serif;
  font-weight: 500;
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

.link-item {
  display: inline-block;
  height: 100%;
  color: #409eff;
}

.s_20x20 {
  width: 20px;
  height: 20px;
}
</style>
