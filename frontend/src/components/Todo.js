import React from "react";
import {Link} from 'react-router-dom';


const TodoItem = ({item, deleteTodo}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.project}</td>
            <td>{item.author.username}</td>
            <td><button onClick={()=>deleteTodo(item.id)} type='button'>Delete</button></td>
        </tr>
    )
}

const TodoList = ({items, deleteTodo}) => {
    return (
        <div>
            <table>
                <tr>
                    <td>ID</td>
                    <td>PROJECT</td>
                    <td>AUTHOR</td>
                    <th></th>
                </tr>
                {items.map((item) => <TodoItem item={item} deleteTodo={deleteTodo} />)}
            </table>
            <Link to='/todos/create'>Create</Link>
        </div>
    )
}

export default TodoList