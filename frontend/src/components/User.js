import React from "react";
import {Link} from 'react-router-dom';

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                <Link to={`user/${user.id}`}>{user.id}</Link>
            </td>
            <td>
                {user.username}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.age}
            </td>
            <td>
                {user.mail}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Username
            </th>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                Age
            </th>
            <th>
                Male
            </th>
            {users.map((user) => <UserItem user={user}/>)}
        </table>
    )
}

export default UserList