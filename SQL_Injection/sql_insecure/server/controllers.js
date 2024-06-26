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

module.exports.find_users_POST = async (req, res) => {
    const { language } = req.body;
    try {
        const users = await db.findUser(language);
        if(Array.isArray(users) && Array.isArray(users[0])) { // this one is for purpose of displaying the results of SQL injection
            res.render("index.ejs", {
                "users" : users[0]
            });
        }
        else {
            res.render("index.ejs", {
                "users" : users
            });
        }
    }
    catch(error) {
        console.log(error)
    }
}




