import React from "react";
import { notification } from 'antd';
import { SmileOutlined, FrownOutlined  } from '@ant-design/icons';
import { getErrorMessage } from './text_mapper.js'

const post = async (payload, uri)=>{
  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: "1223",
    },
    body: JSON.stringify(payload),
  };

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/${uri}`,
      requestOptions
    );

    const data = await response.json();

    console.log('response:', response);
    console.log('data:', data);
    if (response.ok) {
      notification.open({
        message: 'Sucesso!',
        icon: <SmileOutlined style={{ color: '#108ee9' }} />,
      });
      return data;
    } else {
      notification.open({
            message: 'Erro no envio dos dados!',
            icon: <FrownOutlined style={{ color: '#108ee9' }} />,
      });
      return false
    }
  } catch (error) {
    console.error(error);
  }
}


const fetchData = async (uri, verb, payload)=>{
  const requestOptions = {
    method: verb,
    headers: {
      "Content-Type": "application/json",
      Authorization: "1223",
    }
  };

  if (payload) {
    requestOptions.body = JSON.stringify(payload)
  }

  try {
    const response = await fetch(
      `http://192.168.25.19:8000/api/v1/${uri}`,
      requestOptions
    );

    const data = await response.json();

    if (response.ok) {
      return data;
    } else {
      console.log('erro');
      notification.open({
            message: getErrorMessage(data),
            icon: <FrownOutlined style={{ color: '#108ee9' }} />,
      });
      return false
    }
  } catch (error) {
    console.error(error);
    notification.open({
      message: 'Ops, estamos com erro em nossos serviços!',
      icon: <FrownOutlined style={{ color: '#108ee9' }} />,
});
  }
}


export const loginUser = async (user)=>{
  return await post(user, 'user/login')
}


export const saveCompany = async (company)=>{
  return await post(company, 'company')
}


export const saveTask = async (task)=>{
  return await post(task, 'task')
}

export const putTask = async (task, taskId)=>{
  const uri = `task/${taskId}`
  return await fetchData(uri, 'PUT', task)
}


export const deleteTask = async (taskId)=>{
  const uri = `task/${taskId}`
  return await fetchData(uri, 'DELETE')
}


export const getTasks = async (companyId)=>{
  const uri = `task?company_id=${companyId}` 
  return await fetchData(uri, 'GET')
}


export const getPlans = async (companyId)=>{
  const uri = `plan?company_id=${companyId}` 
  return await fetchData(uri, 'GET')
}

export const savePlan = async (task)=>{
  return await post(task, 'plan')
}

export const removePlan = async (taskId)=>{
  const uri = `plan/${taskId}`
  return await fetchData(uri, 'DELETE')
}

export const putPlan = async (plan, planId)=>{
  const uri = `plan/${planId}`
  return await fetchData(uri, 'PUT', plan)
}

