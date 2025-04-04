import React from "react";
import { Form, Input, Button, Card, Upload} from 'antd';
import { UploadOutlined } from '@ant-design/icons';
// import {saveCompany} from '../apis/astolfo'


const RegisterForm = () => {

  const submitForm = async (values) => {
    delete values['confirm'];
    // const user = await saveCompany(values)
    
    // saveUserOnStorage(user)
    window.location.href="/";
  };

  const normFile = (e) => {
    console.log('Upload event:', e);
    const reader = new FileReader();
    reader.onload = e => {
        console.log(e.target.result);
    };
    return reader.readAsDataURL(e.file.originFileObj);
  };

  
  return (
    <Form
      name="normal_login"
      className="login-form"
      initialValues={{ remember: true }}
      onFinish={submitForm}
      labelCol={{ span: 6 }}
      wrapperCol={{ span: 12 }}
    >
      <Form.Item
        name="email"
        label="E-mail"
        rules={[
          {
            type: 'email',
            message: 'The input is not valid E-mail!',
          },
          {
            required: true,
            message: 'Please input your E-mail!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        name="password"
        label="Senha"
        rules={[
          {
            required: true,
            message: 'Insira sua senha!',
          },
        ]}
        hasFeedback
      >
        <Input.Password />
      </Form.Item>

      <Form.Item
        name="confirm"
        label="Confirme a senha"
        dependencies={['password']}
        hasFeedback
        rules={[
          {
            required: true,
            message: 'Confirme sua senha!',
          },
          ({ getFieldValue }) => ({
            validator(_, value) {
              if (!value || getFieldValue('password') === value) {
                return Promise.resolve();
              }
              return Promise.reject(new Error('As duas senhas que você informou, não são iguais!'));
            },
          }),
        ]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item
        name="name"
        label="Nome do estabelecimento"
        rules={[
          {
            required: true,
            message: 'Insira o nome do estabelecimento!',
          },
        ]}
        hasFeedback
      >
        <Input />
      </Form.Item>

      <Form.Item
        name="tenant_name"
        label="Nome do domínio"
        rules={[
          {
            required: true,
            message: 'Insira o nome do dominio para ser criado!',
          },
        ]}
        hasFeedback
      >
        <Input />
      </Form.Item>

      <Form.Item
        name="logo"
        label="Logo"
        valuePropName="logo"
        getValueFromEvent={normFile}
        extra="Faça o upload do logo de seu estabelecimento"
      >
        <Upload  
        maxCount={1} 
        beforeUpload={() => {}}
        listType="picture">
          <Button icon={<UploadOutlined />}>Click to upload</Button>
        </Upload>
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit" className="login-form-button">
          Enviar
        </Button>
      </Form.Item>
    </Form>
    
  )
}

function Register({doLogin, doRegister}) {
  const style = {
    margin: "auto",
    width: "50%",
    padding: "4rem",
  };

  return (
  <div className="site-card-wrapper"  style={style}>
    <Card hoverable title="Cadastro" bordered={false}>
      <RegisterForm doLogin={doLogin}/>
    </Card>
  </div>
  );
}

export default Register;
