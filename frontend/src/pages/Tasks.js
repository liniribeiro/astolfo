import React, { useState, useEffect } from "react";
import { Card, Form, Table, Button, Popconfirm, Space} from "antd";

import {saveTask, getTasks, deleteTask, putTask} from '../apis/astolfo'

import TaskForm from '../components/forms/TaskForm'
import ModalButton from '../components/buttons/ModalButton'


const AddButton = ({companyId, sendTask}) => {
  const onSave = async (values) => {
    values['company_id'] = companyId
    const response = await saveTask(values)
    if (response){
      sendTask(response)
      return true
    }
    return false
  };
  const [formObject] = Form.useForm();
  const action = 'new'
  const target = 'task'
  const buttonType = 'primary'

  return (
    <ModalButton 
    formObject={formObject} 
    FormComponent={() => <TaskForm form={formObject}/>} 
    onSave={onSave} 
    action={action}
    target={target}
    buttonType={buttonType}/>
  );
};

const EditButton = ({record, updateTask}) => {
  const onSave = async (values) => {
    console.log('onSave:', values)
    const response = await putTask(values, record.id)
    if (response){
      updateTask(response)
      return true
    }
    return false
  };
  const [formObject] = Form.useForm();
  const action = 'edit'
  const target = 'task'
  const buttonType = 'link'

  return (
    <ModalButton 
    formObject={formObject} 
    FormComponent={() => <TaskForm form={formObject} formValues={record}/>} 
    onSave={onSave} 
    action={action}
    target={target}
    buttonType={buttonType}/>
  );
};



function Tasks({companyId}) {
  const [tasks, setTasks] = useState([]);

  const sendTask = (task) => {
    setTasks(tasks => [...tasks, task])
  }

  const updateTask = (values) => {
    removeTask(values.id)
    sendTask(values)
  };

  const removeTask = (record_id) => {
      setTasks(tasks.filter((item) => item.id !== record_id));
  };


  const handleDelete = async (record_id) => {
    console.log('handleDelete: ', record_id);
    const response = await deleteTask(record_id)
    if (response){
      removeTask(record_id)
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
      title: "Duração (Minutos)",
      dataIndex: "total_minutes",
      key: "id",
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
            <EditButton record={record} updateTask={updateTask}/>
          </Space>
          
        );
      },
    },
  ];

  useEffect(() => {
    const fetchTasks = async () => {
      const tasks = await getTasks(companyId);
      if (tasks) {
        setTasks(tasks);
      }
  
      console.log(tasks);
    };
    fetchTasks()
  }, [companyId]);


  return (
    <Card title="Tarefas" extra={<AddButton companyId={companyId} sendTask={sendTask}/>}>
      <Table columns={columns} dataSource={tasks} rowKey="id" />
    </Card>
  );
}

export default Tasks;
