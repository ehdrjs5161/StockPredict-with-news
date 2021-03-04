import './App.css';
import React, {useState, useEffect} from 'react';
import Company from './Components/Company.js';
import {Route} from 'react-router-dom';
import {Home, Predict} from './Page';
function App() {
  return (
    <div>
      <Route path="/" exact={true} component={Home}/>
      <Route path="/code/:code"  exact={true} component={Predict}/>
    </div>
  );
}

export default App;
