import { useState } from "react";

import Plot from "./components/Plot";
import TabNavigator from "./components/Navigator";

function App() {
  const [plot, setPlot] = useState("hack-813290_960_720.jpg");

  return (
    <div>
      <div className="box-header">
        <h1> Hello MPB! </h1>
      </div>
      <div className="flex-box-container">
        <TabNavigator setPlot={setPlot} />
        <Plot plot={plot} />
      </div>
    </div>
  );
}

export default App;
