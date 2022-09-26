import { useState } from "react";

import Plot from "./components/Plot";
import TabNavigator from "./components/TabNavigator";

function App() {
  const [plot, setPlot] = useState("hack-813290_960_720.jpg");

  return (
    <div>
      <h1> Hello MPB! </h1>
      <TabNavigator plot={plot} setPlot={setPlot} />
      <Plot plot={plot} />
    </div>
  );
}

export default App;
