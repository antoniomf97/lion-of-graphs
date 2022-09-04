import React from 'react';
import './Plot.css';

export default class Plot extends React.Component {
  render() {
    return (
        <div className='scatter-plt'>
            <img src={this.props.src} alt='error displaying plot'/>
        </div>
    );
  }
}
