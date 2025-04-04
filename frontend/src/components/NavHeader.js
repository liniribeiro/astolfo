import React from "react";
import { Layout, Typography } from "antd";

const { Header } = Layout;
const { Title } = Typography;

const title_style = {
  color: "#fff",
  padding: "1rem",
};

function NavHeader({ headerName }) {
  return (
    <Header className="site-layout-background" style={{ padding: 0 }}>
      <Title level={3} style={title_style}>
        Astolfo App | {headerName}
      </Title>
    </Header>
  );
}

export default NavHeader;
