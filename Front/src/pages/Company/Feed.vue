<template>
  <div>
    <el-drawer
      title="Рдактирование поста"
      :visible.sync="isVisibleEditForm"
      direction="ttb"
      :before-close="handleClose"
      size="100%"
    >
    </el-drawer>
    <div>
      Новости:
      <el-button @click="isVisibleEditForm = true">Edit Post</el-button>
    </div>
    <ul>
      <li :key="index" v-for="(item, index) in getCompanyValues.news">
        <span>{{ item.title }} <el-button></el-button></span>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Feed",
  data() {
    return {
      isVisibleEditForm: false,
      editPostIndex: -1,
    };
  },
  computed: {
    ...mapGetters(["getCompanyValues"]),
  },
  methods: {
    handleClose(done) {
      done();
    },
  },
};
</script>
