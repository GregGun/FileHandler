import datetime

fileWriter = open("dummy.txt", "at")

current_date_time = datetime.datetime.now()
current_date = datetime.date.today().strftime("%d.%m.%Y")

print(current_date_time)
print(current_date)

fileWriter.write("| 2        | Hey     | " + current_date + "\n")
