const express = require("express");
const path = require("path");
const APIrouter = require("./paths");
const bodyParser = require("body-parser")
const controllers = require("./controllers");

const PORT = process.env.PORT || 8080;
const app = express();
app.use(APIrouter);
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.json());

app.use(express.static(path.join(__dirname, "../", "static")));

app.set("view engine", "ejs")

app.listen(PORT, () => {
    console.log(`listening on port ${PORT}`);
});

app.get("/", (req, res) => {
    res.sendFile("index.html");
});