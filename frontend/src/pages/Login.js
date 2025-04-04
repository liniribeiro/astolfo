import React from "react";
import { Form, Input, Button, Card } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';
import {loginUser} from '../apis/astolfo'
import {saveUserOnStorage} from '../utils/storage'

const LoginForm = () => {
  const onFinish = async (values) => {
    const user = await loginUser(values)
    saveUserOnStorage(user)
    window.location.href="/";
  };

  return (
    <Form
      name="normal_login"
      className="login-form"
      initialValues={{ remember: true }}
      onFinish={onFinish}
    >
      <Form.Item
        name="email"
        rules={[{ required: true, message: 'Insira seu E-mail!' }]}
      >
        <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="E-mail" />
      </Form.Item>
      <Form.Item
        name="password"
        rules={[{ required: true, message: 'Insira sua senha!' }]}
      >
        <Input
          prefix={<LockOutlined className="site-form-item-icon" />}
          type="password"
          placeholder="Senha"
        />
      </Form.Item>
      <Form.Item>
      <Button  className="login-form-forgot" type="link">
      Esqueci minha senha!
      </Button >
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit" className="login-form-button">
          Entrar
        </Button> Ou <a href="/register"> Cadastrar</a>
      </Form.Item>
    </Form>
    
  )
}


function Login() {
  const style = {
    margin: "auto",
    width: "50%",
    padding: "4rem",
  };

  return (
  <div className="site-card-wrapper"  style={style}>
    <Card hoverable title="Login" bordered={false}>
      <LoginForm />
    </Card>
  </div>
  );
}

export default Login; 
