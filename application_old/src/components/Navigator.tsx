import React, { useState } from "react";

import "./Navigator.scss";

import PlotterTab from "./PlotterTab";
import FitterTab from "./FitterTab";
import { submitPlotRequest } from "../api/plotter";
import { submitFitRequest } from "../api/fitter";

type TabNavigatorProps = {
  setPlot: React.Dispatch<React.SetStateAction<string>>;
};

const TabNavigator: React.FC<TabNavigatorProps> = ({ setPlot }) => {
  const [selectedTab, changeSelectedTab] = useState("plotter");

  const renderSwitcher = (selected: string) => {
    switch (selected) {
      case "plotter":
        return <PlotterTab submitter={submitPlotRequest} setPlot={setPlot} />;
      case "fitter":
        return <FitterTab submitter={submitFitRequest} setPlot={setPlot} />;
    }
  };

  return (
    <div className="flex-box-child">
      <div className="navigator">
        <button onClick={() => changeSelectedTab("plotter")}>plotter</button>
        <button onClick={() => changeSelectedTab("fitter")}>fitter</button>
      </div>
      <div className="navigator-tab">{renderSwitcher(selectedTab)}</div>
    </div>
  );
};

export default TabNavigator;
