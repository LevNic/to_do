import React from "react";


const TodoItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.project}</td>
            <td>{item.author.username}</td>
        </tr>
    )
}

const TodoList = ({items}) => {
    return (
        <table>
            <tr>
                <td>ID</td>
                <td>PROJECT</td>
                <td>AUTHOR</td>
            </tr>
            {items.map((item) => <TodoItem item={item} />)}
        </table>
    )
}

export default TodoList