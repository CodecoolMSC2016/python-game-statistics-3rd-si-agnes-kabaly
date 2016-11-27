
# Export functions

import reports

file = open("export.txt", "w")
file.write(str(reports.count_games("file_name")) + '\n')
file.write(str(reports.decide("file_name", year)) + '\n')
file.write(str(reports.get_latest("file_name")) + '\n')
file.write(str(reports.count_by_genre("file_name", genre)) + '\n')
file.write(str(reports.get_line_number_by_title("file_name", "title")) + '\n')
file.close()

