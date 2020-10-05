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
      context.state.isFetching = true;

      try {
        const { companies } = await getRequest({
          url: `api/v1/Company/Companies/`,
        });

        context.commit("setCompanies", companies);
      } catch (error) {
        console.error(error);
      }

      context.state.isFetching = false;
    },
    async fetchCompany(context, { companyId }) {
      context.state.isFetching = true;
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

      context.state.isFetching = false;
    },
    async createCompany(context, { setMessage, router }) {
      context.state.isFetching = true;

      try {
        const companyData = context.state.company;
        console.log(companyData);
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

      context.state.isFetching = false;
    },
    async editCompany(context, { setMessage, router }) {
      context.state.isFetching = true;

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

      context.state.isFetching = false;
    },
    async deleteCompany(context, { router, id, setMessage }) {
      context.state.isFetching = true;

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

      context.state.isFetching = false;
    },
  },
  mutations: {
    setCompanies(state, companiesList) {
      state.companiesList = companiesList;
      state.isFetching = false;
    },
    setCompany(state, company) {
      state.company = company;
    },
  },
  state: {
    isFetching: false,
    companiesList: [],
    company: { ...defaultCompany },
  },
  getters: {
    getAllCompanies: ({ companiesList }) => companiesList,
    getCompanyValues: ({ company }) => company,
    isLoadingCompany: ({ isFetching }) => isFetching,
  },
};
