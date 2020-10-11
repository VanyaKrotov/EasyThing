import Router from 'vue-router';
import Home from '../pages/Home/Home';
import ServiceEdit from '../pages/Service/Forms/EditService';
import Page404 from '../pages/ErrorPages/Page404';
import Companies from '../pages/Company/Companies';
import Login from '../pages/Login';
import CompanyEdit from '../pages/Company/Edit';
import Company from '../pages/Company/Company';
import Calendar from '../pages/Calendar/Calendar';
import Settings from '../pages/Profile/Settings/Settings';
import Board from '../pages/Board/Board';
import Analytics from '../pages/Analytics/Analytics';
import News from '../pages/CommonNews/News';
import Profile from '../pages/Profile/Profile';
import Near from '../pages/Near/Near';

import CompanyFeed from '../pages/Company/SubPages/Feed';
import CompanyServices from '../pages/Company/SubPages/Services';
import CompanySchedule from '../pages/Company/SubPages/Schedule';
import CompanyWorkers from '../pages/Company/SubPages/Workers';
import CompanySettings from '../pages/Company/SubPages/Settings';
import CompanyAbout from '../pages/Company/SubPages/About';

export default new Router({
  routes: [
    {
      path: '/home',
      component: Home,
      name: 'home'
    },
    /* {
      path: "/service",
      component: Services,
      name: "services",
    }, */
    {
      path: '/calendar',
      component: Calendar,
      name: 'calendar'
    },
    {
      path: '/settings',
      component: Settings,
      name: 'settings'
    },
    {
      path: '/board',
      component: Board,
      name: 'board'
    },
    {
      path: '/analytics',
      component: Analytics,
      name: 'analytics'
    },
    {
      path: '/news',
      component: News,
      name: 'news'
    },
    {
      path: '/:profileId/profile',
      component: Profile,
      name: 'profile'
    },
    {
      path: '/near',
      component: Near,
      name: 'near'
    },
    {
      path: '/login',
      component: Login,
      name: 'login'
    },
    {
      path: '/companies',
      component: Companies,
      name: 'companies'
    },
    {
      path: '/service/:id/edit',
      component: ServiceEdit
    },
    {
      path: '/service/create',
      component: ServiceEdit
    },
    {
      path: '/company/create',
      component: CompanyEdit
    },
    { path: '/company/:id/edit', component: CompanyEdit },
    {
      path: '/company/:id',
      component: Company,
      children: [
        { path: 'about', component: CompanyAbout },
        { path: 'feed', component: CompanyFeed },
        { path: 'services', component: CompanyServices },
        { path: 'schedule', component: CompanySchedule },
        { path: 'workers', component: CompanyWorkers },
        { path: 'settings', component: CompanySettings }
      ]
    },
    {
      path: '*',
      component: Page404
    }
  ]
});
