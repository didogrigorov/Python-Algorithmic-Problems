competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]

results = [0, 0, 1]

teams_dict = {}

for i in range(len(competitions)):
    if competitions[i][0] not in teams_dict:
      teams_dict[competitions[i][0]] = 0

    if competitions[i][1] not in teams_dict:
      teams_dict[competitions[i][1]] = 0

    if results[i] == 0:
        teams_dict[competitions[i][1]] += 3
    else:
        teams_dict[competitions[i][0]] += 3

sorted_dict = sorted(teams_dict.items(), key= lambda item: item[1], reverse=True)
print(sorted_dict[0][0])