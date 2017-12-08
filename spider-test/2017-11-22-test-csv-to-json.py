import csv
import json
#
# # 读csv文件
# def read_csv(file):
#     csv_rows = []
#     with open(file) as csvfile:
#         reader = csv.DictReader(csvfile)
#         title = reader.fieldnames
#         for row in reader:
#             csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
#         return csv_rows
#
# # 写json文件
# def write_json(data, json_file, format=None):
#     with open(json_file, "w") as f:
#         if format == "good":
#             f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
#         else:
#             f.write(json.dumps(data))
#
# write_json(read_csv('test_data.csv'), 'test_data.json', 'good')
def csv_to_json(file):
   # file = "test_data.csv"
   lines = open(file,"r",encoding="utf-8").readlines()
   lines = [line.strip() for line in lines]
   keys = lines[0].split(',')
   line_num =1
   total_lines = len(lines)
   parsed_datas = []
   while line_num < total_lines:
       values = lines[line_num].split(",")
       parsed_datas.append(dict(zip(keys,values)))
       line_num = line_num +1
   json_str = json.dumps(parsed_datas,ensure_ascii=False,indent=4)
   output_file = file.replace("csv","json")

   with open(output_file,"w",encoding="utf-8") as f:
       f.write(json_str)
