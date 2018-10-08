import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

class App extends Component {
  state = {
    data: []
  }
  componentDidMount() {
    this.getDataAsync();
    console.log('componentDidMount....');
  }
  componentWillMount() {
    console.log('componentWillMount');
  }
  consuming = () => {
    let sum = 0;
    console.time('clac');
    for(let i = 0; i < 100000; ++i){
      sum += i;
    }
    console.timeEnd('clac');
    return Promise.resolve([1, 3, 2]);
  }
  getDataSync = () => {
    console.log('before getDataSync render');
    const data = [1, 3, 2, 'sync'];
    this.setState({
      data
    });
    console.log('after getDataSync render');
  }

  getDataAsync = () => {
    let data = [1, 3, 2, 'async'];
    this.consuming().then((data)=>{
      console.log('promise before render');
      this.setState({
        data
      });
      console.log('promise after render');
    });
  }

  event = () => {
    let data = [1, 3, 2, 'setTimeout'];
    console.log('before event render');
    setTimeout(() => {
      for (let i = 0; i < 5; i++) {
          this.setState({ data });
      }
    }, 5000);
    console.log('after event render');
  }
  render() {
    const data = this.state.data;
    console.log('page render data:', data);
    return (
      <div className="App">
        <button className="button" onClick={this.getDataSync}>同步</button><br/>
        <button className="button" onClick={this.getDataAsync}>异步</button><br/>
        <button className="button" onClick={this.event}>事件set</button><br/>
      </div>
    );
  }
}

export default App;
