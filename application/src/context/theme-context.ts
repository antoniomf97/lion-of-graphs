import React from "react";

import { Theme, themeContextType } from "../@types/themes";

export const ThemeContext = React.createContext<themeContextType>({
  theme: Theme.dark,
  changeTheme: () => {},
});
