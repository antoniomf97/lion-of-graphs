import Plot from "./components/Plot";
import { submitPlotRequest } from "./api/plotter";

function App() {
  return (
    <div>
      <h1> Hello MPB! </h1>
      <Plot submitter={submitPlotRequest} />
    </div>
  );
}

export default App;
