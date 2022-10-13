import React, { useState } from "react";

import "./PlotterTab.scss";

import type { formSubmitter } from "../@types/submitter";
import type { options } from "../@types/options";


type PlotterTabProps = {
  submitter: formSubmitter;
  setPlot: React.Dispatch<React.SetStateAction<string>>;
};

const PlotterTab: React.FC<PlotterTabProps> = ({ submitter, setPlot }) => {
  const [dataFileName, setDataFileName] = useState<File>();
  const [options] = useState<options>({
    color: "#0000FF", 
    title: {label: "Title", color: "#666666", fontsize: 12},
    xlabel: {xlabel: "x", loc: "center"},
    ylabel: {ylabel: "y", loc: "center"},
    grid: {visible: true, axis: "both"}
  });

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const fileList = event.target.files;
    if (!fileList) return;
    setDataFileName(fileList[0]);
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (dataFileName) {
      const formData = new FormData();
      formData.append("file", dataFileName, dataFileName.name);
      formData.append("options", JSON.stringify(options));
      const data = await submitter(formData);
      setPlot(data);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type={"file"} accept={".csv"} onChange={handleChange} />
        <button type="submit">Submit plotting request</button>
      </form>
    </div>
  );
};

export default PlotterTab;
