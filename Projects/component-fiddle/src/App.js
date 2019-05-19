import React from 'react';
import './App.css';
import Tweet from './components/Tweet/Tweet.js';
import Navbar from './components/Navbar/Navbar.js'
import Picture from './components/Picture/Picture.js';

function App() {
  return (
    <div className="App">
      <Navbar firstbar='About' secondbar='' thirdbar='Pictures' fourthbar='Projects' fifthbar='Resume' />
      <Picture />       <Picture />       <Picture />       <Picture />
      <header className="App-header">
        <Tweet name='Johnny' message="Johnny 5 in da house" likes="14" />
        <Tweet name='Keegan' message="You know how Keegan do BETTY BOO" likes="45" />
        <Tweet name='Bawlz' message="Hello, I'm bawlz" likes="345" />
        <Tweet name='Courtney' message="I'm COURT-NAYYY" likes="8" />
      </header>
    </div>
  );
}

export default App;
