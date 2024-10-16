const mysql = require("mysql2");
const dotenv = require("dotenv");

dotenv.config();

const pool = mysql.createPool({
    multipleStatements: true,
    host: "mysql_server",
    database: "website",
    user:"root",
    password:"root"
}).promise();

module.exports.createUser = async (user_name, email, password, language) => {
    const res = await pool.query(`
        INSERT INTO Users (email, user_name)
        VALUES ("${email}", "${user_name}");
        INSERT INTO Auth (email, password)
        VALUES ("${email}", "${password}");
        INSERT INTO Languages (email, language)
        VALUES ("${email}", "${language}");`);
    return res[0];
}

module.exports.findUser = async (language) => {
    const res = await pool.query(`
        SELECT Users.user_name, Languages.language
        FROM Users
        INNER JOIN Languages on Users.email = Languages.email
        WHERE language LIKE "${language}";`)
    return res[0];
}





