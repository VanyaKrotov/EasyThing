<template>
  <el-col
    :xs="24"
    :sm="24"
    :md="12"
    :lg="12"
    :xl="8"
    :span="10"
    class="mtb05"
    :key="`service-${service.id}`"
  >
    <el-card shadow="hover">
      <el-row :gutter="20">
        <el-col :xs="18" :sm="20" :md="20" :lg="22" :xl="22">
          <router-link :to="`/service/${service.id}/feed`">
            <el-button type="text">{{ service.title }}</el-button>
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
          <el-dropdown @command="(link) => $router.push(link)" trigger="click">
            <el-button type="text" class="s_20x20">
              <i class="el-icon-more-outline" />
            </el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item :command="`/service/${service.id}/settings`"
                >Настройки</el-dropdown-item
              >
              <el-dropdown-item :command="`/service/${service.id}/edit`"
                >Редактировать</el-dropdown-item
              >
            </el-dropdown-menu>
          </el-dropdown>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs="6" :sm="4" :md="4" :lg="2" :xl="1" class="time">
          {{ service.email }}
        </el-col>
      </el-row>
    </el-card>
  </el-col>
</template>

<script>
export default {
  name: 'ServiceCard',
  props: ['service']
};
</script>

<style scoped></style>
