import React from 'react';
import ReactDOM from 'react-dom/client';
import PlotPage from './pages/PlotPage';
import './index.css';

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>
          MatPlotBuilder App
        </h1>
        <PlotPage />
      </div>      
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

