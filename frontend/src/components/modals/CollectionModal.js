import React from "react";
import { Modal} from "antd";

const CollectionModal = ({
    modalVisible,
    onCreate,
    onCancel,
    name,
    FormComponent,
    form
  }) => {
    return (
      <Modal
        visible={modalVisible}
        title={name}
        okText="Enviar"
        cancelText="Cancelar"
        onCancel={onCancel}
        onOk={() => {
          form
            .validateFields()
            .then(values => {
              onCreate(values);
              form.resetFields();

            })
            .catch(info => {
              console.log('Validate Failed:', info);
            });
        }}
      >
        {FormComponent()}
      </Modal>
    );
  };
  
  export default CollectionModal;