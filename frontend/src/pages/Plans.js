import React, { useState, useEffect } from "react";
import { Card, Table, Form, Button, Popconfirm, Space, Input, Select, InputNumber, Tag  } from "antd";

import {savePlan, getPlans, putPlan, removePlan, getTasks} from '../apis/astolfo'

import PlanForm from '../components/forms/PlanForm'
import ModalButton from '../components/buttons/ModalButton'

const AddButton = ({companyId, sendTask}) => {
  const onSave = async (values) => {
    values['company_id'] = companyId
    const response = await savePlan(values)
    if (response){
      sendTask(response)
      return true
    }
    return false
  };
  const [formObject] = Form.useForm();
  const action = 'new'
  const target = 'plan'
  const buttonType = 'primary'

  return (
    <ModalButton 
    formObject={formObject} 
    FormComponent={() =><PlanForm companyId={companyId} form={formObject}/>} 
    onSave={onSave} 
    action={action}
    target={target}
    buttonType={buttonType}/>
  );
};

const EditButton = ({companyId, record, updatePlan}) => {
  const onSave = async (values) => {
    console.log('onSave:', values)
    const response = await putPlan(values, record.id)
    if (response){
      updatePlan(response)
      return true
    }
    return false
  };
  const [formObject] = Form.useForm();
  const action = 'edit'
  const target = 'plan'
  const buttonType = 'link'

  console.log('record:', record)

  return (
    <ModalButton 
    formObject={formObject} 
    FormComponent={() => <PlanForm companyId={companyId} form={formObject} formValues={record}/>} 
    onSave={onSave} 
    action={action}
    target={target}
    buttonType={buttonType}/>
  );
};


function Plans({companyId}) {
  const [plans, setPlans] = useState([]);

  const sendPlan = (plan) => {
    setPlans(plans => [...plans, plan])
  }

  const updatePlan = (values) => {
    console.log('updatePlan: ', values);
    removePlan(values.id)
    sendPlan(values)
  };

  const removePlan = (record_id) => {
    setPlans(plans.filter((item) => item.id !== record_id));
  };

  const handleDelete = async (record_id) => {
    console.log('handleDelete: ', record_id);
    const response = await removePlan(record_id)
    if (response){
      removePlan(record_id)
    }
  };

  const columns = [
    {
      title: "Nome",
      dataIndex: "title",
      key: "id",
    },
    {
      title: "Descrição",
      dataIndex: "description",
      key: "id",
    },
    {
      title: "Valor",
      dataIndex: "price",
      key: "id",
    },
    {
      title: "Dias de duração",
      dataIndex: "days",
      key: "id",
    },
    {
      title: 'Tarefas',
      key: 'tasks',
      dataIndex: 'tasks',
      render: tasks => (
        <>
          {tasks.map(task => {
            let color = task.length > 5 ? 'geekblue' : 'green';
            if (task === 'loser') {
              color = 'volcano';
            }
            return (
              <Tag color={color} key={task['title']}>
                {task['title']}
              </Tag>
            );
          })}
        </>
      ),
    },
    {
      title: "Ações",
      key: "action",
      dataIndex: "operation",
      render: (_, record) => {
        return (
          <Space size="middle">
            <Popconfirm
              title="Tem certeza??"
              onConfirm={() => {
                handleDelete(record.id);
              }}
            >
              <Button  type="link">Delete </Button >
            </Popconfirm>
            <EditButton companyId={companyId} record={record} updatePlan={updatePlan}/>
          </Space>
        );
      },
    },
  ];

  useEffect(() => {
    const fetchPlans = async () => {
      const api_plans = await getPlans(companyId);
  
      if (api_plans) {
        setPlans(api_plans);
      }
      };
    fetchPlans()
  }, [companyId]);

  return (
    <Card title="Planos" extra={<AddButton companyId={companyId} sendPlan={sendPlan} />}>
      <Table columns={columns} dataSource={plans} rowKey="id" />
    </Card>
  );
}

export default Plans;
