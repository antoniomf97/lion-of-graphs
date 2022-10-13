import React, { useState } from "react";

import "./FitterTab.scss";

import type { formSubmitter } from "../@types/submitter";
import type { options } from "../@types/options";


type FitterTabProps = {
  submitter: formSubmitter;
  setPlot: React.Dispatch<React.SetStateAction<string>>;
};

const FitterTab: React.FC<FitterTabProps> = ({ submitter, setPlot }) => {
  const [dataFileName, setDataFileName] = useState<File>();
  const [fittingFunc, setFittingFunc] = useState("y = x + 1");
  const [options] = useState<options>({
    color: "#0000FF", 
    title: {label: "Title", color: "#666666", fontsize: 12},
    xlabel: {xlabel: "x", loc: "center"},
    ylabel: {ylabel: "y", loc: "center"},
    grid: {visible: true, axis: "both"}
  });


  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const fileList = event.target.files;
    if (!fileList) return;
    setDataFileName(fileList[0]);
  };

  const handleFuncChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const fittingFunc = event.target.value;
    // TODO some validation and display warning / RED if not validated
    setFittingFunc(fittingFunc);
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (dataFileName && fittingFunc) {
      const formData = new FormData();
      formData.append("file", dataFileName, dataFileName.name);
      formData.append("options", JSON.stringify(options));
      formData.append("func", fittingFunc);
      const data = await submitter(formData);
      setPlot(data);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type={"file"} accept={".csv"} onChange={handleFileChange} />
        <input type="text" onChange={handleFuncChange} />
        <button type="submit">Submit fitting request</button>
      </form>
    </div>
  );
};

export default FitterTab;
