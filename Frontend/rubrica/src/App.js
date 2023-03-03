import logo from './logo.svg';
import SignIn from './components/SignIn.tsx';
import './App.css';
// import SignIn from './components/signin';
import {BrowserRouter, Route, Routes} from 'react-router-dom'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path='/' element={<SignIn />}>

        </Route>
      </Routes>
      </BrowserRouter> 
    </div>
  );
}

export default App;
