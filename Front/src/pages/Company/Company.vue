<template>
  <div v-loading="isLoadingCompany">
    <el-row style="padding-bottom: 50px" v-if="getCompanyValues">
      <div class="company-title-bunner">
        <div class="mg20">{{ getCompanyValues.title }}</div>
        <div class="text-center">
          <el-image
            style="width: 100px; height: 100px"
            :src="getLogoPath"
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
        :default-active="defaultMenuRoute"
        mode="horizontal"
        active-text-color="#409EFF"
        :router="true"
      >
        <el-menu-item index="feed">
          Лента
        </el-menu-item>
        <el-menu-item index="services">
          Предприятия
        </el-menu-item>
        <el-menu-item index="workers">
          Сотрудники
        </el-menu-item>
        <el-menu-item index="schedule">
          Графики
        </el-menu-item>
        <el-menu-item index="settings">
          Настройки
        </el-menu-item>
        <el-menu-item index="about">
          О компании
        </el-menu-item>
      </el-menu>
    </el-row>
    <router-view></router-view>
    <div class="edit-link-floating-button">
      <router-link to="edit" class="link-item">
        <el-button type="primary" circle icon="el-icon-edit" />
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import { getImageUrl } from '../../request-methods';
import { ru } from 'date-fns/locale';
import { format } from 'date-fns';

export default {
  name: 'Company',
  computed: {
    ...mapGetters(['getCompanyValues', 'isLoadingCompany']),
    companyId: ({ getCompanyValues = {} }) => getCompanyValues.id,
    defaultMenuRoute() {
      const parseRoute = this.$route.fullPath.split('/');

      return parseRoute[parseRoute.length - 1];
    },
    getLogoPath: ({ getCompanyValues = {} }) =>
      getImageUrl(getCompanyValues.logo)
  },
  methods: {
    ...mapActions(['fetchCompany'])
  },
  async mounted() {
    const companyId = this.$route.params.id || 0;
    this.fetchCompany({ companyId });
  },
  filters: {
    dateCreateFilter: (value) => {
      return (
        value &&
        format(new Date(value), 'd MMMM yyyy года', {
          locale: ru
        })
      );
    }
  }
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
