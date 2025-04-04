
import React, { useState } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import { Layout } from "antd";

import Sidebar from "../../components/Sidebar";
import AFooter from "../../components/AFooter";
import NavHeader from "../../components/NavHeader";
import Home from "../Home";
import Tasks from "../Tasks";
import Signatures from "../Signatures";
import Company from "../company/Company";
import Plans from "../Plans";
import Customers from "../Customers";


const { Content } = Layout;

const AContent = ({companyId}) => {
  const style = {
    padding: "3rem",
  };

  return (
    <Content style={style}>
      <Switch>
        <Route path="/" exact component={() => <Home companyId={companyId}/>} />
        <Route path="/tasks" exact component={() => <Tasks companyId={companyId}/>} />
        <Route path="/signatures" exact component={() => <Signatures companyId={companyId}/>} />
        <Route path="/company" exact component={() => <Company companyId={companyId}/>}  />
        <Route path="/plans" exact component={() => <Plans companyId={companyId}/>}  />
        <Route path="/customers" exact component={() => <Customers companyId={companyId}/>} />
      </Switch>
    </Content>
  );
};

const AuthorizedApp = ({doLogOff, companyId}) => {
  const [collapsed, setCollapsed] = useState(false);
  const [headerName, setHeaderName] = useState("Painel");

  const activateMenu = (name) => {
    setHeaderName(name);
  };

  const onCollapse = () => setCollapsed(!collapsed);

    
  return (
    <Router>
      <Layout style={{ minHeight: "100vh" }}>
        <Sidebar
          collapsed={collapsed}
          onCollapse={onCollapse}
          activeMenu={activateMenu}
          doLogOff={doLogOff}
        />
        <Layout className="site-layout">
          <NavHeader headerName={headerName} />
          <AContent companyId={companyId} />
          <AFooter />
        </Layout>
      </Layout>
    </Router>
  );
}


export default AuthorizedApp;
