import React, { useState } from "react";

import type { formSubmitter } from "../@types/submitter";

type PlotterTabProps = {
  submitter: formSubmitter;
  plot: string;
  setPlot: React.Dispatch<React.SetStateAction<string>>;
};

const PlotterTab: React.FC<PlotterTabProps> = ({
  submitter,
  plot, // Q: possible to use for download in the future?
  setPlot,
}) => {
  const [dataFileName, setDataFileName] = useState<File>();

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
