# with open("数据.txt",encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.strip()
#         print(line)

# from datetime import *
# date_string = '2023-2-23 12:38:57'
# date =datetime.strptime(date_string, "%Y-%m-%d   %H:%M:%S")


# print(date)
# with open("数据ins.txt",encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines[1:]:
#         line = line.strip().replace("/","-")
#         print(dict(list(zip(lines[0].split(),line.split()))),",")

# from datetime import *
# date_string = '2023-2-23 12:38:57'
# date =datetime.strptime(date_string, "%Y-%m-%d   %H:%M:%S")

import re
def bulk_add(file_name,separator):
    with open(file_name,encoding="utf-8") as f:
        lines = f.readlines()
        records=[]
        first_line:str = lines[0].strip()
        first_line = first_line.replace("\t","")

        field_list = first_line.split(separator)
        for line in lines[1:]:
            #line = line.replace("\t"," ")
            one_record_list = line.strip().split(separator)
            for index,v in enumerate(one_record_list):
                v = v.replace("\t"," ")
                v = v.strip()
                one_record_list[index] = v
            # usr = Usr.objects.get(uid="780303f9-b0a1-4d7b-a7b4-d191daa85f47")
            #one_reocrd_dict = Outs(**dict(zip(field_list,one_record_list)),usr=usr)
            records.append(dict(zip(field_list,one_record_list)))
    #Outs.objects.bulk_create(records)
    print(records[0])

bulk_add("数据ins_bulk.txt",",")