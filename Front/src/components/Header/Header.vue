<template>
  <div>
    <el-row class="header">
      <el-col :xs="24" :sm="4" :md="4" :lg="4" :xl="2" class="logo">
        <div>
          <router-link to="/home">EasyThing</router-link>
        </div>
      </el-col>
      <el-col :xs="12" :sm="10" :md="10" :lg="10" :xl="11">
        <el-menu
          :default-active="$route.fullPath"
          mode="horizontal"
          active-text-color="#409EFF"
        >
          <el-menu-item index="/home">
            <router-link to="/home" class="link-item"> Главная </router-link>
          </el-menu-item>
        </el-menu>
      </el-col>
      <el-col :xs="12" :sm="10" :md="10" :lg="10" :xl="11" class="user-col">
        <el-dropdown trigger="click" v-if="isAuthenticated">
          <el-button icon="el-icon-bell" circle></el-button>
          <el-dropdown-menu slot="dropdown">
            <div style="width: 200px; height: 200px">notification</div>
          </el-dropdown-menu>
        </el-dropdown>

        <el-dropdown
          v-if="isAuthenticated"
          trigger="click"
          @command="(command) => command()"
        >
          <div class="user-avatar-button">
            <el-tooltip
              class="item"
              effect="dark"
              :content="userName"
              placement="bottom-end"
            >
              <el-avatar
                :size="40"
                src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"
              ></el-avatar>
            </el-tooltip>
          </div>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item :command="() => $router.push('/home')">
              Профиль
            </el-dropdown-item>
            <el-dropdown-item :command="exit" divided>Выход</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <el-button plain v-else-if="$route.fullPath !== '/login'">
          <router-link to="/login" class="link-item"> Войти </router-link>
        </el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Header",
  props: ["collapsedTrigger"],
  data() {
    return {
      search: {
        query: "",
      },
    };
  },
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

.logo a,
.item-link-sidebar a {
  transition: 150ms;
  color: #303133;
}

.logo {
  font-size: 20px;
  text-align: center;
  border-bottom: solid 1px #e6e6e6;
}

.logo a {
  line-height: 3em;
  color: #409eff;
}

.menu-user {
  position: absolute;
  right: 0;
}

.el-col {
  min-height: 50px;
}

.user-avatar-button {
  cursor: pointer;
}

.user-col {
  height: 61px;
  border-bottom: solid 1px #e6e6e6;
  padding: 10px 12px;
  text-align: right;
  display: flex;
  justify-content: flex-end;
}

.user-col > div {
  margin: 0px 5px;
}
</style>
