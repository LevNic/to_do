import React from "react";
import './App.css';
import UserList from "./components/User";
import axios from "axios";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
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
            <div>
                <UserList users={this.state.users}/>
            </div>
        )
    }
}

export default App;
