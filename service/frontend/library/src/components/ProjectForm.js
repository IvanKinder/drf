import React from 'react'


class ProjectForm extends React.Component {
    constructor(props) {
      super(props)
      this.state = {name: '', data_link: '', user: ''}
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
      console.log(this.state.name)
      console.log(this.state.data_link)
      console.log(this.state)
      this.props.createProject(this.state.name, this.state.data_link, this.state.user)
      event.preventDefault()
    }

    render() {
      return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <div className="form-group">
            <label for="name">name</label>
                <input type="text" className="form-control" name="name" value={this.state.name} onChange={(event)=>this.handleChange(event)} />
            </div>

            <div className="form-group">
            <label for="data_link">data_link</label>
                <input type="text" className="form-control" name="data_link" value={this.state.data_link} onChange={(event)=>this.handleChange(event)} />
            </div>

            <div className="form-group">
            <label for="user">user</label>
            <select name='user' className='form-control' onChange={(event) => this.handleChange(event)}>
                {this.props.users.map((item)=><option value={item}>{item.username}</option> )}
            </select>
            {/*<input type="text" className="form-control" name="author" value={this.state.author} onChange={(event)=>this.handleChange(event)} />*/}


          </div>
          <input type="submit" className="btn btn-primary" value="Save" />
        </form>
      );
    }
  }

  export default ProjectForm