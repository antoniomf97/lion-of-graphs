import React from 'react';
import './Plot.css';

// https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths
export default class PathPlot extends React.Component {
  render() {
    return (
        <div>
            <svg className="axis" height={500} width={500}>
                {this.props.points.map((path) => <path d={path.d} stroke={path.stroke} fill={path.fill}/>)}
            </svg>
        </div>
    );
  }
}
