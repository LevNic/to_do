import React from "react";
import {useParams} from 'react-router-dom';

const TodoItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.project}</td>
            <td>{item.author.username}</td>
        </tr>
    )
}

const UserTodoList = ({items}) => {
    let {id} = useParams();
    let filtered_items = items.filter((item) => item.author.id == id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>PROJECT</th>
                <th>AUTHOR</th>
            </tr>
            {filtered_items.map((item) => <TodoItem item={item} />)}
        </table>
    )
}

export default UserTodoList