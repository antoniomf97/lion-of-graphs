import React, { useState } from "react";

import PlotterTab from "../components/PlotterTab";
import FitterTab from "../components/FitterTab";
import { submitPlotRequest } from "../api/plotter";
import { submitFitRequest } from "../api/fitter";

type TabNavigatorProps = {
  plot: string;
  setPlot: React.Dispatch<React.SetStateAction<string>>;
};

const TabNavigator: React.FC<TabNavigatorProps> = ({ plot, setPlot }) => {
  const [selectedTab, changeSelectedTab] = useState("plotter");

  const renderSwitcher = (selected: string) => {
    switch (selected) {
      case "plotter":
        return (
          <PlotterTab
            submitter={submitPlotRequest}
            plot={plot}
            setPlot={setPlot}
          />
        );
      case "fitter":
        return (
          <FitterTab
            submitter={submitFitRequest}
            plot={plot}
            setPlot={setPlot}
          />
        );
    }
  };

  return (
    <div>
      <div>
        <button onClick={() => changeSelectedTab("plotter")}>plotter</button>
        <button onClick={() => changeSelectedTab("fitter")}>fitter</button>
      </div>
      {renderSwitcher(selectedTab)}
    </div>
  );
};

export default TabNavigator;
