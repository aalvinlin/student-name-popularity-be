
exports.up = function(knex) {
    return knex.schema
        .createTable("sexes", table => {

            // specified in seeds: 1 will represent "M" and 2 will represent "F"
            table.increments("sex_id");

            table.string("sex", 32)
                .notNullable()
        })

        .createTable("names", table => {

            table.increments("name_id");

            table.string("name", 64)
                .notNullable()
                .index()
            
            table.integer("sex_id")
                .unsigned()
                .references("sex_id")
                .inTable("sexes")
                .onUpdate("CASCADE")
                .onDelete("RESTRICT")
        })
};

exports.down = function(knex) {
    return knex.schema
        .dropTableIfExists("names")
        .dropTableIfExists("sexes")
};
