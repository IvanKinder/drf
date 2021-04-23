import React from 'react'


class BookForm extends React.Component {
    constructor(props) {
      super(props)
      this.state = {name: '', author: '08ddc8a7-5637-4be4-bf49-39dd4d146223'}
      console.log(props.authors[0].uuid)
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
      console.log(this.state.author)
      this.props.createBook(this.state.name, this.state.author)
      event.preventDefault()
    }

    render() {
      return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <div className="form-group">
            <label for="login">name</label>
                <input type="text" className="form-control" name="name" value={this.state.name} onChange={(event)=>this.handleChange(event)} />
            </div>

        <div className="form-group">
            <label for="author">author</label>
            <select name='author' className='form-control' onChange={(event) => this.handleChange(event)}>
                {this.props.authors.map((item)=>)}
            </select>
            {/*<input type="text" className="form-control" name="author" value={this.state.author} onChange={(event)=>this.handleChange(event)} />*/}


          </div>
          <input type="submit" className="btn btn-primary" value="Save" />
        </form>
      );
    }
  }

  export default BookForm