<template>
  <div>
    <el-row class="header">
      <el-col :xs="24" :sm="4" :md="4" :lg="4" :xl="2" class="logo">
        <div>
          <router-link to="/home">EasyThing</router-link>
        </div>
      </el-col>
      <el-col :xs="18" :sm="14" :md="14" :lg="16" :xl="11">
        <el-menu
          :default-active="$route.fullPath"
          mode="horizontal"
          @select="(path) => $router.push(path)"
          active-text-color="#409EFF"
        >
          <el-menu-item index="/home">
            <i class="el-icon-house" />
            <span slot="title" class="menu-header-title">Главная</span>
          </el-menu-item>

          <el-menu-item index="/near">
            <i class="el-icon-location-information" />
            <span slot="title" class="menu-header-title">Поблизости</span>
          </el-menu-item>

          <el-menu-item index="/news">
            <i class="el-icon-news" />
            <span slot="title" class="menu-header-title">Новости</span>
          </el-menu-item>

          <!-- <el-menu-item index="/about">
            <i class="el-icon-warning-outline" />
            <span slot="title" class="menu-header-title">О нас</span>
          </el-menu-item>

          <el-menu-item index="/help">
            <i class="el-icon-help" />
            <span slot="title" class="menu-header-title">Помощь</span>
          </el-menu-item> -->
        </el-menu>
      </el-col>
      <el-col :xs="6" :sm="6" :md="6" :lg="4" :xl="11" class="user-col">
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
            <el-dropdown-item :command="() => $router.push('/my/profile')">
              Профиль
            </el-dropdown-item>
            <el-dropdown-item :command="exit" divided>Выход</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>

        <el-button
          plain
          v-else-if="$route.fullPath !== '/login'"
          @click="$router.push('/login')"
        >
          Войти
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
@media screen and (max-width: 600px) {
  .menu-header-title {
    display: none;
  }
}

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
