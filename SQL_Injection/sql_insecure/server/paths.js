const express = require("express");
const controllers = require("./controllers");
const bodyParser = require("body-parser");

const router = express.Router();

router.use(express.json());
router.use(bodyParser.urlencoded({extended : true}));

// API paths
router.post("/api/create_user", controllers.create_user_POST);

module.exports = router;