const express = require("express");
const helmet = require("helmet");
const cors = require("cors");

const server = express();

server.use(helmet());
server.use(express.json());
server.use(cors());

// Fallback in case an invalid route is encountered anywhere in the routes above
server.use("/", (req, res) => {
    res.status(200).send("Student name database is running.")
})

module.exports = server;