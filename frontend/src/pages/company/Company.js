import React from "react";
import { Card, Col, Row } from "antd";
import CompanyCard from "./CompanyCard";

const UserCard = () => {
  return (
    <Card hoverable title="Usuário Administrador" bordered={false}>
      <p>Card content</p>
      <p>Card content</p>
      <p>Card content</p>
    </Card>
  );
};

const ListUsersCard = () => {
  return (
    <Card hoverable title="Lista de Usuários da Empresa" bordered={false}>
      <p>Card content</p>
      <p>Card content</p>
      <p>Card content</p>
    </Card>
  );
};

function Company() {
  return (
    <div className="site-card-wrapper">
      <Row gutter={16}>
        <Col span={8}>
          <CompanyCard />
        </Col>
        <Col span={8}>
          <UserCard />
        </Col>
        <Col span={8}>
          <ListUsersCard />
        </Col>
      </Row>
    </div>
  );
}

export default Company;
