
exports.up = function(knex) {
    return knex.schema
        .createTable("names_years", table => {

            table.increments();

            table.integer("name_id")
                .unsigned()
                .notNullable()
                .references("name_id")
                .inTable("names")
                .onUpdate("CASCADE")
                .onDelete("RESTRICT")
            
            table.integer("year")
                .unsigned()
                .notNullable()
                .index()
            
            table.integer("births")
                .unsigned()
                .index()
        })
};

exports.down = function(knex) {
    return knex.schema
        .dropTableIfExists("names_years")
};
