import { getRequest } from '../../request-methods';

export default {
  state: {
    isFetching: false,
    data: []
  },
  actions: {
    fetchWorkShedudles: async (context) => {
      context.commit('setWorkShedudlesFetching', true);

      try {
        const data = await getRequest({
          url: 'api/v1/Service/WorkShedudles/'
        });

        context.commit('setWorkShedudlesData', data);
      } catch (error) {
        console.error(error);
      }

      context.commit('setWorkShedudlesFetching', false);
    }
  },
  mutations: {
    setWorkShedudlesFetching: (store, isFetching) => {
      store.isFetching = isFetching;
    },
    setWorkShedudlesData: (store, data = []) => {
      store.data = data;
    }
  },
  getters: {
    workShedudlesData: ({ data }) => data
  }
};
