// src/App.js
import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Dashboard from './Dashboard';
import ScriptForm from './ScriptForm';

function App() {
  return (
    <Router>
      <div>
        {/* Add navigation or header here */}
        <Switch>
          <Route path="/create-script">
            <ScriptForm />
          </Route>
          <Route path="/">
            <Dashboard />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
