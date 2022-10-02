import React from "react";

import "./Plot.scss";

type PlotProps = {
  plot: string;
};

const Plot: React.FC<PlotProps> = ({ plot }) => {
  return (
    <div className="flex-box-child">
      <div className="plot">
        <img src={plot} alt="error displaying plot" />
      </div>
      <a href={plot} download={plot}>
        download plot
      </a>
    </div>
  );
};

export default Plot;
