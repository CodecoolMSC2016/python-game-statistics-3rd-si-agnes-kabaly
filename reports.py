#count_games(file_name)

def count_games(file_name):
    file_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            file_list.append(line.split("\t"))
        return len(file_list)

#decide(file_name, year)

def decide(file_name, year):
    file_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            file_list.append(line.split("\t"))
    for k in file_list:
        if str(year) in k:
            return True
    return False

#get_latest(file_name)
def get_latest(file_name):
    file_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            file_list.append(line.split("\t"))
    counter = 0
    name = ''
    for k in file_list:
        if k[2] > str(counter):
            counter = k[2]
            name = k[0]
    return name

#count_by_genre(file_name, genre)
def count_by_genre(file_name, gener):
    file_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            file_list.append(line.split("\t"))
    counter = 0
    for k in file_list:
        if k[3] == gener:
            counter += 1
    return counter

#get_line_number_by_title(file_name, title)
def get_line_number_by_title(file_name, title):
    file_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            file_list.append(line.split("\t"))
        counter = 0
        for k in file_list:
            counter += 1
            if title == k[0]:
                return counter
        raise ValueError
