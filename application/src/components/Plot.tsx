import React from "react";

import "./Plot.css";

type PlotProps = {
  plot: string;
};

const Plot: React.FC<PlotProps> = ({ plot }) => {
  return (
    <div className="scatter-plt">
      <img src={plot} alt="error displaying plot" />
      <a href={plot} download={plot}>
        download plot
      </a>
    </div>
  );
};

export default Plot;
