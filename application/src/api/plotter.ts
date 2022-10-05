import type { formSubmitter } from "../@types/submitter";

const plotterApi: string = process.env.REACT_APP_MBP_PLOTTER_API as string;

export const submitPlotRequest: formSubmitter = async (formData: FormData) => {
  const response = await fetch(plotterApi, {
    method: "POST",
    headers: {
    },
    body: formData,
  });
  const data = await response.json();
  return data;
};
