import React from 'react';
import Plot from '../components/Plot';
import './PlotPage.css';


export default class PlotPage extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      picture: 'hack-813290_960_720.jpg',
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
          method: 'POST',
          headers: {
            'Content-type': 'multipart/form-data',
            'Access-Control-Allow-Origin': '*' // FIXME: this is to go around localhost issues
          },
          body: formData,
        })
        const data = await response.json();
        this.setState({ picture: data})
    }
  }

  render() {
    return (
      <div>        
        <form onSubmit={this.handleSubmit}>
          <input type={'file'} accept={'.csv'} onChange={this.handleOnChange}/>
          <button onClick={this.handleOnSubmit}> IMPORT CSV</button>
        </form>
        <div className='basePage'>
          <Plot src={this.state.picture}/>
        </div>
      </div>
    );
  }
}
