import React, { useState } from "react";
import "./Plot.css";

const plotterApi: string = process.env.REACT_APP_MBP_PLOTTER_API as string;

type PlotProps = {};

const Plot: React.FC<PlotProps> = () => {
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
      const response = await fetch(plotterApi, {
        method: "POST",
        headers: {
          "Content-type": "multipart/form-data",
          "Access-Control-Allow-Origin": "*", // FIXME: this is to go around localhost issues
        },
        body: formData,
      });
      const data = await response.json();
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
