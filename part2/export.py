# Export functions

import reports

file = open("export.txt", "w")
file.write(str(get_most_played(file_name)) + "\n")
file.write(str(sum_sold(file_name)) + "\n")
file.write(str(get_selling_avg(file_name)) + "\n")
file.writ(str(count_longest_title(file_name)) + "\n")
file.write(str(get_date_avg(file_name)) + "\n")
file.write(str(get_game(file_name, title)) + "\n")
file.close()
