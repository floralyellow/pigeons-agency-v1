import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Dashboard from './components/dashboard/Dashboard';
import Login from './components/login/Login';
import Register from './components/register/Register';
//import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
  <Dashboard />
  <Login />
  <Register />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
//reportWebVitals();
