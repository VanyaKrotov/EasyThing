<template>
  <div v-loading="isLoadingCompany">
    <AuthenticationError v-if="!isAuthenticated" />
    <el-row v-else-if="getAllCompaniesSorted.length > 0">
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="">
        <el-row>
          <el-col :xs="24" :sm="6" :md="8" :lg="6" :xl="4">
            <span class="page-title"> Ваши компании: </span>
          </el-col>
          <el-col
            :xs="24"
            :sm="18"
            :md="16"
            :lg="18"
            :xl="20"
            class="settings-controls"
          >
            <span class="mlr1">
              <el-select
                v-model="settingsControl.sortedValue"
                placeholder="Сортировка"
              >
                <el-option label="По названию" :value="0" />
                <el-option label="По дате создания" :value="1" />
                <el-option label="По дате регистрации" :value="2" />
                <el-option label="По количеству предприятий" :value="3" />
              </el-select>
            </span>

            <span class="mlr1">
              <el-tooltip
                class="item"
                effect="dark"
                content="Перейти к настройкам компаний"
                placement="bottom-end"
              >
                <el-button icon="el-icon-s-operation" circle />
              </el-tooltip>
            </span>
          </el-col>
        </el-row>
      </el-col>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="">
        <el-row :gutter="20" class="mtb1">
          <el-col
            :xs="24"
            :sm="24"
            :md="12"
            :lg="12"
            :xl="8"
            :span="10"
            class="mtb05"
            v-for="{ title, id, email } in getAllCompaniesSorted"
            :key="`company-${id}`"
          >
            <el-card shadow="hover">
              <el-row :gutter="20">
                <el-col :xs="18" :sm="20" :md="20" :lg="22" :xl="22">
                  <router-link :to="`/company/${id}/feed`">
                    <el-button type="text">{{ title }}</el-button>
                  </router-link>
                </el-col>
                <el-col
                  :xs="6"
                  :sm="4"
                  :md="4"
                  :lg="2"
                  :xl="2"
                  style="text-align: right"
                >
                  <el-dropdown
                    @command="(link) => $router.push(link)"
                    trigger="click"
                  >
                    <el-button type="text" class="s_20x20">
                      <i class="el-icon-more-outline" />
                    </el-button>
                    <el-dropdown-menu slot="dropdown">
                      <el-dropdown-item :command="`/company/${id}/settings`"
                        >Настройки</el-dropdown-item
                      >
                      <el-dropdown-item :command="`/company/${id}/edit`"
                        >Редактировать</el-dropdown-item
                      >
                    </el-dropdown-menu>
                  </el-dropdown>
                </el-col>
              </el-row>
              <el-row>
                <el-col :xs="6" :sm="4" :md="4" :lg="2" :xl="1" class="time">
                  {{ email }}
                </el-col>
              </el-row>
            </el-card>
          </el-col>
        </el-row>
      </el-col>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class=""></el-col>
    </el-row>
    <CompaniesIsEmpty v-else />
    <div class="fixed-button-right_bottom">
      <router-link :to="`/company/create`">
        <el-tooltip
          class="item"
          effect="dark"
          content="Создать компанию"
          placement="bottom-end"
        >
          <el-button icon="el-icon-plus" circle type="primary" />
        </el-tooltip>
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import { ru } from "date-fns/locale";
import { format } from "date-fns";
import CompaniesIsEmpty from "./CompaniesIsEmpty";
import AuthenticationError from "../ConfirmPages/AuthenticationError";

export default {
  name: "Companies",
  components: {
    AuthenticationError,
    CompaniesIsEmpty,
  },
  data() {
    return {
      settingsControl: {
        sortedValue: 0,
      },
    };
  },
  computed: {
    ...mapGetters(["getAllCompanies", "isAuthenticated", "isLoadingCompany"]),
    getAllCompaniesSorted() {
      return [...this.getAllCompanies].sort((first, next) => {
        switch (this.settingsControl.sortedValue) {
          case 0:
            return first.title > next.title ? 1 : -1;
          case 1:
            return Date.parse(first.dateCreated) - Date.parse(next.dateCreated);
          case 2:
            return (
              Date.parse(first.dateRegistration) -
              Date.parse(next.dateRegistration)
            );
          case 3:
            return next.countServices - first.countServices;
        }
      });
    },
  },
  methods: {
    ...mapActions(["fetchAllCompanies"]),
  },
  mounted() {
    this.fetchAllCompanies(this.$message);
  },
  filters: {
    dateCreateFilter: (value) => {
      return format(new Date(value), "d MMMM yyyy года", {
        locale: ru,
      });
    },
  },
};
</script>

<style scoped>
.mlr1 {
  margin-left: 10px;
  margin-right: 10px;
}

.mtb1 {
  margin-top: 10px;
  margin-bottom: 10px;
}

.mtb05 {
  margin-top: 5px;
  margin-bottom: 5px;
}

.mlr05 {
  margin-left: 5px;
  margin-right: 5px;
}

.settings-controls {
  text-align: right;
}

.page-title {
  font-size: 22px;
  line-height: 2em;
  color: var(--primary_text);
}

.time {
  font-size: 13px;
  color: #999;
  margin-top: 4px;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
</style>
