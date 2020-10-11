<template>
  <div class="container" v-loading="isEditForm && isLoadingService">
    <AuthenticationError v-if="!isAuthenticated" />
    <el-form
      v-else
      status-icon
      label-position="top"
      ref="companyEdit"
      :disable="isLoadingService"
      label-width="100px"
      :model="formValues"
    >
      <h2 class="title">
        <span v-if="isEditForm">Редактирование предприятие</span>
        <span v-else>Создание предприятие</span>
        <span v-if="formValues.title"> - {{ formValues.title }}</span>
        <el-popconfirm
          v-if="isEditForm"
          confirmButtonText="Да"
          cancelButtonText="Нет"
          icon="el-icon-info"
          iconColor="red"
          @onConfirm="handlerDelete"
          title="Вы действительно хотите удалить данное предприятие?"
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
        label="Название предприятия:"
        prop="title"
        :rules="[
          {
            required: true,
            trim: true,
            message: 'Название не может быть пустым',
            trigger: 'blur'
          }
        ]"
      >
        <el-input v-model="formValues.title" name="title" />
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
        <el-input v-model="formValues.email" name="email" />
      </el-form-item>
      <el-form-item label="Дата создания:" prop="dateCreated">
        <el-date-picker
          v-model="formValues.dateCreated"
          type="date"
          name="dateCreated"
          placeholder="Выберите дату создания"
        >
        </el-date-picker>
      </el-form-item>

      <el-form-item label="Модули предприятия:" prop="types">
        <el-select v-model="formValues.types" multiple placeholder="Модули">
          <el-option
            v-for="type in typeOptions"
            :key="type"
            :label="type"
            :value="type"
          >
          </el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="Режим работы:" prop="workShedudle">
        <el-select v-model="formValues.workShedudle" placeholder="Рассписание">
          <el-option
            v-for="workShedudle in workShedudleOptions"
            :key="workShedudle"
            :value="workShedudle"
            :label="workShedudle"
          />
        </el-select>
        <el-button circle type="text" v-if="formValues.workShedudle">
          <i class="el-icon-info" />
        </el-button>
        <el-button
          style="margin: 0px 10px;"
          size="mini"
          circle
          type="primary"
          plain
          ><i class="el-icon-plus"
        /></el-button>
      </el-form-item>

      <el-form-item label="Расположение компании:" prop="location">
        <div class="container-map">
          <yandex-map :coords="arrayCoords" :zoom="10" @click="changeLocation">
            <ymap-marker
              :coords="arrayCoords"
              marker-id="123"
              :hint-content="formValues.title"
            >
              <!--  <i class="el-icon-location-information" slot="balloon">{{
                formValues.title
              }}</i> -->
            </ymap-marker>
          </yandex-map>
        </div>
      </el-form-item>
      <el-form-item
        label="Описание:"
        prop="description"
        :rules="[
          {
            required: true,
            message: 'Описание должно быть заполнено',
            trigger: 'blur'
          }
        ]"
      >
        <vue-editor v-model="formValues.description" name="description" />
      </el-form-item>
      <el-form-item class="buttons-control">
        <el-button
          type="primary"
          @click="submitForm"
          :loading="isLoadingService"
          >Сохранить</el-button
        >
        <el-button @click="cancelHandler">Отменить</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import { defaultService } from '../../../store/models/service';
import { Coords } from '../../../objects';
import AuthenticationError from '../../ConfirmPages/AuthenticationError';

export default {
  name: 'EditService',
  data: () => ({
    isEditForm: false,
    formValues: { ...defaultService }
  }),
  components: {
    AuthenticationError
  },
  computed: {
    ...mapGetters([
      'serviceData',
      'isLoadingService',
      'isAuthenticated',
      'serviceTypeData',
      'workShedudlesData'
    ]),
    arrayCoords: ({
      formValues: {
        location: { coords: { latitude = 0.0, longitude = 0.0 } = {} } = {}
      } = {}
    }) => [latitude, longitude],
    typeOptions: ({ serviceTypeData = [] }) =>
      serviceTypeData.map(({ title = '' }) => title),
    workShedudleOptions: ({ workShedudlesData = [] }) =>
      workShedudlesData.map(({ title }) => title)
  },
  methods: {
    ...mapActions(['fetchServiceById']),
    handlerDelete() {},
    cancelHandler() {},
    submitForm() {},
    async changeLocation(e) {
      const coords = e.get('coords');

      this.formValues.location.coords = new Coords({
        latitude: coords[0],
        longitude: coords[1]
      });
    }
  },
  async mounted() {
    const serviceId = this.$route.params.id || 0;

    this.isEditForm = Boolean(serviceId);

    if (this.isEditForm) {
      await this.fetchServiceById({ setMessage: this.$message, serviceId });

      const serviceData = this.serviceData;

      const serviceTypes = this.serviceTypeData;
      serviceData.types = serviceData.types.map((typeId) => {
        const findType = serviceTypes.find(({ id }) => typeId === id);

        return findType ? findType.title : '';
      });

      this.formValues = serviceData;
    }

    navigator.geolocation.getCurrentPosition(
      ({ coords: { latitude, longitude } }) => {
        this.formValues.location.coords = new Coords({
          latitude,
          longitude
        });
      }
    );

    console.log(this.formValues.location);
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
</style>
