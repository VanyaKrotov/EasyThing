import Router from "vue-router";
import Home from "../pages/Home/Home";
import Services from "../pages/Service/Services";
import Page404 from "../pages/ErrorPages/Page404";
import Companies from "../pages/Company/Companies";
import Login from "../pages/Login";
import CompanyEdit from "../pages/Company/Edit";
import CompanySettings from "../pages/Company/Settings";
import Company from "../pages/Company/Company";
import CompanyFeed from "../pages/Company/Feed";
import CompanyServices from "../pages/Company/Services";
import CompanySchedule from "../pages/Company/Schedule";
import CompanyWorkers from "../pages/Company/Workers";

export default new Router({
  routes: [
    {
      path: "/home",
      component: Home,
      name: "home",
    },
    {
      path: "/service",
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
    { path: "/company/:id/edit", component: CompanyEdit },
    {
      path: "/company/:id",
      component: Company,
      children: [
        { path: "feed", component: CompanyFeed },
        { path: "services", component: CompanyServices },
        { path: "schedule", component: CompanySchedule },
        { path: "workers", component: CompanyWorkers },
        { path: "settings", component: CompanySettings },
      ],
    },
    {
      path: "*",
      component: Page404,
    },
  ],
});
