import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class Graph extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      imglink: 'https://portswigger.net/web-security/images/cross-site-scripting.svg',
      altmsg: 'Failed to do cross-site scripting'
    }
  }
  render() {
    return (
      <div>
        <div>
          <img src={this.state.imglink} alt={this.state.altmsg}/>
        </div>
        <div>
          <button onClick={
            () => this.setState({
              imglink: 'https://google.com',
              altmsg: 'and to access google'
            })
          }> Replace with google </button>
        </div>
      </div>
    );
  }
}

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>
          MathPlotBuilder App
        </h1>
        <Graph />
      </div>      
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

