import { Container } from 'react-bootstrap';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { w3cwebsocket as W3CWebSocket } from 'websocket';
import Header from './components/Header';
// import Footer from './components/Footer';
// import HomeScreen from './screens/HomeScreen';
// import Chat from './screens/Chat';

function App() {
  return (
    <div>
        <Header />
    </div>
  )
}

export default App