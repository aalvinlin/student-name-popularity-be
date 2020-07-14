year_start = 1880
year_end = 2019

known_names = dict()

# parse each file from the original data
for year in range(year_start, year_end):

    with open("by_year/yob" + str(year) + ".txt") as file:

        for line in file.readlines():

            # extract data from each line
            name, sex, count = line.split(",")
            count = int(count)

            # create a dictionary for the name if it hasn't been seen before
            if (name, sex) not in known_names:
                known_names[(name, sex)] = dict()

            known_names[(name, sex)][year] = count

# create new files, one for each name
for name_data in known_names:

    name, sex = name_data
    year_data = known_names[name_data]

    with open("by_name/" + name + "_" + sex + ".txt", "w") as file:

        for year in year_data:

            count = year_data[year]

            file.write(year + ", ", count)
    
print("done")