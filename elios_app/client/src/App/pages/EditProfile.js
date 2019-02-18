import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom';
import Table from 'react-bootstrap/Table'
import Jumbotron from 'react-bootstrap/Jumbotron'
import Container from 'react-bootstrap/Container'

class EditProfile extends Component {
  constructor(props){
    super(props);

    this.handleSubmit = this.handleSubmit.bind(this);
  } // End constructor

  handleSubmit(e){
    e.preventDefault();
    // Collect Form submission data
    const data = new FormData(e.target)

    fetch('/person/' + this.props.match.params.id + '/edit', {
      method: 'POST',
      body: data,
    })
    .then(res => this.props.history.push('/person/' + this.props.match.params.id));
  }

  render(){
    return(
      <Container>
        <form onSubmit={this.handleSubmit}>
          <label>
            Full Name: <br />
            <input type="text" ref={(input) => this.input = input} name="name" id="name" placeholder="Enter a new full name" />
          </label>
          <br />
          <input type="submit" value="Submit" />
        </form>
      </Container>
    );
  }
}

export default EditProfile;