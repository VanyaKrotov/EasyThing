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
      >
        <el-menu-item index="/companies">
          <router-link to="/companies" class="link-item">
            <i class="el-icon-office-building"></i>
          </router-link>
          <span slot="title" to="/companies">Компании</span>
        </el-menu-item>
        <el-menu-item index="/settings">
          <router-link to="/settings" class="link-item">
            <i class="el-icon-setting"></i>
          </router-link>
          <span slot="title">Настройки</span>
        </el-menu-item>
      </el-menu>
    </div>
    <div style="width: 100%;">
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
</style>