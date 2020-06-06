<template>
  <div class="container">
    <div v-if="isAuthenticated" style="text-align: center;">
      <el-button type="danger" plain @click="logoutUser">Выйти</el-button>
    </div>
    <el-form
      v-else
      status-icon
      label-position="top"
      ref="formValues"
      label-width="100px"
      :model="formValues"
      class="demo-dynamic"
    >
      <el-form-item
        label="Электронная почта"
        prop="username"
        :rules="[
          {
            required: true,
            message: 'Пожалуйста укажите электронную почту',
            trigger: 'blur',
          },
        ]"
      >
        <el-input
          v-model="formValues.username"
          name="username"
          autocomplete="on"
        />
      </el-form-item>
      <el-form-item
        label="Пароль"
        prop="password"
        :rules="[
          {
            required: true,
            message: 'Пожалуйста заполните поле пароль',
            trigger: 'blur',
          },
          {
            message: 'Недостаточное количество символов',
            min: 8,
            max: 64,
            trigger: ['blur', 'change'],
          },
        ]"
      >
        <el-input
          v-model="formValues.password"
          type="password"
          name="password"
        />
      </el-form-item>
      <el-form-item class="buttons-control">
        <el-button type="primary" @click="submitForm('formValues')" submit
          >Войти</el-button
        >
        <el-tooltip
          class="item"
          effect="dark"
          content="Сбросить данные формы"
          placement="bottom-end"
        >
          <el-button
            :disabled="formValues.username === '' && formValues.password === ''"
            type="primary"
            icon="el-icon-refresh-right"
            @click="formValues = { username: '', password: '' }"
          />
        </el-tooltip>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

const defaultValues = {
  username: "",
  password: "",
};

export default {
  name: "Login",
  data() {
    return {
      formValues: defaultValues,
    };
  },
  beforeDestroy() {
    this.formValues = defaultValues;
  },
  computed: {
    ...mapGetters(["isAuthenticated"]),
  },
  methods: {
    ...mapActions(["loginUser", "logoutUser"]),
    async submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          return this.loginUser({
            data: this.formValues,
            message: this.$message,
            router: this.$router,
          });
        } else {
          return false;
        }
      });
    },
  },
};
</script>

<style scoped>
.buttons-control {
  text-align: center;
}
</style>
