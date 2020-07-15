year_start = 1880
year_end = 2019

# return a dictionary after parsing the SSA data
# key: tuple (name, sex)
# value: dictionary of years to births
def parse_raw_data(year_start, year_end):

    known_names = dict()

    # parse each file from the original data
    for year in range(year_start, year_end):

        with open("raw/yob" + str(year) + ".txt") as file:

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

# create a single JSON file containing all the name data
# each name is an object in the overall array
def create_file_of_names(known_names):
    
    # restructure Python data to convert to a JSON object
    # tuples can't be used as keys in JSON
    modified_name_data = [0] * len(known_names.keys())

    for i, name_data in enumerate(known_names):
        
        name, sex = name_data
        year_data = known_names[name_data]

        modified_name_data[i] = {name + "_" + sex: year_data}

    with open("names.json", "w") as file:
        file.write(json.dumps(modified_name_data))

known_names = parse_raw_data(year_start, year_end)
create_file_of_names(known_names)

print("done")