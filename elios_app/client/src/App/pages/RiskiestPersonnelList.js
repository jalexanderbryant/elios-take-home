import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom';
import Table from 'react-bootstrap/Table';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Container from 'react-bootstrap/Container';
import NavBar from './partials/NavBar';

const Person = ({ body, getProfile }) => {

  return (
    <tbody>
      {body.map(person => {
        const { id, full_name, date_of_birth, has_criminal_record, risk_score } = person;
        return (
          <tr key={id} onClick={() => getProfile(id)}>
            <td>{full_name}</td>
            <td>{date_of_birth}</td>
            <td>{has_criminal_record ? "Yes" : "No"}</td>
            <td>{risk_score}</td>
          </tr>

        );
      })}
    </tbody>
  );
};



class RiskiestPersonnelList extends Component {
  constructor(props){
    super(props);
    console.log('debug0')

    this.state={
      isLoading: true,
      people: [],
      error: null
    }
  } // End constructor

  // Fetch list when component mounts
  componentDidMount(){
    this.getPeople();
  }

  getProfile = (id) => {
    console.log('clicked Profile: ' + id)
    // this.props.history.push('/list');
    this.props.history.push('/person/'+id)
  }

  getPeople = () =>{
    fetch('/person/highest_risk')
      .then(res => res.json())
      .then(
        data => this.setState({
                  people: data,
                  isLoading: false,
                })
      )
      .catch(error => this.setState({error, isLoading: false}));
  }


  render(){
    const { isLoading, people, error } = this.state;
    return(
      <React.Fragment>
        <NavBar />
        <Container>
          <Jumbotron>
            <h1>Personnel with Highest Risk (>200) </h1>
          </Jumbotron>
          <hr />
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Full Name</th>
                <th>D.O.B</th>
                <th>Criminal Record</th>
                <th>Risk Score</th>
              </tr>
            </thead>
            
              {Object.keys(people).map(key => <Person key={key} body={people[key]} getProfile={this.getProfile} />) }
            
          </Table>
        </Container>
        
      </React.Fragment>
    );
    
  }
}

export default RiskiestPersonnelList;