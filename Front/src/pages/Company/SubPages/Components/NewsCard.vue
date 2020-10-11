<template>
  <el-col :xs="24" :sm="24" :md="24" :lg="12" :xl="12" :span="10" class="mtb05">
    <el-card shadow="hover">
      <el-row :gutter="20">
        <el-col
          :xs="24"
          :sm="24"
          :md="24"
          :lg="24"
          :xl="24"
          class="text-center"
        >
          {{ post.title }}
        </el-col>
      </el-row>
      <el-divider content-position="right">{{ dateCreated }}</el-divider>
      <el-row style="margin: 10px 0px;">
        <el-col
          :xs="24"
          :sm="24"
          :md="24"
          :lg="24"
          :xl="24"
          v-html="post.article"
        />
      </el-row>
      <el-divider content-position="left">
        <el-button type="text" plain round @click="onChangeLike">
          <i :class="`el-icon-star-${isPostHaveMyLike ? 'on' : 'off'}`" />
          {{ post.likes.length }}
        </el-button></el-divider
      >
      <el-row :gutter="20">
        <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="12" class="mtb05">
          <span class="time" style="color: var(--primary_text);">Автор: </span
          ><span class="time">
            <router-link :to="`/${post.author.id}/profile`" class="link-item">
              {{ authorString }}
            </router-link>
          </span>
        </el-col>
        <el-col
          :xs="12"
          :sm="12"
          :md="12"
          :lg="12"
          :xl="12"
          class="text-right"
          v-if="isHaveRuleEditAndDelete"
        >
          <span class="button-edit_delete-container">
            <el-button type="primary" plain circle @click="onEdinPost">
              <i class="el-icon-edit" />
            </el-button>
          </span>

          <span class="button-edit_delete-container">
            <el-popconfirm
              title="Вы действительно хотите удалить данный пост?"
              confirmButtonText="Да"
              cancelButtonText="Нет"
              icon="el-icon-info"
              iconColor="red"
              @onConfirm="onDeletePost"
            >
              <el-button type="danger" plain circle slot="reference">
                <i class="el-icon-delete" />
              </el-button>
            </el-popconfirm>
          </span>
        </el-col>
      </el-row>
    </el-card>
  </el-col>
</template>

<script>
import { format } from 'date-fns';
import { ru } from 'date-fns/locale';
import { mapGetters } from 'vuex';

export default {
  name: 'NewsCard',
  props: ['post', 'onEdinPost', 'onDeletePost', 'onChangeLike'],
  computed: {
    ...mapGetters(['userId']),
    authorString: ({ post = {} }) =>
      `${post.author.last_name} ${post.author.first_name}`,
    dateCreated: ({ post = {} }) =>
      format(new Date(post.dateCreate), 'd MMMM yyyy года в HH:mm:ss', {
        locale: ru
      }),
    postId: ({ post = {} }) => post.id,
    isPostHaveMyLike: ({ post = {}, userId }) =>
      (post.likes || []).includes(userId),
    isHaveRuleEditAndDelete: ({ post = {}, userId }) =>
      post.author.id === userId
  }
};
</script>

<style scoped>
.button-edit_delete-container {
  margin: 0px 5px;
  display: inline-block;
}
</style>
