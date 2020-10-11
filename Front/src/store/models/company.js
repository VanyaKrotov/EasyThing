import {
  getRequest,
  postRequest,
  deleteRequest,
  putRequest
} from '.././../request-methods';
import { format } from 'date-fns';
import { Location } from '../../objects';

export const defaultCompany = {
  logo: null,
  title: '',
  email: '',
  description: '',
  dateCreated: new Date(),
  location: new Location()
};

export const permissionsVariants = {
  Всем: 0,
  Подписчикам: 1,
  Сотрудникам: 2
};

export default {
  actions: {
    async fetchAllCompanies(context) {
      context.state.isFetching = true;

      try {
        const companies = await getRequest({
          url: `api/v1/Company/Companies/`
        });

        context.commit('setCompanies', companies);
      } catch (error) {
        console.error(error);
      }

      context.state.isFetching = false;
    },
    async fetchCompany(context, { companyId }) {
      context.state.isFetching = true;

      try {
        const company = await getRequest({
          url: `api/v1/Company/${companyId}/`
        });

        context.commit('setCompanies', [company]);
      } catch (error) {
        console.error(error);
      }

      context.state.isFetching = false;
    },
    async createCompany(context, { setMessage, router, companyData }) {
      context.state.isFetching = true;

      try {
        const { id } = await postRequest({
          url: 'api/v1/Company/Create/',
          data: {
            ...companyData,
            location: JSON.stringify(companyData.location),
            master: context.rootState.user.user.id,
            dateCreated: format(
              new Date(companyData.dateCreated),
              'yyyy-MM-dd'
            ),
            dateRegistration: format(new Date(), 'yyyy-MM-dd')
          }
        });

        router.push({ path: `/company/${id}/feed` });

        setMessage({
          message: 'Компания успешно создана',
          type: 'success'
        });
      } catch (error) {
        setMessage({
          message: error,
          type: 'error'
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
              'yyyy-MM-dd'
            ),
            location: JSON.stringify(companyData.location)
          }
        });

        router.push({ path: `/company/${id}/feed` });

        setMessage({
          message: 'Компания успешно отредактирована',
          type: 'success'
        });
      } catch (error) {
        setMessage({
          message: error,
          type: 'error'
        });
        console.error(error);
      }

      context.state.isFetching = false;
    },
    async deleteCompany(context, { router, id, setMessage }) {
      context.state.isFetching = true;

      try {
        await deleteRequest({
          url: `api/v1/Company/Delete/${id}/`
        });

        router.push({ path: '/companies' });
        setMessage({
          message: 'Компания успешно удалена',
          type: 'success'
        });
      } catch (error) {
        setMessage({
          message: error,
          type: 'error'
        });
        console.error(error);
      }

      context.state.isFetching = false;
    },
    async createCompanyNews(context, { setMessage, postValues, closeForm }) {
      context.state.isNewsFetching = true;

      try {
        await postRequest({
          url: 'api/v1/Company/News/Create/',
          data: {
            ...postValues,
            permissions: permissionsVariants[postValues.permissions]
          }
        });

        closeForm();

        context.dispatch('fetchCompanyNews', {
          setMessage,
          companyId: postValues.company
        });

        setMessage({
          message: 'Пост успешно добавлен',
          type: 'success'
        });
      } catch (error) {
        setMessage({
          message: error,
          type: 'error'
        });
      }

      context.state.isNewsFetching = false;
    },
    async editCompanyNews(context, { setMessage, postValues, closeForm }) {
      context.state.isNewsFetching = true;

      try {
        await putRequest({
          url: `api/v1/Company/News/Edit/${postValues.id}/`,
          data: {
            ...postValues,
            permissions: permissionsVariants[postValues.permissions]
          }
        });

        closeForm();

        context.dispatch('fetchCompanyNews', {
          setMessage,
          companyId: postValues.company
        });

        setMessage({
          message: 'Пост обновлен',
          type: 'success'
        });
      } catch (error) {
        setMessage({
          message: error,
          type: 'error'
        });
      }

      context.state.isNewsFetching = false;
    },
    async changeLikeCompanyNews(context, { setMessage, postId, companyId }) {
      context.state.isNewsFetching = true;

      try {
        const newPost = await putRequest({
          url: `api/v1/Company/News/${postId}/Likes/`
        });

        context.commit('updateCompanyNewsPost', {
          companyId,
          postId,
          newPost
        });
      } catch (error) {
        setMessage({
          message: error,
          type: 'error'
        });
      }

      context.state.isNewsFetching = false;
    },
    async deleteCompanyNews(context, { setMessage, postId, companyId }) {
      context.state.isNewsFetching = true;

      try {
        await deleteRequest({
          url: `api/v1/Company/News/Delete/${postId}/`
        });

        context.commit('deleteCompanyNews', { postId, companyId });

        setMessage({
          message: 'Пост удален',
          type: 'success'
        });
      } catch (error) {
        setMessage({
          message: error,
          type: 'error'
        });
      }

      context.state.isNewsFetching = false;
    },
    async fetchCompanyNews(context, { setMessage, companyId }) {
      context.state.isNewsFetching = true;

      try {
        const { news } = await getRequest({
          url: `api/v1/Company/${companyId}/News/`
        });

        context.commit('setCompanyNews', { companyId, news });
      } catch (error) {
        setMessage({
          message: error,
          type: 'error'
        });
      }

      context.state.isNewsFetching = false;
    }
  },
  mutations: {
    setCompanies(state, companies) {
      state.companies = companies;
    },
    deleteCompanyNews(state, { postId, companyId }) {
      for (let index = 0; index < state.companies.length; index++) {
        if (state.companies[index].id === companyId) {
          state.companies[index].news = state.companies[index].news.filter(
            (post) => post.id !== postId
          );

          return;
        }
      }
    },
    setCompanyNews(state, { companyId, news }) {
      for (let index = 0; index < state.companies.length; index++) {
        if (state.companies[index].id === companyId) {
          state.companies[index].news = news;

          return;
        }
      }
    },
    updateCompanyNewsPost(state, { companyId, postId, newPost }) {
      for (let index = 0; index < state.companies.length; index++) {
        if (state.companies[index].id === companyId) {
          for (
            let indexPost = 0;
            indexPost < state.companies[index].news.length;
            indexPost++
          ) {
            if (state.companies[index].news[indexPost].id === postId) {
              state.companies[index].news[indexPost] = newPost;
            }
          }
        }
      }
    }
  },
  state: {
    isFetching: false,
    isNewsFetching: false,
    companies: []
  },
  getters: {
    getAllCompanies: ({ companies }) => companies,
    getCompanyValues: ({ companies }) => companies[0],
    isLoadingCompany: ({ isFetching }) => isFetching,
    isLoadingNews: ({ isNewsFetching }) => isNewsFetching
  }
};
