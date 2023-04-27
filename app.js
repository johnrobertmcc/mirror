import React, { Component } from "react"; // import from react
import { App } from "proton-native"; // import the proton-native components
import Layout from "./components/layout/Layout";

export default class Example extends Component {
  render() {
    // all Components must have a render method
    return (
      <App>
        <Layout />
      </App>
    );
  }
}
