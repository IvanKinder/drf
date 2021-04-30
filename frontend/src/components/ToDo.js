import React from "react";
import {Link} from "react-router-dom";

const ToDoItem = ({todo, deleteToDo}) => {
    console.log(todo)
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
            <td>
                <button onClick={()=>deleteToDo(todo.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const ToDoList = ({todos, deleteToDo}) => {
    return (
        <div>
        <table>
            <tr>
            <th>
                PROJECT
            </th>
            <th>
                USER
            </th>
            <th>
                TEXT
            </th>
        </tr>
            {todos.map((todo) => <ToDoItem todo={todo} deleteToDo={deleteToDo}/>)}
        </table>
        <Link to='/todos/create'>Create</Link>
        </div>
    )
}
export default ToDoList