import React, { useState } from "react";

import type { formSubmitter } from "../@types/submitter";

type FitterTabProps = {
  submitter: formSubmitter;
  setPlot: React.Dispatch<React.SetStateAction<string>>;
};

const FitterTab: React.FC<FitterTabProps> = ({ submitter, setPlot }) => {
  const [dataFileName, setDataFileName] = useState<File>();
  const [fittingFunc, setFittingFunc] = useState("y = x + 1");

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

  const default_json = JSON.stringify({
    title: 'Title tities',
  })

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (dataFileName && fittingFunc) {
      const formData = new FormData();
      formData.append("file", dataFileName, dataFileName.name);
      formData.append("options", default_json);
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
