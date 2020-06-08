<template>
  <div>
    <el-row>
      <el-col :xs="24" :sm="6" :md="4" :lg="4" :xl="2" class="center">
        <el-avatar
          :size="100"
          src="https://cube.elemecdn.com/e/fd/0fc7d20532fdaf769a25683617711png.png"
        >
        </el-avatar>
      </el-col>
      <el-col
        :xs="24"
        :sm="18"
        :md="10"
        :lg="10"
        :xl="11"
        class="text-container"
      >
        <div class="title-container">
          {{ getCompanyValues.title }}
        </div>
        <div class="text-description-company">
          <span class="text-color-silver ">{{ getCompanyValues.email }}</span>
        </div>
        <div class="text-description-company">
          <span class="text-color-silver ">
            Основана: {{ getCompanyValues.dateCreated | dateCreateFilter }}
          </span>
        </div>
        <div class="text-description-company">
          <span class="text-color-silver ">
            Зарегистрирована:
            {{ getCompanyValues.dateRegistration | dateCreateFilter }}
          </span>
        </div>
      </el-col>
      <el-col
        :xs="24"
        :sm="24"
        :md="10"
        :lg="10"
        :xl="11"
        class="text-container"
      >
        <div
          class="text-description-company"
          v-if="getCompanyValues.services && getCompanyValues.services.length"
        >
          <span>Предприятия:</span>
          <span
            v-bind:key="service.id"
            class="text-color-silver"
            v-for="service in getCompanyValues.services"
          >
            {{ service.title }},
          </span>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-collapse>
        <el-collapse-item title="Описание компании" name="1">
          <div v-html="getCompanyValues.description" /> </el-collapse-item
      ></el-collapse>
    </el-row>
    <el-row>
      <el-menu
        :default-active="path"
        mode="horizontal"
        active-text-color="#409EFF"
      >
        <el-menu-item index="feed">
          <router-link
            :to="`/company/${getCompanyValues.id}/feed`"
            class="link-item"
          >
            Общее</router-link
          ></el-menu-item
        >
        <el-menu-item index="services">
          <router-link
            :to="`/company/${getCompanyValues.id}/services`"
            class="link-item"
          >
            Предприятия</router-link
          >
        </el-menu-item>
        <el-menu-item index="workers">
          <router-link
            :to="`/company/${getCompanyValues.id}/workers`"
            class="link-item"
          >
            Сотрудники</router-link
          >
        </el-menu-item>
        <el-menu-item index="schedule">
          <router-link
            :to="`/company/${getCompanyValues.id}/schedule`"
            class="link-item"
          >
            Графики</router-link
          >
        </el-menu-item>
        <el-menu-item index="settings">
          <router-link
            :to="`/company/${getCompanyValues.id}/settings`"
            class="link-item"
          >
            Настройки</router-link
          >
        </el-menu-item>
      </el-menu>
    </el-row>
    <router-view></router-view>
    <div class="edit-link-floating-button">
      <router-link
        :to="`/company/${getCompanyValues.id}/edit`"
        class="link-item"
      >
        <el-button type="primary" circle icon="el-icon-edit" />
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import { ru } from "date-fns/locale";
import { format } from "date-fns";

export default {
  name: "Company",
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["getCompanyValues"]),
    path() {
      return this.$route.fullPath.split("/").pop();
    },
  },
  methods: {
    ...mapActions(["fetchCompany"]),
  },
  async mounted() {
    const companyId = this.$route.params.id || 0;

    this.fetchCompany({ companyId });
  },
  filters: {
    dateCreateFilter: (value) => {
      return (
        value &&
        format(new Date(value), "d MMMM yyyy года", {
          locale: ru,
        })
      );
    },
  },
};
</script>

<style scoped>
.title-container {
  font-size: 40px;
  margin-bottom: 10px;
}

.text-color-silver {
  color: #909399;
}

.text-container {
  padding: 10px;
}

.text-description-company {
  margin-top: 4px;
}

.edit-link-floating-button {
  position: absolute;
  right: 40px;
  bottom: 40px;
}
</style>
