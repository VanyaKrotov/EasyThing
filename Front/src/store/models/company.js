import {
  getRequest,
  postRequest,
  deleteRequest,
  putRequest,
} from ".././../request-methods";
import { format } from "date-fns";

const defaultCompany = {
  title: "",
  email: "",
  description: "",
  dateCreated: new Date(),
  location: [0, 0],
};

export default {
  actions: {
    async fetchAllCompanies(context) {
      try {
        const { companies } = await getRequest({
          url: `api/v1/Company/Companies/`,
        });

        context.commit("setCompanies", companies);
      } catch (error) {
        console.error(error);
      }
    },
    async fetchCompany(context, { companyId }) {
      context.commit("setFormState", true);
      context.commit("setCompany", { ...defaultCompany });

      try {
        const { company } = await getRequest({
          url: `api/v1/Company/${companyId}/`,
        });

        context.commit("setCompany", {
          ...company,
          location: JSON.parse(company.location),
        });
      } catch (error) {
        console.error(error);
      }

      context.commit("setFormState", false);
    },
    async createCompany(context, { setMessage, router }) {
      context.commit("setFormState", true);

      try {
        const companyData = context.state.company;
        console.log(companyData)
        const { id } = await postRequest({
          url: "api/v1/Company/Create/",
          data: {
            ...companyData,
            location: JSON.stringify(companyData.location),
            master: context.rootState.user.user.id,
            dateCreated: format(
              new Date(companyData.dateCreated),
              "yyyy-MM-dd"
            ),
            dateRegistration: format(new Date(), "yyyy-MM-dd"),
          },
        });

        router.push({ path: `/company/${id}/feed` });

        setMessage({
          message: "Компания успешно создана",
          type: "success",
        });
      } catch (error) {
        setMessage({
          message: error,
          type: "error",
        });
        console.error(error);
      }

      context.commit("setFormState", false);
    },
    async editCompany(context, { setMessage, router }) {
      context.commit("setFormState", true);

      try {
        const companyData = context.state.company;
        const { id } = await putRequest({
          url: `api/v1/Company/Edit/${companyData.id}/`,
          data: {
            ...companyData,
            dateCreated: format(
              new Date(companyData.dateCreated),
              "yyyy-MM-dd"
            ),
            location: JSON.stringify(companyData.location),
          },
        });

        router.push({ path: `/company/${id}/feed` });

        setMessage({
          message: "Компания успешно отредактирована",
          type: "success",
        });
      } catch (error) {
        setMessage({
          message: error,
          type: "error",
        });
        console.error(error);
      }

      context.commit("setFormState", false);
    },
    async deleteCompany(context, { router, id, setMessage }) {
      try {
        await deleteRequest({
          url: `api/v1/Company/Delete/${id}/`,
        });

        router.push({ path: "/companies" });
        setMessage({
          message: "Компания успешно удалена",
          type: "success",
        });
      } catch (error) {
        setMessage({
          message: error,
          type: "error",
        });
        console.error(error);
      }
    },
  },
  mutations: {
    setCompanies(state, companiesList) {
      state.companiesList = companiesList;
    },
    setCompany(state, company) {
      state.company = company;
    },
    setFormState(state, formState) {
      state.isFormSubmitting = formState;
    },
  },
  state: {
    companiesList: [],
    company: { ...defaultCompany },
    isFormSubmitting: false,
  },
  getters: {
    getAllCompanies(state) {
      return state.companiesList;
    },
    getCompanyValues: (state) => {
      return state.company;
    },
    getFormState(state) {
      return state.isFormSubmitting;
    },
  },
};
