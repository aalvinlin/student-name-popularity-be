// all_names_data = require("../names.json");

// exports.seed = function(knex) {

//     return knex("names").insert(
//         all_names_data.map(current_name_data => {

//             // get name and sex from key
//             name_and_sex = Object.keys(current_name_data)[0];
//             let [name, sex] = name_and_sex.split("_");

//             // ID: 0 for "M", 1 for "F"
//             let sex_id = (sex === "F")

//             console.log(name_and_sex, name, sex_id)

//             return {name, sex_id}
//         })
//     )
// }