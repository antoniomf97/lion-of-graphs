import { render } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { jest, test } from "@jest/globals";

import { submitPlotRequest } from "../api/plotter";
import type { formSubmitter } from "../types/submitter";
import Plot from "./Plot";
import { act } from "react-dom/test-utils";

test("Plotter form submit triggers post and image replacement", () => {
  // given
  const testFile = new File(["hello"], "hello.csv", { type: "text/csv" });
  const mockImg = new File(["mock"], "mock.png", { type: "image/png" });
  const mockSubmitter = jest.fn(async (formData: FormData) => {
    return mockImg;
  });

  // when
  // TODO

  // then
  // TODO
});
