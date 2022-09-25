import React from "react";

import "./Plot.css";

type PlotProps = {
  plot: string;
};

const Plot: React.FC<PlotProps> = ({ plot }) => {
  return (
    <div className="scatter-plt">
      <img src={plot} alt="error displaying plot" />
    </div>
  );
};

export default Plot;
