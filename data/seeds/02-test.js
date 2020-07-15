exports.seed = function(knex) {

    return knex("names").insert([
        {name: "test", sex_id: 1}
    ])
}