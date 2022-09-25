import React, { useState } from "react";

import type { formSubmitter } from "../types/submitter";
import "./Plot.css";

type PlotProps = { submitter: formSubmitter };

const Plot: React.FC<PlotProps> = ({ submitter }) => {
  const [pictureSrc, setPictureSrc] = useState("hack-813290_960_720.jpg");
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
      setPictureSrc(data);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type={"file"} accept={".csv"} onChange={handleChange} />
        <button type="submit">Import csv</button>
      </form>
      <div className="base-div">
        <div className="scatter-plt">
          <img src={pictureSrc} alt="error displaying plot" />
        </div>
      </div>
    </div>
  );
};

export default Plot;
