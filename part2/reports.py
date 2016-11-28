#get_most_played(file_name)
def get_most_played(file_name):
    file_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            file_list.append(line.split("\t"))
    counter = 0
    name = ''
    for k in file_list:
        if float(k[1]) > float(counter):
            counter = float(k[1])
            name = k[0]
    return name

#print(get_most_played("game_stat.txt"))

#sum_sold(file_name)
def sum_sold(file_name):
    file_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            file_list.append(line.split("\t"))
    counter = 0
    for k in file_list:
        counter += float(k[1])
    return counter

#print(sum_sold("game_stat.txt"))

#get_selling_avg(file_name)
def get_selling_avg(file_name):
    file_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            file_list.append(line.split("\t"))
    counter = 0
    total = 0
    for k in file_list:
        counter += 1
        total += float(k[1])
    average_s = total / counter
    return average_s

#print(get_selling_avg("game_stat.txt"))

#count_longest_title(file_name)
def count_longest_title(file_name):
    file_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            file_list.append(line.split("\t"))
    return max([len(k[0]) for k in file_list])

#print(count_longest_title("game_stat.txt"))

#get_date_avg(file_name)
def get_date_avg(file_name):
    file_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            file_list.append(line.split("\t"))
    total = 0
    counter = 0
    for k in file_list:
        total += int(k[2])
        counter += 1
    average_y = total / counter
    return round(average_y)

#print(get_date_avg("game_stat.txt"))

#get_game(file_name, title)
def get_game(file_name, title):
    file_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            file_list.append(line.split("\t"))
    game = []
    for k in file_list:
        if title == k[0]:
            game = k
            game = [i.rstrip() for i in game]
            for item in game:
                game[1] = float(game[1])
                game[2] = int(game[2])
            return game
print(get_game("game_stat.txt", "The Sims"))
