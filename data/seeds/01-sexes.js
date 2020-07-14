exports.seed = function(knex) {

    return knex("sexes").insert([
        {sex: "M"},
        {sex: "F"}
    ])
}