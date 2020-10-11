import { postRequest, getRequest } from '.././../request-methods';

export default {
  actions: {
    async loginUser(context, { data, message, router }) {
      context.state.isFetching = true;

      try {
        const { user } = await postRequest({
          url: 'api/v1/User/Login/',
          data
        });
        context.commit('setUserInformation', user);
        router.go(-1);
      } catch (detail) {
        console.error(detail);
        message({
          message: detail,
          type: 'error'
        });
      }

      context.state.isFetching = false;
    },
    async authUser(context) {
      context.state.isFetching = true;

      try {
        const { user } = await getRequest({
          url: 'api/v1/User/Auth/'
        });

        context.commit('setUserInformation', user);
      } catch (detail) {
        console.error(detail);
      }

      context.state.isFetching = false;
    },
    async logoutUser(context) {
      context.state.isFetching = true;

      try {
        await getRequest({
          url: 'api/v1/User/Logout/'
        });

        context.commit('setUserInformation', null);
        context.commit('setCompanies', []);
      } catch (detail) {
        console.error(detail);
      }

      context.state.isFetching = false;
    }
  },
  mutations: {
    setUserInformation(state, information) {
      state.user = information;
      state.isFetching = false;
    }
  },
  state: {
    isFetching: false,
    user: null
  },
  getters: {
    isAuthenticated: ({ user }) => Boolean(user),
    getUserInformation: ({ user }) => user,
    userId: ({ user }) => (user || {}).id,
    isLoadingUser: ({ isFetching }) => isFetching
  }
};
