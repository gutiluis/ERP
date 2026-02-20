import js from "@eslint/js";
import parserTS from "@typescript-eslint/parser"; // read ts syntax //
import globals from "globals";
import react from "eslint-plugin-react";
import tsPlugin from "@typescript-eslint/eslint-plugin";
import reactHooks from "eslint-plugin-react-hooks";
import { defineConfig } from "eslint/config";

export default defineConfig([
  js.configs.recommended,
  { 
    // js and jsx are for react files //
    files: ["**/*.{ts,tsx,js,jsx}"],  // more files has more errors //
    languageOptions: {
      parser: parserTS,
      parserOptions: {
        ecmaVersion: "latest", // javascript syntax version newest latest is the recommendation ECMAScript version//
        // import/export allowed; top-level undefined //
        sourceType: "module", // module is default. invalid if code has a module scope and is run in strict mode. from official docs //
        ecmaFeatures: { jsx: true },
      },
      globals: globals.browser, // browser globals //
    },
    plugins: {
      "@typescript-eslint": tsPlugin,
      react,
      "react-hooks": reactHooks,
    },
    settings: {
      react: { version: "detect" },
    },
    rules: { // rules key to configure rules with error levels and options fron eslint docs //
      // react hooks //
      // in flat config react-hooks does not need plugin object import //
      "react-hooks/rules-of-hooks": "error",
      "react-hooks/exhaustive-deps": "warn",
      // general js //
      "no-console": "warn",
    },
  },
]);
