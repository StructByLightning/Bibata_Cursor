import { ThemeColors } from "bibata-core/src/types";

// Common Colors
const black = "#000000";
const white = "#FFFFFF";
const amber = "#FF8300";
const richBlack = "#001524";

const themeColors: ThemeColors = {
  Amber: {
    base: amber,
    outline: white,
    watch: {
      background: richBlack,
      foreground: amber
    }
  },
  Classic: {
    base: black,
    outline: white,
    watch: {
      background: black,
      foreground: white,
    }
  },
  Ice: {
    base: white,
    outline: black,
    watch: {
      background: white,
      foreground: black,
    }
  }
};

export { themeColors };
