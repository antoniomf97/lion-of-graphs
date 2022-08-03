import React from 'react';
import ScatterPlot from '../components/ScatterPlot';
import PathPlot from '../components/PathPlot';
import './PlotPage.css';


export default class PlotPage extends React.Component {
  constructor(props){
    super(props);
    // the default points should be empty
    this.state = {
      points: [{x: 10, y: 10},{x: 50, y: 100},{x: 200, y: 50}, {x: 300, y: 200}, {x: 350, y: 200}, {x: 480, y: 250}],
      paths: [{d:"M 10 10 C 20 20, 40 20, 50 10", stroke:"black", fill:"transparent"}, {d:"M 70 10 C 70 20, 110 20, 110 10", stroke:"black", fill:"transparent"}],
      plotType: "paths",
    }
    
    this.handleOnChange = this.handleOnChange.bind(this);
    this.handleOnSubmit = this.handleOnSubmit.bind(this);
    this.switchPlot = this.switchPlot.bind(this);
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

  switchPlot = () => {
    switch (this.state.plotType) {
      case "points":
        return <ScatterPlot points={this.state.points} />
      case "paths":
        return <PathPlot points={this.state.paths} />
      default:
        return null
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
          {this.switchPlot()}
        </div>
      </div>
    );
  }
}
