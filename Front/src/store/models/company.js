import {
  getRequest,
  postRequest,
  deleteRequest,
  putRequest,
} from ".././../request-methods";
import { format } from "date-fns";

export const defaultCompany = {
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

      try {
        const { company } = await getRequest({
          url: `api/v1/Company/${companyId}/`,
        });

        const newCompanies = [
          {
            ...company,
            location: JSON.parse(company.location),
          },
        ];

        context.commit("setCompanies", newCompanies);
      } catch (error) {
        console.error(error);
      }

      context.state.isFetching = false;
    },
    async createCompany(context, { setMessage, router, companyData }) {
      context.state.isFetching = true;

      try {
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
    async editCompany(context, { setMessage, router, companyData }) {
      context.state.isFetching = true;

      try {
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
    setCompanies(state, companies) {
      state.companies = companies;
    },
  },
  state: {
    isFetching: false,
    companies: [],
  },
  getters: {
    getAllCompanies: ({ companies }) => companies,
    getCompanyValues: ({ companies }) => companies[0],
    isLoadingCompany: ({ isFetching }) => isFetching,
  },
};
