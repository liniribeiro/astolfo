import React,  { useState, useCallback, useEffect }  from "react";
import { Modal, Form, Input, Select, InputNumber  } from "antd";

import {getTasks} from '../../apis/astolfo'

const { Option } = Select;


const PlanForm = ({form, companyId, formValues}) => {
  const [taskOptions, setTaskOptions] = useState([])  

  const getTasks1 = useCallback(async () => {
    const apiTasks = await getTasks(companyId);
    
    if (apiTasks) {
      setTaskOptions(apiTasks);
    }
  }, [companyId])


  const parseInitialValues = useCallback(() => {
    delete formValues['tasks'];
  }, [companyId])



  useEffect(() => {
    getTasks1()   
    parseInitialValues()
    console.log(' formValues:', formValues);


  }, [getTasks1, parseInitialValues])

  return (
    <Form
      form={form}
      className="new-task-form"
      labelCol={{ span: 6 }}
      wrapperCol={{ span: 12 }}
      // initialValues={formValues}
    >
      <Form.Item
        name="title"
        label="Título"
        rules={[
          {
            required: true,
            message: 'Insira o título to plano!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        name="description"
        label="Descrição"
      >
        <Input/>
      </Form.Item>

      <Form.Item 
        name="price" 
        label="Valor"  
       >
        <InputNumber
        type="number"
        />
      </Form.Item>

      <Form.Item 
        name="days" 
        label="Dias de duração"  
       >
        <InputNumber
        type="number"
        />
      </Form.Item>

      <Form.Item
          name="tasks"
          label="Tarefas"
          hasFeedback
          rules={[{ type: 'array', required: true, message: 'Selecioe o tempo em minutos desta tarefa!' }]}
        >
          <Select mode='multiple' placeholder="Selecione os minutos" >
         {
            taskOptions.map((currentTask) => {
              return (
                <Option key={currentTask.id} value={currentTask.id}>{currentTask.title}</Option>
              );
            })
          
          }
        </Select>
      </Form.Item> 
    </Form>
  )
}

  export default PlanForm;
  