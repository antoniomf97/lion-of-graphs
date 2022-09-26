export enum Theme {
  light, // not implemented
  dark, // not implemented
  neon, // not implemented
}

export type themeContextType = {
  theme: Theme;
  changeTheme: (theme: Theme) => void;
};
