import React, { Component } from 'react';
class List extends Component {
  constructor(props){
    super(props);

    this.state={
      list: []
    }
  } // End constructor

  // Fetch list when component mounts
  componentDidMount(){
    this.getList();
  }

  // Gets list of People from API
  getList = () => {
    fetch('/list/')
      .then(res => res.json())
      .then(list => this.setState({ list }))
  }

  render(){
    const { list } = this.state;

    return (
      <div className="App">
        <h1>Personnel List</h1> 
        {/* Check to see if any items are found*/}
        { list.length ? (
            <div>
              {/* Render the list of items*/}
              {list.map((item) => {
                return(
                  <div>
                    {item}
                  </div>
                );
              })}
            </div>
          ) : (
            <div>
              <h2>No list items found</h2>
            </div>
          )
        }
        </div>
    );
  }
}

export default List;