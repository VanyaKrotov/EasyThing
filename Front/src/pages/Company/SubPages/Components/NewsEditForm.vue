<template>
  <div style="margin: 0px 20px;">
    <el-form
      status-icon
      label-position="top"
      ref="newsForm"
      label-width="100px"
      :model="formValues"
      class="demo-dynamic"
    >
      <el-form-item
        label="Заголовок"
        prop="title"
        :rules="[
          {
            required: true,
            message: 'Заголовок должен быть указан',
            trigger: 'blur'
          }
        ]"
      >
        <el-input v-model="formValues.title" name="title" />
      </el-form-item>

      <el-form-item
        label="Содержание поста"
        prop="article"
        :rules="[
          {
            required: true,
            message: 'Поле должно быть заполнено',
            trigger: 'blur'
          }
        ]"
      >
        <vue-editor v-model="formValues.article" name="article" />
      </el-form-item>

      <el-form-item label="Публикация видна" prop="permissions">
        <el-select v-model="formValues.permissions" name="permissions">
          <el-option v-for="option in options" :key="option" :value="option">{{
            option
          }}</el-option>
        </el-select>
      </el-form-item>

      <el-form-item class="buttons-control">
        <el-button
          type="primary"
          @click="submitForm"
          submit
          :loading="isLoadingNews"
          >Сохранить</el-button
        >
        <el-button type="info" plain @click="closeForm">Отмена</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { permissionsVariants } from '../../../../store/models/company';

const permissionLabels = Object.keys(permissionsVariants);

export default {
  name: 'NewsEditForm',
  props: [
    'postId',
    'news',
    'createCompanyNews',
    'companyId',
    'editCompanyNews',
    'closeForm'
  ],
  data() {
    return {
      options: permissionLabels,
      formValues: {
        title: '',
        article: '',
        permissions: 'Всем'
      }
    };
  },
  computed: {
    ...mapGetters(['getUserInformation', 'isLoadingNews']),
    isEditForm: ({ postId }) => Boolean(postId)
  },
  methods: {
    async submitForm() {
      this.$refs['newsForm'].validate((valid) => {
        if (valid) {
          const resultObject = {
            postValues: {
              ...this.formValues,
              id: this.postId,
              author: this.getUserInformation.id,
              company: this.companyId
            }
          };

          if (this.isEditForm) {
            this.editCompanyNews(resultObject);
          } else {
            this.createCompanyNews(resultObject);
          }

          return true;
        }

        return false;
      });
    }
  },
  mounted() {
    if (this.isEditForm) {
      const { title, article, permissions } =
        this.news.find((post) => post.id === this.postId) || {};

      this.formValues = {
        title,
        article,
        permissions: permissionLabels.find(
          (label) => permissionsVariants[label] == permissions
        )
      };
    }
  }
};
</script>

<style scoped></style>
