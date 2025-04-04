import React, { useState } from "react";
import {  Button} from "antd";
import CollectionModal from '../modals/CollectionModal'
import { getComponentName } from '../../apis/text_mapper.js'


const ModalButton = ({
    formObject,
    FormComponent, 
    onSave, 
    action,
    target,
    buttonType}) => {
    const [modalVisible, setModalVisible] = useState(false);
  
    const onCreate = async (values) => {
        console.log(values)
        const response = onSave(values)
        if (response){
            setModalVisible(false);
        }
    };
  
    const showModal = () => {
      setModalVisible(true);
    };

    return (
      <>
      <Button  onClick={showModal} type={buttonType}>
        {getComponentName([action])}
      </Button >

      <CollectionModal
          modalVisible={modalVisible}
          onCreate={onCreate}
          onCancel={() => {
            setModalVisible(false);
          }}
          name={getComponentName([action, target])}
          FormComponent={FormComponent}
          form={formObject}
      />
    </>
    );
  };
  
  export default ModalButton;