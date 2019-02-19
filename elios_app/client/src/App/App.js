import React, { Component } from 'react';
import {Route, Switch} from 'react-router-dom';
import './App.css';
import Home from './pages/Home';
import List from './pages/List';
import PersonnelList from './pages/PersonnelList';
import RiskiestPersonnelList from './pages/RiskiestPersonnelList';
import Profile from './pages/Profile';
import EditProfile from './pages/EditProfile';

class App extends Component {
  render() {
    const App = () => (
      <div>
        <Switch>
          <Route exact path='/' component={PersonnelList}/>
          <Route exact path='/highest_risk' component={RiskiestPersonnelList}/>
          <Route path='/person/:id/edit' component={EditProfile} />
          <Route path='/person/:id' component={Profile} />
          <Route path='/person' component={PersonnelList}/>
          
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
