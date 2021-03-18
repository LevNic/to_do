import React from "react";
import './App.css';
import UserList from "./components/User";
import TodoList from "./components/Todo";
import UserTodoList from "./components/UserTodo";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import axios from "axios";
import {Link, Route, Switch, Redirect, BrowserRouter} from "react-router-dom";

const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}


class App extends React.Component {
    constructor(props) {
        const user1 = {id: 1, username: 'Гриня', first_name: 'Александр', last_name: 'Грин', age: '38', mail: 'mail@mail.ru'}
        const user2 = {id: 2, username: 'Пушка', first_name: 'Александр', last_name: 'Пушкин', age: '25', mail: 'mail@mail.ru'}
        const users = [user1, user2]
        const todo1 = {id: 1, project: 'Алые паруса', author: user1}
        const todo2 = {id: 2, project: 'Золотая цепь', author: user1}
        const todo3 = {id: 3, project: 'Пиковая дама', author: user2}
        const todo4 = {id: 4, project: 'Руслан и Людмила', author: user2}
        const todos = [todo1, todo2, todo3, todo4]
        super(props);
        this.state = {
            'users': users,
            'todos': todos
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/user/').then(r =>
            {
                const users = r.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }
        ).catch(error => console.log(error))
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
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/todos' component={() => <TodoList items={this.state.todos}/>}/>
                        <Route path='/user/:id'>
                            <UserTodoList items={this.state.todos}/>
                        </Route>
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
