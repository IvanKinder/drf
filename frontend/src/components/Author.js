import React from "react"
import {Link} from "react-router-dom"

const AuthorItem = ({author}) => {
    console.log(author)
    return (
        <tr>
            <td>
                <Link to={`author/${author.uuid}`}>{author.uuid}</Link>
            </td>
            <td>
                {author.first_name}
            </td>
            <td>
                {author.last_name}
            </td>
            <td>
                {author.birthday_year}
            </td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                FIRST NAME
            </th>
            <th>
                LAST NAME
            </th>
            <th>
                BIRTHDAY YEAR
            </th>
            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
    )
}
export default AuthorList