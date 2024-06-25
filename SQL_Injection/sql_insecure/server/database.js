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

module.exports.getUser_by_name = async (id) => {
    const res = await pool.query(`SELECT * FROM Users WHERE user_name LIKE "${id}"`);
    return res[0];
}





