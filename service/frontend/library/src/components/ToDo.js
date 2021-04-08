import React from "react";

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.user.username}
            </td>
            <td>
                {todo.text}
            </td>
        </tr>
    )
}

const ToDoList = ({todos}) => {
    return (
        <table>
            <th>
                PROJECT
            </th>
            <th>
                USERNAME
            </th>
            <th>
                TEXT
            </th>
            {todos.map((todo) => <ToDoItem todo={todo} />)}
        </table>
    )
}
export default ToDoList