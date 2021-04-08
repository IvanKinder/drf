import React from "react";
import logo from './logo.svg';
import './App.css';
import AuthorList from "./components/Author.js";
import UserList from "./components/User.js";
import BookList from "./components/Book.js";
import axios from "axios";
import {HashRouter, Link, Route, Switch, Redirect, BrowserRouter} from 'react-router-dom';
import AuthorBookList from "./components/AuthorBook.js";
import ProjectList from "./components/Project";
import ToDoList from "./components/ToDo";
import LoginForm from "./components/Auth.js";
import Cookies from 'universal-cookie'
import ToDoProjectList from "./components/ToDoProject";


const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}


class App extends React.Component{
    constructor(props) {
        super(props)
        // const author1 = {id:1, name: 'Грин', birthday_year: 1880}
        // const author2 = {id:2, name: 'Пушкин', birthday_year: 1799}
        // const authors = [author1, author2]
        // const book1 = {id: 1, name: 'Алые паруса', author: author1}
        // const book2 = {id: 2, name: 'Золотая цепь', author: author1}
        // const book3 = {id: 3, name: 'Пиковая дама', author: author2}
        // const book4 = {id: 4, name: 'Руслан и Людмила', author: author2}
        // const books = [book1, book2, book3, book4]
        this.state = {
            'authors': [],
            'users': [],
            'books': [],
            'token': '',
            'my_username': ''
        }
    }

    get_token(username, password){
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
        this.setState({'my_username': username}, () => this.load_data())
    }

    set_token(token){
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated(){
        return this.state.token != ''
    }

    logout(){
        this.set_token('')
        document.location.href = "/login"
    }

    get_token_from_storage(){
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_headers(){
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()){
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/authors', {headers})
            .then(response => {
                const authors = response.data.results
                this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error)
        )
        axios.get('http://127.0.0.1:8000/pagination/userlimitoffset/', {headers})
                .then(response => {
                    const users = response.data.results
                    this.setState(
                        {
                            'users': users
                        }
                    )
                }).catch(error => console.log(error)
            )
    axios.get('http://127.0.0.1:8000/pagination/projectlimitoffset/', {headers})
                .then(response => {
                    const projects = response.data.results
                    this.setState(
                        {
                            'projects': projects
                        }
                    )
                }).catch(error => console.log(error)
            )
    axios.get('http://127.0.0.1:8000/pagination/todolimitoffset/', {headers})
                .then(response => {
                    const todos = response.data.results
                    this.setState(
                        {
                            'todos': todos
                        }
                    )
                }).catch(error => console.log(error)
            )
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
        return (
            <div className="App">
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/todos'>ToDo</Link>
                            </li>
                            <li>
                                <Link to='/users'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/login'>Login</Link>
                            </li>
                            <li>
                                <Link to='/logout'>{this.state.my_username} Logout</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors} />} />
                        <Route exact path='/users' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todos' component={() => <ToDoList todos={this.state.todos} />} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Route exact path='/logout' component={() => this.logout()} />
                        {/*<Route exact path='/login' component={() => <LoginForm />} />*/}
                        {/*<Route path='/'>*/}
                        {/*    <ToDoProjectList items={this.state.project} />*/}
                        {/*</Route>*/}
                        {/*<Route path='/author/:id'>*/}
                        {/*    <AuthorBookList items={this.state.books} />*/}
                        {/*</Route>*/}
                        <Redirect from='/' to='/users'/>
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
