import { postRequest, getRequest } from ".././../request-methods";

export default {
  actions: {
    async loginUser(context, { data, message, router }) {
      context.rootState.isLoading = true;

      try {
        const { user } = await postRequest({
          url: "api/v1/User/Login/",
          data,
        });
        context.commit("setUserInformation", user);
        router.go(-1);
      } catch (detail) {
        console.error(detail);
        message({
          message: detail,
          type: "error",
        });
      }

      context.rootState.isLoading = false;
    },
    async authUser(context) {
      context.rootState.isLoading = true;

      try {
        const { user } = await getRequest({
          url: "api/v1/User/Auth/",
        });

        context.commit("setUserInformation", user);
      } catch (detail) {
        console.error(detail);
      }

      context.rootState.isLoading = false;
    },
    async logoutUser(context) {
      context.rootState.isLoading = true;

      try {
        await getRequest({
          url: "api/v1/User/Logout/",
        });

        context.commit("setUserInformation", null);
        context.commit("setCompanies", []);
      } catch (detail) {
        console.error(detail);
      }

      context.rootState.isLoading = false;
    },
  },
  mutations: {
    setUserInformation(state, information) {
      state.user = information;
    },
  },
  state: {
    user: null,
  },
  getters: {
    isAuthenticated(state) {
      return Boolean(state.user);
    },
    getUserInformation(state) {
      return state.user;
    },
  },
};
