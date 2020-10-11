import { getRequest } from '../../request-methods';

export default {
  state: {
    isFetching: false,
    data: []
  },
  actions: {
    fetchAllServiceTypes: async (context) => {
      context.commit('setServiceTypeFetching', true);

      try {
        const data = await getRequest({ url: 'api/v1/Service/AllTypes/' });

        context.commit('setServiceTypeData', data);
      } catch (error) {
        console.error(error);
      }

      context.commit('setServiceTypeFetching', false);
    }
  },
  mutations: {
    setServiceTypeFetching: (state, isFetching) => {
      state.isFetching = isFetching;
    },
    setServiceTypeData: (state, data) => {
      state.data = data;
    }
  },
  getters: {
    serviceTypeData: ({ data }) => data,
    isLoadingServiceTypes: ({ isFetching }) => isFetching
  }
};
