name_data = require("../names.json");

exports.seed = function(knex) {

    return knex("names").insert(
        Object.keys(name_data).map(name_and_sex => {
            let name, sex = name_and_sex.split("_");

            // ID: 0 for "M", 1 for "F"
            let sex_id = (sex === "F")

            return {name, sex_id}
        })
    )
}