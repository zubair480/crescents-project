// importing packages
const express = require("express");
const router = express.Router();
const fetch = (...args) =>
  import("node-fetch").then(({ default: fetch }) => fetch(...args));
router.get(`/`, async function (req, res) {
  const url =
    "https://famous-quotes4.p.rapidapi.com/random?category=all&count=2";
  const options = {
    method: "GET",
    headers: {
      "X-RapidAPI-Host": "famous-quotes4.p.rapidapi.com",
      "X-RapidAPI-Key": "your-rapidapi-key",
    },
  };
  // promise syntax
  fetch(url, options)
    .then((res) => res.json())
    .then((json) => console.log(json))
    .catch((err) => console.error("error:" + err));
  try {
    let response = await fetch(url, options);
    response = await response.json();
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ msg: `Internal Server Error.` });
  }
});
module.exports = router;
