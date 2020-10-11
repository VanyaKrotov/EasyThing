<template>
  <div class="container" v-loading="isEditForm && isLoadingCompany">
    <AuthenticationError v-if="!isAuthenticated" />
    <el-form
      v-else
      status-icon
      label-position="top"
      ref="companyEdit"
      :disable="isLoadingCompany"
      label-width="100px"
      :model="formData"
    >
      <h2 class="title">
        <span v-if="isEditForm">Редактирование компании</span>
        <span v-else>Создание компании</span>
        <span v-if="formData.title">: "{{ formData.title }}"</span>
        <el-popconfirm
          v-if="isEditForm"
          confirmButtonText="Да"
          cancelButtonText="Нет"
          icon="el-icon-info"
          iconColor="red"
          @onConfirm="handlerDelete"
          title="Вы действительно хотите удалить компанию?"
        >
          <el-button
            type="danger"
            slot="reference"
            class="delete-button"
            plain
            circle
            ><i class="el-icon-delete"
          /></el-button>
        </el-popconfirm>
      </h2>

      <el-form-item
        label="Название компании:"
        prop="title"
        :rules="[
          {
            required: true,
            trim: true,
            message: 'Название компании не может быть пустым',
            trigger: 'blur'
          }
        ]"
      >
        <el-input v-model="formData.title" name="title" />
      </el-form-item>
      <el-form-item
        label="Электронная почта:"
        prop="email"
        :rules="[
          {
            required: true,
            message: 'Электронная почта должна быть указана',
            trigger: 'blur'
          },
          {
            type: 'email',
            message: 'Электронная почта неккоректна',
            trigger: 'blur'
          }
        ]"
      >
        <el-input v-model="formData.email" name="email" />
      </el-form-item>
      <el-form-item label="Дата основания компании:" prop="dateCreated">
        <el-date-picker
          v-model="formData.dateCreated"
          type="date"
          name="dateCreated"
          placeholder="Выберите дату основания"
        >
        </el-date-picker>
      </el-form-item>
      <el-form-item label="Расположение компании:" prop="location">
        <div class="container-map">
          <yandex-map :coords="arrayCoords" :zoom="10" @click="changeLocation">
            <ymap-marker
              :coords="arrayCoords"
              marker-id="123"
              :hint-content="formData.title"
            >
              <!--  <i class="el-icon-location-information" slot="balloon">{{
                formData.title
              }}</i> -->
            </ymap-marker>
          </yandex-map>
        </div>
      </el-form-item>
      <el-form-item
        label="Описание компании:"
        prop="description"
        :rules="[
          {
            required: true,
            message: 'Описание компании должно быть заполнено',
            trigger: 'blur'
          }
        ]"
      >
        <vue-editor v-model="formData.description" name="description" />
      </el-form-item>
      <el-form-item class="buttons-control">
        <el-button
          type="primary"
          @click="submitForm"
          :loading="isLoadingCompany"
          >Сохранить</el-button
        >
        <el-button @click="cancelHandler">Отменить</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex';
import { Coords } from '../../objects';
import { defaultCompany } from '../../store/models/company';
import AuthenticationError from '../ConfirmPages/AuthenticationError';

export default {
  name: 'Edit',
  components: {
    AuthenticationError
  },
  data() {
    return {
      isEditForm: false,
      formData: { ...defaultCompany }
    };
  },
  computed: {
    ...mapGetters(['getCompanyValues', 'isLoadingCompany', 'isAuthenticated']),
    arrayCoords: ({
      formData: {
        location: { coords: { latitude = 0.0, longitude = 0.0 } = {} } = {}
      } = {}
    }) => [latitude, longitude]
  },
  methods: {
    ...mapMutations(['setStatusLoading']),
    ...mapActions([
      'createCompany',
      'deleteCompany',
      'editCompany',
      'fetchCompany'
    ]),

    /* async checkAdress(pos) {
      const response = await fetch(
        `http://geocode-maps.yandex.ru/1.x/?geocode=${pos[1]},${pos[0]}&format=json&apikey=6eae48fe-cd83-408a-a2e5-c11bb62da1cf`
      );

      return await response.json();
    }, */
    async changeLocation(e) {
      const coords = e.get('coords');

      this.formData.location.coords = new Coords({
        latitude: coords[0],
        longitude: coords[1]
      });
      /* const {
        response: {
          GeoObjectCollection: { featureMember }
        }
      } = await this.checkAdress(this.formData.location);
      this.formData.locationName =
        featureMember[0].GeoObject.metaDataProperty.GeocoderMetaData.text; */
    },
    async submitForm() {
      this.$refs['companyEdit'].validate((valid) => {
        if (valid) {
          const serviceObject = {
            setMessage: this.$message,
            companyData: this.formData,
            router: this.$router
          };

          if (this.isEditForm) {
            this.editCompany(serviceObject);
          } else {
            this.createCompany(serviceObject);
          }

          return true;
        }

        return false;
      });
    },
    cancelHandler() {
      this.$confirm(
        'Все несохраненные данные будут потеряны. Продолжить?',
        `Отмена ${this.isEditForm ? 'редактирования' : 'сохранения'}`,
        {
          confirmButtonText: 'Да',
          cancelButtonText: 'Отменить',
          type: 'warning'
        }
      )
        .then(() => {
          this.$router.go(-1);
        })
        .catch(() => {});
    },
    handlerDelete() {
      this.deleteCompany({
        setMessage: this.$message,
        id: this.formData.id,
        router: this.$router
      });
    }
  },
  async mounted() {
    const companyId = this.$route.params.id || 0;

    this.isEditForm = Boolean(companyId);

    if (this.isEditForm) {
      await this.fetchCompany({ companyId });

      this.formData = this.getCompanyValues;
    } else {
      navigator.geolocation.getCurrentPosition(
        ({ coords: { latitude, longitude } }) => {
          this.formData.location.coords = new Coords({
            latitude,
            longitude
          });
        }
      );
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 1000px;
  margin: 10px auto;
}

h2 {
  text-align: left;
  position: relative;
}

.delete-button {
  position: absolute;
  right: 0px;
}

.buttons-control {
  text-align: center;
}

.title {
  color: var(--primary_text);
}
</style>
