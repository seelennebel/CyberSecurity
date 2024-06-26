const mysql = require("mysql2");
const dotenv = require("dotenv");

dotenv.config();

const pool = mysql.createPool({
    multipleStatements: true,
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: "website"
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





