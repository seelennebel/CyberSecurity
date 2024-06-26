const db = require("./database");

module.exports.create_user_POST = async (req, res) => {
    const {user_name, email, password, language} = req.body;
    try {
        const user = await db.createUser(user_name, email, password, language);
        res.status(201).send("success");
    }
    catch(error) {
        res.send(error)
    }
}




