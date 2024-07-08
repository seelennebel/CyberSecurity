const mysql = require("mysql2");
const dotenv = require("dotenv");

dotenv.config();

const pool = mysql.createPool({
    multipleStatements: false,
    host: "mysql_server",
    user: "root",
    password: "root",
    database: "website"
}).promise();

module.exports.createUser = async (user_name, email, password, language) => {
    const res_1 = await pool.query(`
        INSERT INTO Users (email, user_name)
        VALUES ("${email}", "${user_name}");`)
    const res_2 = await pool.query(`
        INSERT INTO Auth (email, password)
        VALUES ("${email}", "${password}");`)
    const res_3 = await pool.query(`
        INSERT INTO Languages (email, language)
        VALUES ("${email}", "${language}");`)
    return res[0];
}

module.exports.findUser = async (language) => {
    const res = await pool.query(`
        SELECT Users.user_name, Languages.language
        FROM Users
        INNER JOIN Languages on Users.email = Languages.email
        WHERE language LIKE ?;`, [language])
    return res[0];
}





