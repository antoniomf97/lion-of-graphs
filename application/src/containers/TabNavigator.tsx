import React from "react";

import PlotterTab from "../components/PlotterTab";
import FitterTab from "../components/FitterTab";
import { submitPlotRequest } from "../api/plotter";
import { submitFitRequest } from "../api/fitter";

type TabNavigatorProps = {
  plot: string;
  setPlot: React.Dispatch<React.SetStateAction<string>>;
};

const TabNavigator: React.FC<TabNavigatorProps> = ({ plot, setPlot }) => {
  return (
    <div>
      <PlotterTab submitter={submitPlotRequest} plot={plot} setPlot={setPlot} />
      <FitterTab submitter={submitFitRequest} plot={plot} setPlot={setPlot} />
    </div>
  );
};

export default TabNavigator;
