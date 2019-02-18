import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Container from 'react-bootstrap/Container';

class NavBar extends Component {
  render(){
    return (
      <Container>
          <Navbar bg="light" expand="sm">
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
              <Link to="/">Home</Link>
            </Nav>
          </Navbar.Collapse>
        </Navbar>
        <br />
      </Container>
    );
  }
}

export default NavBar;