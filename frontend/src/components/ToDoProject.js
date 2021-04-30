import React from "react"
import {useParams} from "react-router-dom"


const ToDoProjectItem = ({project}) => {
    return(
        <tr>
            <td>
                {project.user.username}
            </td>
            <td>
                {project.name}
            </td>
            <td>
                {project.data_link}
            </td>
        </tr>
    )
}

const ToDoProjectList = ({projects}) => {
    let { id } = useParams()
    // let filtered_project = projects.filter((project) => project.id == id)
    return (
        <table>
            <th>
                USERNAME
            </th>
            <th>
                NAME
            </th>
            <th>
                LINK
            </th>
            {/*{filtered_project.map((project) => <ToDoProjectItem project={project} />)}*/}
        </table>
    )
}

export default ToDoProjectList