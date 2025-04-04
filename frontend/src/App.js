
import React, { useState } from "react";
import './App.css';
import AuthorizedApp from "./pages/auth/AuthorizedApp";
import LogginApp from "./pages/auth/LogginApp";


function App() {
  const [logged, setLogged] = useState(localStorage.getItem('@logged'));
  const [companyId, setcompanyId] =  useState(localStorage.getItem('@companyId'));

  const doLogOff = () => {
    localStorage.removeItem('@logged');
    localStorage.removeItem('@companyId');
    setLogged(false)
    setcompanyId("")
    window.location.href="/";
  };

  if (logged) {
    return (
      <AuthorizedApp doLogOff={doLogOff} companyId={companyId} />
    );
  } else {
    return (
      <LogginApp />
    );
  }

}

export default App;
