import React from 'react';
import Graph from '../components/Graph';
import './GraphPage.css';


export default class GraphPage extends React.Component {
  constructor(props){
    super(props);
    // the default points should be empty
    this.state = {
      points: [{x: 10, y: 10},{x: 50, y: 100},{x: 200, y: 50}, {x: 300, y: 200}, {x: 350, y: 200}, {x: 480, y: 250}],
      file: "",
    }
    
    this.handleOnChange = this.handleOnChange.bind(this);
    this.handleOnSubmit = this.handleOnSubmit.bind(this);
  }

  async handleOnChange(e) {
    this.setState({ file: e.target.files[0]})
  }

  async handleOnSubmit(e) {
    e.preventDefault();
    if (this.state.file) {
        const formData = new FormData();
        formData.append('file', this.state.file)
        const response = await fetch('http://localhost:8080', { // FIXME: don't have hardcoded URLs
          method: "POST",
          headers: {
            'Content-type': 'multipart/form-data',
            'Access-Control-Allow-Origin': '*' // FIXME: this is to go around localhost issues
          },
          body: formData,
        })
        const data = await response.json();
        this.setState({ points: data})
    }
  }

  render() {
    return (
      <div>        
        <form onSubmit={this.handleSubmit}>
          <input type={"file"} accept={".csv"} onChange={this.handleOnChange}/>
          <button onClick={this.handleOnSubmit}> IMPORT CSV</button>
        </form>
        <div className='basePage'>
          <Graph points={this.state.points} />
        </div>
      </div>
    );
  }
}
