import { useState } from "react";

import Plot from "./components/Plot";
import TabNavigator from "./containers/TabNavigator";

function App() {
  const [plot, setPlot] = useState("");

  return (
    <div>
      <h1> Hello MPB! </h1>
      <TabNavigator plot={plot} setPlot={setPlot} />
      <Plot plot={plot} />
    </div>
  );
}

export default App;
