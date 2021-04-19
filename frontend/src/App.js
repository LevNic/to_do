import React from "react";
import './App.css';
import UserList from "./components/User";
import TodoList from "./components/Todo";
import UserTodoList from "./components/UserTodo";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import LoginForm from "./components/Auth";
import axios from "axios";
import {Link, Route, Switch, Redirect, BrowserRouter} from "react-router-dom";
import Cookies from 'universal-cookie';
import TodoForm from "./components/TodoForm";

const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}


class App extends React.Component {
    constructor(props) {
        // const user1 = {id: 1, username: 'Гриня', first_name: 'Александр', last_name: 'Грин', age: '38', mail: 'mail@mail.ru'}
        // const user2 = {id: 2, username: 'Пушка', first_name: 'Александр', last_name: 'Пушкин', age: '25', mail: 'mail@mail.ru'}
        // const users = [user1, user2]
        // const todo1 = {id: 1, project: 'Алые паруса', author: user1}
        // const todo2 = {id: 2, project: 'Золотая цепь', author: user1}
        // const todo3 = {id: 3, project: 'Пиковая дама', author: user2}
        // const todo4 = {id: 4, project: 'Руслан и Людмила', author: user2}
        // const todos = [todo1, todo2, todo3, todo4]
        const users = []
        const todos = []
        super(props);
        this.state = {
            'users': users,
            'todos': todos
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, ()=>this.load_data())
      }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, ()=>this.load_data())
    }


    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
        .then(response => {this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {'Content-Type': 'application/json'}
        if (this.is_authenticated()) {headers['Authorization'] = 'Token ' + this.state.token}
        return headers
    }

    load_data() {

        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {this.setState({users: response.data})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todos/', {headers}).then(response => {
            this.setState({todos: response.data})
            }).catch(error => {console.log(error)
                this.setState({todos: []})
            })
    }

    deleteTodo(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todos/${id}`, {headers}).then(response => {
              this.setState({todos: this.state.todos.filter((item)=>item.id !== id)})
            }).catch(error => console.log(error))
    }

    createTodo(name, author) {
        const headers = this.get_headers()
        const data = {project: name, author: author}
        axios.post(`http://127.0.0.1:8000/api/todos/`, data, {headers}).then(response => {
              let new_todo = response.data
              const author = this.state.users.filter((item) => item.id === new_todo.author)[0]
              new_todo.author = author
              this.setState({todos: [...this.state.todos, new_todo]})
        }).catch(error => console.log(error))
    }



    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
        return (
            <div className={App}>
                <Menu />
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/todos'>Todos</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>


                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/todos/create' component={() => <TodoForm authors={this.state.authors} createTodo={(name, author) => this.createTodo(name, author)} />}  />
                        <Route exact path='/todos' component={() => <TodoList items={this.state.todos} deleteTodo={(id)=>this.deleteTodo(id)} />} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Route path='/user/:id'> <UserTodoList items={this.state.todos}/> </Route>
                        <Redirect from='/users' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
                <Footer/>
            </div>
        )
    }
}

export default App;
