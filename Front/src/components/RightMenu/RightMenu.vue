<template>
  <el-row class="menu-row">
    <div>
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
        <div style="height: 82%">
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

        <div style="height: 18%">
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
      </el-menu>
    </div>
    <div style="width: 100%">
      <slot />
    </div>
  </el-row>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "RightMenu",
  data() {
    return {
      isCollapsed: true,
    };
  },
  computed: {
    ...mapGetters(["isAuthenticated"]),
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
  min-height: 700px;
}
</style>