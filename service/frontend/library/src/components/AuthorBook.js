import React from "react"
import {Link} from "react-router-dom"


const AuthorBookItem = ({item}) => {
    return(
        <tr>
            <td>
                {item.id}
            </td>
            <td>
                {item.name}
            </td>
            <td>
                {item.author.name}
            </td>
        </tr>
    )
}

const AuthorBookList = ({items}) => {
    let { id } = useParams()
    let filtered_items = items.filter((item) => item.author.id === id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>AUTHOR</th>
                {filtered_items.map((item) => <AuthorBookItem item={item} />)}
            </tr>
        </table>
    )
}

export default AuthorBookList