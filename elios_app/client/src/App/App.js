import React, { Component } from 'react';
import {Route, Switch} from 'react-router-dom';
import './App.css';
import Home from './pages/Home';
import List from './pages/List';
import PersonnelList from './pages/PersonnelList';
import Profile from './pages/Profile';

class App extends Component {
  render() {
    const App = () => (
      <div>
        <Switch>
          <Route exact path='/' component={PersonnelList}/>
          <Route exact path='/home' component={Home}/>
          <Route path='/list' component={List}/>
          <Route path='/person/:id' component={Profile} />

        </Switch>
      </div>
    )
    return (
      <Switch>
        <App/>
      </Switch>
    );
  }
}

export default App;
