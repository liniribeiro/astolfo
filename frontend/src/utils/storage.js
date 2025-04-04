export const saveOnStorage = (data, key)=>{
    localStorage.setItem(key, data);
}


export const saveUserOnStorage = (data) =>{
    console.log('data', data);
    const companyId = data['company_id']
    localStorage.setItem('@companyId', companyId);
    localStorage.setItem('@logged', true);
    localStorage.setItem('@loggeduser', data);
}