const express = require("express");
const controllers = require("./controllers");
const bodyParser = require("body-parser");

const router = express.Router();

router.use(express.json());
router.use(bodyParser.urlencoded({extended : true}));

// API paths
router.post("/api/user", controllers.get_user_by_name_POST);

//Other paths
router.post("/users", controllers.render_result_page_POST);

module.exports = router;