year_start = 1880
year_end = 2019

# return a dictionary after parsing the SSA data
# key: tuple (name, sex)
# value: dictionary of years to births
def parse_raw_data(year_start, year_end):

    known_names = dict()

    # parse each file from the original data
    for year in range(year_start, year_end):

        with open("by_year/yob" + str(year) + ".txt") as file:

            for line in file.readlines():

                # extract data from each line
                name, sex, births = line.split(",")
                births = int(births)

                # create a dictionary for the name if it hasn't been seen before
                if (name, sex) not in known_names:
                    known_names[(name, sex)] = dict()

                known_names[(name, sex)][year] = births

    return known_names


import json

# create a single text file of all the names that can be found in the data
def create_file_of_names(known_names):
    
    with open("names.json", "w") as file:

        for name_data in known_names:
        
            # restructure Python data to convert to a JSON object
            # tuples can't be used as keys in JSON
            name, sex = name_data
            year_data = known_names[name_data]

            data = {name + "_" + sex: year_data}

            file.write(json.dumps(data))

known_names = parse_raw_data(year_start, year_end)
create_file_of_names(known_names)

# with open("test.txt", "w") as file:

#     # create new files, one for each name
#     for name_data in known_names:

#         name, sex = name_data
#         year_data = known_names[name_data]

#         # with open("by_name/" + name + "_" + sex + ".txt", "w") as file:

#         for year in year_data:

#             birth = year_data[year]

#             file.write(str(year) + ": " + str(birth) + "\n")
    
print("done")