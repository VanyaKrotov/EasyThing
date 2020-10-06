<template>
  <el-row class="menu-row" :style="{ height: getFullHeight }">
    <div style="height: 100%">
      <el-menu
        text-color="#909399"
        :default-active="$route.fullPath"
        class="el-menu-vertical-demo"
        active-text-color="#409EFF"
        :collapse="isCollapsed"
        v-if="isAuthenticated"
        style="height: 100%"
        @select="menuSelectedHandle"
      >
        <div style="height: 80%">
          <el-menu-item index="/companies">
            <i class="el-icon-office-building"></i>
            <span slot="title">Компании</span>
          </el-menu-item>

          <el-menu-item index="/servecies">
            <i class="el-icon-school"></i>
            <span slot="title">Предприятия</span>
          </el-menu-item>

          <el-menu-item index="/analytics">
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

        <div style="height: 20%; position: relative">
          <div style="position: absolute; width: 100%; bottom: 0">
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
      menuHeight: 0,
    };
  },
  computed: {
    ...mapGetters(["isAuthenticated"]),
    getFullHeight() {
      return `${this.menuHeight}px`;
    },
  },
  methods: {
    calcMenuHeight() {
      const clientHeight = document.getElementsByTagName("html")[0]
        .clientHeight;

      return clientHeight - 61 * (clientHeight < 770 ? 2 : 1);
    },
    menuSelectedHandle(menuItemIndex) {
      if (menuItemIndex) {
        this.$router.push(menuItemIndex);
      }
    },
    onResuze() {
      this.menuHeight = this.calcMenuHeight();
    },
  },
  mounted() {
    this.menuHeight = this.calcMenuHeight();

    window.onresize = this.onResuze;
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