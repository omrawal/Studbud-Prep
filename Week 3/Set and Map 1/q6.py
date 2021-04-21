def getDistinctYears(a):
    line_list = a.split('.')
    print(line_list)
    date_set = set()
    for i in line_list:
        date = i.split(" ")[-1]
        date_set.add(date)
    return date_set


a = 'UN was established on 24-10-1945.India got freedom on 15-08-1947.Soon after the world war 2 ended on 02-09-1945.The UN was established on 24-10-1945.'
print(getDistinctYears(a))
