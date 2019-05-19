import React, { Component } from 'react';
import './App.css';

class App extends Component {

  state = { items: [] }

  componentDidMount() {
    fetch('https://swapi.co/api/people/?format=json')
      .then(response => response.json())
      .then(({ results: items }) => this.setState({ items }))
  }

  render() {
    console.log("render function is running")
    let items = this.state.items
    return (
      <div className="App">
        <div>
          {items.map(item =>
            <h1 key={item.name}>{item.name}</h1>)}
        </div>
      </div>
    );
  }
}


export default App;
