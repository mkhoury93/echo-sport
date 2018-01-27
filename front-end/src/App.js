import React, { Component } from 'react';
import './App.css';
import $ from 'jquery';

class App extends Component {

  handleClick() {
    console.log('hey')
    fetch('/index', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        something: 'hey'
      })
    })
  }

  render() {
    return (
      <div className="App">
        <button onClick={this.handleClick}>team</button>
      </div>
    );
  }
}

export default App;
