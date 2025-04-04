
import React, { useState } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import { Layout } from "antd";

import AFooter from "../../components/AFooter";
import NavHeader from "../../components/NavHeader";
import Login from "../Login";
import Register from "../Register";


const { Content } = Layout;

const LoginContent = () => {
  return (
    <Content>
      <Switch>
        <Route path="/login" exact component={Login}/>
        <Route path="/register" exact component={Register}/>
        <Route path="/*" exact component={Login}/>
      </Switch>
    </Content>
  );
};

const LogginApp = () => {
  const [headerName, setHeaderName] = useState("Bem vindo!");
  return (
    <Router>
    <Layout style={{ minHeight: "100vh" }}>
      <Layout className="site-layout">
        <NavHeader headerName={headerName} />
        <LoginContent />
        <AFooter />
      </Layout>
    </Layout>
  </Router>
  );
}


export default LogginApp;
