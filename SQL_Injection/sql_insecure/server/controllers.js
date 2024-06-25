const db = require("./database");

module.exports.get_user_by_name_POST = async (req, res) => {

    const { user_name } = req.body;
    const user = await db.getUser_by_name(user_name);
    res.status(200).send(user);
}

module.exports.render_result_page_POST = async (req, res) => {
    try {
        const { user_name } = req.body;
        const users = await db.getUser_by_name(user_name);
        console.log(users)
        res.render("index.ejs", {
            users : users
        });
        
    }
    catch(error) {
        console.log(error);
    }
}


