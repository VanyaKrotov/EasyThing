<template>
  <el-row class="menu-row" :style="{ height: getFullHeight }">
    <div style="height: 100%">
      <el-menu
        :default-active="$route.fullPath"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        active-text-color="#409EFF"
        :collapse="isCollapsed"
        v-if="isAuthenticated"
        style="height: 100%"
        @select="menuSelectedHandle"
      >
        <div style="height: 80%">
          <el-menu-item index="/companies">
            <i class="el-icon-office-building"></i>
            <span slot="title" to="/companies">Компании</span>
          </el-menu-item>

          <el-menu-item index="/analitics">
            <i class="el-icon-pie-chart"></i>
            <span slot="title">Аналитика</span>
          </el-menu-item>

          <el-menu-item index="/calendar">
            <i class="el-icon-date"></i>
            <span slot="title">Календарь</span>
          </el-menu-item>

          <el-menu-item index="/board">
            <i class="el-icon-data-line"></i>
            <span slot="title">Доска</span>
          </el-menu-item>
        </div>

        <div style="height: 20%; position: relative;">
          <div style="position: absolute; width: 100%; bottom: 0;">
            <el-menu-item index="/settings">
              <i class="el-icon-setting"></i>
              <span slot="title">Настройки</span>
            </el-menu-item>

            <el-menu-item @click="isCollapsed = !isCollapsed">
              <i :class="`el-icon-arrow-${isCollapsed ? 'right' : 'left'}`"></i>
              <span slot="title" v-if="isCollapsed">Развернуть</span>
              <span slot="title" v-else>Свернуть</span>
            </el-menu-item>
          </div>
        </div>
      </el-menu>
    </div>
    <div class="main-container">
      <slot />
    </div>
  </el-row>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "BodyContainer",
  data() {
    return {
      isCollapsed: true,
    };
  },
  computed: {
    ...mapGetters(["isAuthenticated"]),
    getFullHeight() {
      const clientHeight = document.getElementsByTagName("html")[0]
        .clientHeight;
      return `${clientHeight - 61 * (clientHeight < 770 ? 2 : 1)}px`;
    },
    getTopMenuSectionHeight() {
      return `${
        this.getFullHeight - document.getElementById("bottom-menu-section")
      }px`;
    },
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    menuSelectedHandle(menuItemIndex) {
      if (menuItemIndex) {
        this.$router.push(menuItemIndex);
      }
    },
  },
};
</script>

<style scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}

.menu-row {
  display: flex;
  justify-content: flex-start;
}

.main-container {
  width: 100%;
  overflow-y: auto;
}
</style>