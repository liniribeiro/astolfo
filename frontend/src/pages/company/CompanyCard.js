import React from "react";
import { Form, Input, Button, Upload, Card } from "antd";
import { UploadOutlined } from "@ant-design/icons";

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};
const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

const normFile = (e) => {
  console.log("Upload event:", e);
  if (Array.isArray(e)) {
    return e;
  }
  return e && e.fileList;
};

const CompanyForm = () => {
  const onFinish = (values) => {
    console.log("Success:", values);
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };

  return (
    <Form
      {...layout}
      name="basic"
      initialValues={{ remember: true }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
    >
      <Form.Item
        label="Nome"
        name="name"
        rules={[
          { required: true, message: "Porfavor digíte o nome da Empresa!" },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Tenant"
        name="tenant"
        rules={[
          { required: true, message: "Porfavor digíte o tenant da Empresa!" },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        name="upload"
        label="Logo"
        valuePropName="fileList"
        getValueFromEvent={normFile}
      >
        <Upload name="logo" maxCount="1" listType="picture">
          <Button icon={<UploadOutlined />}>Click to upload</Button>
        </Upload>
      </Form.Item>

      <Form.Item {...tailLayout}>
        <Button type="primary" htmlType="submit">
          Salvar
        </Button>
      </Form.Item>
    </Form>
  );
};

const CompanyCard = () => {
  return (
    <Card hoverable title="Empresa" bordered={false}>
      <CompanyForm />
    </Card>
  );
};

export default CompanyCard;
