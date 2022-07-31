import React from 'react';
import './Plot.css';

export default class ScatterPlot extends React.Component {
  render() {
    return (
        <div>
            <svg className="axis" height={500} width={500}>
                {this.props.points.map((point) => <circle cx={point.x} cy={500-point.y} r={3}/>)}
            </svg>
        </div>
    );
  }
}
