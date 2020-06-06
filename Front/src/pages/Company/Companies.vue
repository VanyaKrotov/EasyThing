<template>
  <div>
    <AuthenticationError v-if="!isAuthenticated" />
    <el-row class="" v-else-if="getAllCompaniesSorted.length > 0">
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="">
        <el-row>
          <el-col :xs="24" :sm="6" :md="8" :lg="6" :xl="4">
            <span class="page-title">
              Ваши компании:
            </span>
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
              <el-select
                v-model="settingsControl.viewValue"
                placeholder="Тип отображения"
              >
                <el-option label="Карточки" :value="0" />
                <el-option label="Список" :value="1" />
              </el-select>
            </span>
            <span class="mlr1">
              <el-tooltip
                class="item"
                effect="dark"
                content="Перейти к настройкам компаний"
                placement="bottom-end"
              >
                <el-button icon="el-icon-s-operation" />
              </el-tooltip>
              {{ " " }}
              <router-link :to="`/company/create`">
                <el-tooltip
                  class="item"
                  effect="dark"
                  content="Создать компанию"
                  placement="bottom-end"
                >
                  <el-button icon="el-icon-plus" />
                </el-tooltip>
              </router-link>
            </span>
          </el-col>
        </el-row>
      </el-col>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="">
        <el-row :gutter="20" v-if="settingsControl.viewValue === 0">
          <el-col
            v-for="{
              title,
              id,
              countServices,
              dateCreated,
            } in getAllCompaniesSorted"
            :span="20"
            class="mtb1"
            :xs="24"
            :sm="12"
            :md="12"
            :lg="8"
            :xl="8"
            :key="`company-${id}`"
          >
            <router-link :to="`/company/${id}/feed`">
              <el-card
                :body-style="{ padding: '0px', cursor: 'pointer' }"
                shadow="hover"
              >
                <img
                  src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                  class="image"
                />
                <div style="padding: 14px;">
                  <span>{{ title }}</span>
                  <div class="bottom clearfix">
                    <time class="time"
                      >Дата основания:
                      {{ dateCreated | dateCreateFilter }}</time
                    >
                    <div class="time">Предприятий: {{ countServices }}</div>
                    <!-- <el-button type="text" class="button">Настройки</el-button> -->
                  </div>
                </div>
              </el-card>
            </router-link>
          </el-col>
        </el-row>
        <el-row :gutter="20" v-else class="mtb1">
          <el-col
            :xs="24"
            :sm="24"
            :md="24"
            :lg="24"
            :xl="24"
            :span="10"
            class="mtb05"
            v-for="{
              title,
              id,
              email,
              location,
              dateRegistration,
              dateCreated,
            } in getAllCompaniesSorted"
            :key="`company-${id}`"
          >
            <el-card shadow="hover">
              <el-row :gutter="20">
                <el-col :xs="10" :sm="7" :md="7" :lg="11" :xl="12">
                  <router-link :to="`/company/${id}/feed`">
                    <el-button type="text" icon="el-icon-top-right">{{
                      title
                    }}</el-button>
                  </router-link>
                </el-col>
                <el-col :xs="8" :sm="6" :md="6" :lg="5" :xl="5">
                  <div class="time">{{ email }}</div>
                  <!-- <div class="time">{{ location }}</div> -->
                </el-col>
                <el-col :xs="0" :sm="7" :md="7" :lg="6" :xl="5">
                  <div class="time">
                    Основана: {{ dateCreated | dateCreateFilter }}
                  </div>
                  <div class="time">
                    Зарегистрирована: {{ dateRegistration | dateCreateFilter }}
                  </div>
                </el-col>
                <el-col :xs="6" :sm="4" :md="4" :lg="2" :xl="1">
                  <div>
                    <router-link :to="`/company/${id}/settings`">
                      <el-button
                        type="text"
                        style="font-size: 12px;"
                        icon="el-icon-s-operation"
                        >Настройки</el-button
                      >
                    </router-link>
                  </div>
                  <div>
                    <router-link :to="`/company/${id}/edit`">
                      <el-button
                        type="text"
                        style="font-size: 12px;"
                        icon="el-icon-edit"
                        >Редактировать</el-button
                      >
                    </router-link>
                  </div>
                </el-col>
              </el-row>
            </el-card>
          </el-col>
        </el-row>
      </el-col>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class=""></el-col>
    </el-row>
    <CompaniesIsEmpty v-else />
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
        viewValue: 1,
        sortedValue: 0,
      },
    };
  },
  computed: {
    ...mapGetters(["getAllCompanies", "isAuthenticated"]),
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
  color: #303133;
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
