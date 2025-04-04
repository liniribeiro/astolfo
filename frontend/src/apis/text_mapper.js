
export const getErrorMessage = (message)=>{
  const default_response =  'Erro no envio dos dados!'
  const errors = {
    'plan-using-task': "Erro ao deletar tarefa! Esta tareefa está sento utilizada por um plano!",
  }
  const error_response = errors[message]
  return error_response ? error_response : default_response
}

export const getComponentName = (tags)=>{
  const translated = {
    'edit': 'Editar',
    'task': "Tarefa",
    'edit_task': "Editar tarefa",
    'new': "Novo",
    'plan': "Plano",
  }
  const word_list = tags.map((tag) => translated[tag])
  const words = word_list.join().replace(',', ' ')
  return words
}