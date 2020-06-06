<template>
  <el-row class="header">
    <el-col :xs="24" :sm="4" :md="4" :lg="4" :xl="10" class="logo">
      <router-link to="/home">EasyThing</router-link>
    </el-col>
    <el-col :xs="24" :sm="20" :md="20" :lg="20" :xl="14" class="links-control ">
      <el-menu
        :default-active="$route.fullPath"
        mode="horizontal"
        active-text-color="#409EFF"
      >
        <el-menu-item index="/home">
          <router-link to="/home" class="link-item">
            Главная
          </router-link>
        </el-menu-item>
        <el-menu-item index="/companies">
          <router-link to="/companies" class="link-item">
            Компании
          </router-link>
        </el-menu-item>
        <el-submenu
          :index="`/${userId}/`"
          v-if="isAuthenticated"
          class="menu-user"
        >
          <template slot="title">{{ userName }}</template>
          <router-link :to="`/${userId}/profile`"
            ><el-menu-item :index="`/${userId}/profile`">
              Профиль
            </el-menu-item></router-link
          >
          <el-menu-item :index="`/${userId}/notifications/`">
            Уведомления
          </el-menu-item>
          <el-menu-item :index="`/${userId}/settings/`">
            Настройки
          </el-menu-item>
          <el-menu-item @click="exit" index="exit">
            Выход
          </el-menu-item>
        </el-submenu>
        <el-menu-item v-else class="menu-user">
          <router-link to="/login">
            Войти
          </router-link>
        </el-menu-item>
      </el-menu>
    </el-col>
  </el-row>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Header",
  computed: {
    ...mapGetters(["getUserInformation", "isAuthenticated"]),
    fullPath() {
      return this.$route.fullPath;
    },
    userName() {
      const { first_name = "", last_name = "" } = this.getUserInformation || {};

      return `${first_name} ${last_name}`;
    },
    userId() {
      return this.getUserInformation ? this.getUserInformation.id : null;
    },
  },
  methods: {
    ...mapActions(["logoutUser"]),
    exit() {
      this.$confirm("Вы действительно хотите выйти?", `Выход`, {
        confirmButtonText: "Да, Выйти",
        cancelButtonText: "Отменить",
        type: "warning",
        confirmButtonClass: "el-button--danger",
      })
        .then(() => {
          this.logoutUser();
        })
        .catch(() => {});
    },
  },
};
</script>

<style scoped>
* {
  text-decoration: none;
}

.header {
  box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.5);
}

.logo a,
.item-link-sidebar a {
  transition: 150ms;
  color: #303133;
}

.logo {
  font-size: 20px;
  text-align: center;
  line-height: none;
}

.link-item {
  display: inline-block;
  height: 100%;
}

.logo a {
  line-height: 3em;
}

.menu-user {
  position: absolute;
  right: 0;
}

.el-col {
  min-height: 50px;
}
</style>
