import { getRequest } from '../../request-methods';
import { Location } from '../../objects';

export const defaultService = {
  title: '',
  dateCreated: '',
  description: '',
  location: new Location(),
  email: '',
  image: '',
  types: []
};

export default {
  state: {
    isFetching: false,
    data: null
  },
  actions: {
    fetchServiceById: async (context, { setMessage, serviceId }) => {
      context.commit('setServiceFetching', true);

      try {
        const data = await getRequest({
          url: `api/v1/Service/${serviceId}/`
        });

        context.commit('setServiceData', data);
      } catch (error) {
        setMessage({
          type: 'error',
          message: error
        });
      }

      context.commit('setServiceFetching', false);
    }
  },
  mutations: {
    setServiceFetching: (state, isFetching) => {
      state.isFetching = isFetching;
    },
    setServiceData: (state, data) => {
      state.data = data;
    }
  },
  getters: {
    serviceData: ({ data }) => data,
    isLoadingService: ({ isFetching }) => isFetching
  }
};
