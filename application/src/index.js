import React from 'react';
import ReactDOM from 'react-dom/client';
import GraphPage from './pages/GraphPage';
import './index.css';

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>
          MathPlotBuilder App
        </h1>
        <GraphPage />
      </div>      
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

