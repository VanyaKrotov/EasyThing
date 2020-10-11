<template>
  <div v-loading="isLoadingNews">
    <el-drawer
      destroy-on-close
      :title="editPostId == -1 ? 'Создание поста' : 'Редактирование поста'"
      :visible.sync="isVisibleEditForm"
      direction="ttb"
      size="100%"
      ref="newsEditFormDrawer"
    >
      <NewsEditForm
        :postId="editPostId"
        :news="companyNews"
        :createCompanyNews="createCompanyNewsHandle"
        :editCompanyNews="editCompanyNewsHandle"
        :companyId="companyId"
        :closeForm="closeForm"
      />
    </el-drawer>
    <el-row v-if="companyNews.length === 0">
      <h2
        class="text-center"
        style="color: var(--primary_text); margin: 100px 0px;"
      >
        Нет постов
      </h2>
    </el-row>
    <el-row :gutter="20" class="mtb1" v-else>
      <NewsCard
        v-for="post in companyNews"
        :post="post"
        :onEdinPost="() => onEdinPost(post.id)"
        :onDeletePost="() => onDeletePost(post.id)"
        :onChangeLike="() => onChangeLike(post.id)"
        :key="`post-${post.id}`"
      />
    </el-row>
    <div class="fixed-button-right_bottom" style="right: 90px;">
      <el-tooltip content="Создать пост" placement="top-end">
        <el-button type="primary" circle @click="isVisibleEditForm = true">
          <i class="el-icon-plus" />
        </el-button>
      </el-tooltip>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import NewsCard from './Components/NewsCard';
import NewsEditForm from './Components/NewsEditForm';

export default {
  name: 'Feed',
  components: {
    NewsCard,
    NewsEditForm
  },
  data() {
    return {
      isVisibleEditForm: false,
      editPostId: null
    };
  },
  computed: {
    ...mapGetters(['getCompanyValues', 'isLoadingNews']),
    companyNews: ({ getCompanyValues = {} }) =>
      (getCompanyValues.news || []).sort((firstNews, nextNews) =>
        new Date(firstNews.dateCreate) < new Date(nextNews.dateCreate) ? 1 : -1
      ),
    companyId: ({ getCompanyValues = {} }) => getCompanyValues.id
  },
  methods: {
    ...mapActions([
      'createCompanyNews',
      'deleteCompanyNews',
      'editCompanyNews',
      'changeLikeCompanyNews'
    ]),
    prepeaDataToSend(sendData) {
      return {
        setMessage: this.$message,
        closeForm: this.closeForm.bind(this),
        ...sendData
      };
    },
    createCompanyNewsHandle(sendData) {
      this.createCompanyNews(this.prepeaDataToSend(sendData));
    },
    editCompanyNewsHandle(sendData) {
      this.editCompanyNews(this.prepeaDataToSend(sendData));
    },
    closeForm() {
      this.$refs.newsEditFormDrawer.closeDrawer();

      this.editPostId = null;
    },
    onEdinPost(editPostId) {
      this.editPostId = editPostId;
      this.isVisibleEditForm = true;
    },
    onDeletePost(postId) {
      this.deleteCompanyNews({
        postId,
        companyId: this.companyId,
        setMessage: this.$message
      });
    },
    onChangeLike(postId) {
      this.changeLikeCompanyNews({
        setMessage: this.$message,
        postId,
        companyId: this.companyId
      });
    }
  }
};
</script>
