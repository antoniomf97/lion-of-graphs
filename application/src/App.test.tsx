import React from "react";
import { render, screen } from "@testing-library/react";
import App from "./App";

test("finds Hello MPB!", () => {
  render(<App />);
  const linkElement = screen.getByText(/Hello MPB!/i);
  expect(linkElement).toBeInTheDocument();
});
