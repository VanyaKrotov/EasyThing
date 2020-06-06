import Router from "vue-router";
import Home from "../pages/Home/Home";
import Services from "../pages/Service/Services";
import Page404 from "../pages/ErrorPages/Page404";
import Companies from "../pages/Company/Companies";
import Login from "../pages/Login";
import CompanyEdit from "../pages/Company/Edit";
import CompanySettings from "../pages/Company/CompanySettings";
import CompanyProfile from "../pages/Company/CompanyProfile";

export default new Router({
  routes: [
    {
      path: "/home",
      component: Home,
      name: "home",
    },
    {
      path: "/services",
      component: Services,
      name: "services",
    },
    {
      path: "/login",
      component: Login,
      name: "login",
    },
    {
      path: "/companies",
      component: Companies,
      name: "companies",
    },
    {
      path: "/company/create",
      component: CompanyEdit,
    },
    {
      path: "/company/:id/edit",
      component: CompanyEdit,
    },
    {
      path: "/company/:id/feed",
      component: CompanyProfile,
    },
    {
      path: "/company/:id/settings",
      component: CompanySettings,
    },
    {
      path: "*",
      component: Page404,
    },
  ],
});
