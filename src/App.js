import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
import NavbarPincipal from './componentes/NavbarPrincipal';
import Cuerpo from './componentes/Cuerpo.js';
import Home from './componentes/Home.js';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
            <Route path='/' element={<NavbarPincipal/> }> 
            <Route path='/home' element={<Home/>} />
            <Route path='/actividades' element={<Cuerpo/>} />
            <Route path='*' element={<Navigate replace to="<Home/>" />} />
            
            </Route> 

        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
