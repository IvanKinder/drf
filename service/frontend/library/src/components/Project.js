import React from "react";

const ProjectItem = ({project}) => {
    return (
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

const ProjectList = ({projects}) => {
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
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}
export default ProjectList