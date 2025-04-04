import React from "react";
import {
  PieChartOutlined,
  BarsOutlined,
  SettingOutlined,
  AppstoreOutlined,
  ShopOutlined,
  UserOutlined,
  FundProjectionScreenOutlined,
  CloseCircleOutlined,
} from "@ant-design/icons";

export const SidebarData = [
  {
    type: "menu",
    title: "Painel",
    path: "/",
    icon: <FundProjectionScreenOutlined />,
    cName: "nav-text",
  },
  {
    type: "menu",
    title: "Tarefas",
    path: "/tasks",
    icon: <BarsOutlined />,
    cName: "nav-text",
  },
  {
    type: "menu",
    title: "Planos",
    path: "/plans",
    icon: <AppstoreOutlined />,
    cName: "nav-text",
  },
  {
    type: "menu",
    title: "Clientes",
    path: "/customers",
    icon: <UserOutlined />,
    cName: "nav-text",
  },
  {
    type: "menu",
    title: "Assinaturas",
    path: "/signatures",
    icon: <PieChartOutlined />,
    cName: "nav-text",
  },
  {
    type: "sub",
    title: "Configurações",
    icon: <SettingOutlined />,
    cName: "nav-text",
    sub: [
      {
        title: "Empresa",
        path: "/company",
        icon: <ShopOutlined />,
        cName: "nav-text",
      },
      {
        title: "Logout",
        path: "/",
        icon: <CloseCircleOutlined />,
        cName: "nav-text",
      },
    ],
  },
];
