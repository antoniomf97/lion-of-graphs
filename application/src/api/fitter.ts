import type { formSubmitter } from "../@types/submitter";

const fitterApi: string = process.env.REACT_APP_MBP_FITTER_API as string;

export const submitFitRequest: formSubmitter = async (formData: FormData) => {
  const response = await fetch(fitterApi, {
    method: "POST",
    headers: {
    },
    body: formData,
  });
  const data = await response.json();
  return data;
};
