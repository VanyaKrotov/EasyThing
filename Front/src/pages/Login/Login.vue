<template>
  <div class="root-control">
    <div class="side">
      <div class="side-label">
        <span>Вход в аккаунт</span>
      </div>
      <div class="side-form">
        <div class="form-container">
          <el-form
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
              <el-button
                :loading="isLoadingUser"
                type="primary"
                @click="submitForm('formValues')"
                submit
                >Войти</el-button
              >
            </el-form-item>
          </el-form>
        </div>
      </div>
      <div class="side-additionally">
        <span>
          <router-link to="/FargonPassword" class="link-item">
            <el-button type="text">Забыли пароль?</el-button>
          </router-link>
          <router-link to="/Registration" class="link-item">
            <el-button type="text">Регистрация</el-button>
          </router-link>
        </span>
      </div>
    </div>
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
    ...mapGetters(["isAuthenticated", "isLoadingUser"]),
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

.root-control {
  width: 400px;
  height: 600px;
  display: flex;
  justify-self: center;
  margin: 50px auto;
}

.side {
  width: 100%;
  height: 100%;
}

img {
  max-width: 100%;
  margin: 82px 0px;
}

.side > div {
  width: 100%;
}

.side-label span {
  color: #409eff;
  padding: 12%;
  font-size: 24px;
  font-weight: normal;
  line-height: 24px;
  display: inline-block;
  text-align: center;
  width: 76%;
}

.side-label {
  height: 20%;
}

.side-form {
  height: 67%;
}

.side-additionally {
  height: 10%;
  text-align: center;
}

.form-container {
  margin: 20px;
}

.side-additionally span {
  margin: 14px;
}

.side-additionally span a {
  margin: 5px;
}
</style>
