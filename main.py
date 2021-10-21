from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = r"(\+7|8)[\s(]*(\d+)[\s)]*(\d+)[\s-]?(\d+)[\s-]?(\d+)[\s(]*([\w+]*[\s.]*[\d+]*)[\s)]*"
subst = r"+7(\2)\3-\4-\5 \6"
contacts_list2 = []
check_in = []
for cl in contacts_list:
    full_name = cl[0] + ' ' + cl[1] + ' ' + cl[2]
    list_full_name = re.findall("\w+", full_name)
    phone = re.sub(pattern, subst, cl[5])
    name = list_full_name[0]+list_full_name[1]
    if name in check_in:
        for people in contacts_list2:
            if list_full_name[0] == people[0] and list_full_name[1] == people[1]:
                if len(people[2]) < 1:
                    if len(list_full_name) == 3:
                        people[2] = list_full_name[2]
                if len(people[3]) < 1:
                    people[3] = cl[3]
                if len(people[4]) < 1:
                    people[4] = cl[4]
                if len(people[5]) < 1:
                    people[5] = phone
                if len(people[6]) < 1:
                    people[6] = cl[6]
    else:
        if len(list_full_name) == 3:
            contacts_list2.append([list_full_name[0],
                                      list_full_name[1],
                                      list_full_name[2],
                                      cl[3],
                                      cl[4],
                                      phone,
                                      cl[6]])
            check_in.append(name)
        else:
            contacts_list2.append([list_full_name[0],
                                      list_full_name[1],
                                      cl[2],
                                      cl[3],
                                      cl[4],
                                      phone,
                                      cl[6]])
            check_in.append(name)
pprint(contacts_list2)

with open("phonebook.csv", "w", encoding='UTF-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list2)
