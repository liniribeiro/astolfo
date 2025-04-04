import React  from "react";
import { Modal, Form, Input, Select, InputNumber  } from "antd";

const { Option } = Select;

const TaskForm = ({form, formValues}) => {

    return (
      <Form
        form={form}
        name="new_task"
        className="new-task-form"
        labelCol={{ span: 6 }}
        wrapperCol={{ span: 12 }}
        initialValues={formValues}
      >
        <Form.Item
          name="title"
          label="Título"
          rules={[
            {
              required: true,
              message: 'Insira o título ta tarefa!',
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
          name="total_minutes"
          label="Minutos"
          type="number "
          hasFeedback
          rules={[{ required: true, message: 'Selecioe o tempo em minutos desta tarefa!' }]}
        >
          <Select placeholder="Selecione os minutos">
            <Option key="15minuts" value="15">15</Option>
            <Option key="30minuts" value="30">30</Option>
            <Option key="45minuts" value="45">45</Option>
            <Option key="60minuts" value="60">60</Option>
            <Option key="120minuts" value="120">120</Option>
            <Option key="400minuts" value="400">Diária</Option>
          </Select>
        </Form.Item>
        
      </Form>
    )
  }

  export default TaskForm;
  