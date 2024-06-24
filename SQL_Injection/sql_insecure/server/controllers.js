const db = require("./database");

module.exports.get_user_by_name_POST = async (req, res) => {

    const { user_name } = req.body;
    const user = await db.getUser_by_name(user_name);
    res.status(200).send(user);
}

module.exports.render_result_page_POST = async (req, res) => {
    try {
        const { user_name } = req.body;
        const user = await db.getUser_by_name(user_name);
        res.send(user);
        /*
        res.render("result.ejs", {
            user : user
        });
        */
    }
    catch(error) {
        console.log(error);
    }
}


