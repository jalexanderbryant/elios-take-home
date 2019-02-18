import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom';
import Table from 'react-bootstrap/Table';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Container from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Tab from 'react-bootstrap/Tab';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import {
    Accordion,
    AccordionItem,
    AccordionItemTitle,
    AccordionItemBody,
} from 'react-accessible-accordion';

import 'react-accessible-accordion/dist/fancy-example.css';


const CriminalRecord = ({data}) => {
  // console.log(data);
  return(
    <AccordionItem>
      <AccordionItemTitle>
        <h5>Case Number: {data.case_number}</h5>
      </AccordionItemTitle>
      <AccordionItemBody>
        <h6>Details</h6>
        <p>
          <span>Full Name: {data.first_name} {data.middle_name} {data.last_name}</span><br/>
          <span>D.O.B: {data.date_of_birth}</span><br/>
          <span>Race: {data.race}</span><br/>
          <span>Street Address: {data.address}</span><br/>
          <span>Street Address Line 2: {data.address_second_line}</span><br/>
          <span>Arresting Agency: {data.arresting_agency ? data.arresting_agency : "N/A"}</span><br/>
          <span>City: {data.city}</span><br/>
          <span>State: {data.state}</span><br/>
          <span>Zip: {data.zip}</span><br/>
          <span>Case Number: {data.case_number}</span><br/>
          <span>Case Type: {data.case_type}</span><br/>
          <span>Category: {data.charge_category}</span><br/>
          <span>Charges Filed Date: {data.charges_filed_date}</span><br/>
          <span>Counts: {data.counts}</span><br/>
          <span>Court: {data.court}</span><br/>
          <span>Disposition: {data.disposition}</span><br/>
          <span>Disposition Date: {data.disposition_date}</span><br/>
          <span>Fines: {data.fines ? data.fines : "None"}</span><br/>
          <span>Offense: {data.offsense_description}</span><br/>
          <span>Offense Date: {data.offense_code}</span><br/>
          <span>Offense Code: {data.offense_date}</span><br/>
          <span>Plea: {data.plea || "N/A"}</span><br/>
          <span>Conviction Place: {data.conviction_place || "N/A"}</span><br/>
          <span>Mugshot: {data.mugshot || "N/A"}</span><br/>
          <span>Probation Date: {data.probation_date}</span><br/>
          <span>Sentence Date: {data.sentence_date}</span><br/>
          <span>Source: {data.source}</span><br/>
          <span>Source Name: {data.source_name}</span><br/>
          <span>Source State: {data.source_state}</span><br/>
        </p>
      </AccordionItemBody>
    </AccordionItem>
  );
}

const CriminalRecordSegment = ({data}) => {
  console.log('crt')
  console.log(data);
  return(
    <Accordion>
      {data.map(cr => <CriminalRecord data={cr} />)}
    </Accordion>
  );
}

const Address = ({data}) => {
  // console.log(data);
  return (
    <ListGroup variant="flush">
      <ListGroup.Item>
        {data.street}<br />{data.city}, {data.state} {data.zipcode}<br />
        Duration: <strong>{data.time}</strong>
      </ListGroup.Item>
    </ListGroup>
  );
}

const Person = ({ body }) => {
  // console.log(body)
  return (
    <div>
      <h2>{body.full_name} <Link to={"/person/" + body.id +"/edit"} className="editName">Edit</Link></h2>
      <h4>D.O.B: {body.date_of_birth}</h4>
      <h4>Risk Score: {body.risk_score}</h4>
      <h4>Criminal record: {body.has_criminal_record ? <strong>Yes</strong> : <strong>No</strong>}</h4>
      <hr />
      <br />
      <h3>Addresses</h3>
      {body.addresses.map(addr => <Address data={addr} />)}

      <br />
      <br />
      <h4>Criminal Records</h4>
       {/*body.has_criminal_record ? body.criminal_records.map(record => <CriminalRecord data={record}/>) : <h5>No Criminal Records</h5>*/}
      {body.has_criminal_record ? <CriminalRecordSegment data={body.criminal_records}/> : <h5>No Criminal Records</h5>}
    </div>
  );
};



class Profile extends Component {
  constructor(props){
    super(props);

    this.state={
      isLoading: true,
      person: {},
      error: null
    }
  } // End constructor

  // Fetch list when component mounts
  componentDidMount(){
    this.getProfile();
  }

  // getProfile = (id) => {
  //   console.log('clicked Profile: ' + id)
  //   // this.props.history.push('/list');
  //   this.props.history.push('/person/'+id)
  // }

  getProfile = () =>{
    console.log('Debug ' +this.props.match.params.id )
    fetch('/person/'+this.props.match.params.id)
      .then(res => res.json())
      .then(
        data => this.setState({
                  person: data,
                  isLoading: false,
                })
      )
      .catch(error => this.setState({error, isLoading: false}));
  }


  render(){
    const { isLoading, person, error } = this.state;
    return(
      <React.Fragment>
        <Container>
          {Object.keys(person).map(key => <Person key={key} body={person[key]} />)}
        </Container>
      </React.Fragment>
    );
    
  }
}

export default Profile;