import React from 'react'
import {Link} from "react-router-dom";
import ProjectForm from "./ProjectForm";
import ProjectList from "./Project";
import Route from "react-router-dom/es/Route";


class SearchForm extends React.Component {
    constructor(props) {
      super(props)
      this.state = {name: ''}
      console.log(props)
    }

    handleChange(event)
    {
        this.setState(
                {
                    [event.target.name]: event.target.value
                }
            );
    }

    handleSubmit(event) {
      this.props.searchProject(this.state.name)
      event.preventDefault()
    }

    render() {
      return (
          <div>
            <form onSubmit={(event)=> this.handleSubmit(event)}>
            <div className="form-group">
            <label for="name">name</label>
                <input type="text" className="form-control" name="name" value={this.state.name} onChange={(event)=>this.handleChange(event)} />
            </div>
            <input type="submit" className="btn btn-primary" value="Search" />
        </form>
          </div>
      );
    }
  }

  export default SearchForm