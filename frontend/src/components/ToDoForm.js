import React from 'react'


class ToDoForm extends React.Component {
    constructor(props) {
      super(props)
      this.state = {project: '', text: '', created_at: '', updated_at: '', user: '', is_active: ''}
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
      console.log(this.state)
      this.props.createToDo(this.state.project, this.state.text, this.state.created_at, this.state.updated_at, this.state.user, this.state.is_active)
      event.preventDefault()
    }

    render() {
      return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <div className="form-group">
            <label for="project">project</label>
                <select name='project' className='form-control' onChange={(event) => this.handleChange(event)}>
                 {this.props.projects.map((item)=><option value={item}>{item.name}</option> )}
                </select>
            </div>

            <div className="form-group">
            <label for="text">text</label>
                <input type="text" className="form-control" name="text" value={this.state.text} onChange={(event)=>this.handleChange(event)} />
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

  export default ToDoForm