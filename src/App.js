import './App.css';
import * as React from 'react'
import './index.css';
import {Routes, Route} from 'react-router-dom';
import Login from './pages/Login';

function App() {
  return (
    <div className='App'>
      <Routes>
        <Route path="/" element={<Login/>}/>
        
      </Routes>
    </div>
  );
}

export default App;
