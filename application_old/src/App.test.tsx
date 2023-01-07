import { render, screen } from "@testing-library/react";
import App from "./App";

test("finds Hello MPB!", () => {
  // given
  // when
  render(<App />);
  // then
  const linkElement = screen.getByText(/Hello MPB!/i);
  expect(linkElement).toBeInTheDocument();
});
