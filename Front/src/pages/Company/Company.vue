<template>
  <div>
    <el-row style="padding-bottom: 50px">
      <div class="company-title-bunner">
        <div class="mg20">{{ getCompanyValues.title }}</div>
        <div class="text-center">
          <el-image
            style="width: 100px; height: 100px"
            src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4aff544c0c25941171jpeg.jpeg"
            fit="fill"
          >
            <div slot="error" style="width: 100px; height: 100px">
              <div class="error-logo-company">LOGO</div>
            </div>
          </el-image>
        </div>
      </div>
    </el-row>
    <el-row>
      <el-menu
        :default-active="$route.fullPath"
        mode="horizontal"
        active-text-color="#409EFF"
        @select="(path) => $router.push(path)"
      >
        <el-menu-item :index="`/company/${getCompanyValues.id}/about`">
          О компании
        </el-menu-item>
        <el-menu-item :index="`/company/${getCompanyValues.id}/feed`">
          Общее
        </el-menu-item>
        <el-menu-item :index="`/company/${getCompanyValues.id}/services`">
          Предприятия
        </el-menu-item>
        <el-menu-item :index="`/company/${getCompanyValues.id}/workers`">
          Сотрудники
        </el-menu-item>
        <el-menu-item :index="`/company/${getCompanyValues.id}/schedule`">
          Графики
        </el-menu-item>
        <el-menu-item :index="`/company/${getCompanyValues.id}/settings`">
          Настройки
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
.company-title-bunner {
  width: 100%;
  height: 150px;
  border: solid 1px #e6e6e6;
  color: var(--primary_text);
  text-align: center;
  position: relative;
}

.error-logo-company {
  width: 98%;
  height: 98%;
  background: #f5f7fa;
  color: #c0c4cc;
  padding: 37px 0px;
}

.company-title-bunner > div:first-child {
  font-size: 36px;
}

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
