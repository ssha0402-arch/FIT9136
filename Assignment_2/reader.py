import sys,re

# pattern for fullmatch
pattern_int = r"-?(0|[1-9]\d*)"
pattern_float = r"-?(0|[1-9]\d*)((\.\d*[1-9])|(\.0))?"
pattern_id = r"[A-Z]+(0|[1-9]\d*)"
pattern_zone = r"[A-Z]+"

def read_to_table(path:str)->list[dict]:
    """
    This function takes a csv file path and returns a list of dict
    every dict in returned list is the content of every row(without title row) in csv file
    every key in dict is from title row
    every value in dict is from every row 
    [{"title_1": "row_1_column_1", "title_2": "row_1_column_2"}, {"title_1": "row2_column_1", "title_2": "row_2_column_2"}]
    """
    with open(path,"r") as fileref:
        out_list = []
        file_lines = fileref.readlines()
        title_list = list(file_lines[0].strip().split(","))
        for row_num, row in enumerate(file_lines[1:],start=1):
            row_list = list(row.strip().split(","))
            row_dict = {}
            for colum_num, colum_name in enumerate(title_list):
                row_dict[colum_name]=row_list[colum_num]
            out_list.append(row_dict)
    return out_list

def read_robots(robots_path:str)->list[dict]:
    """
    This function takes a csv file path and returns a list of dict
    every value will be checked, if any value in a row is illegal, whole row won't be return
    [{"title_1": "row_1_column_1", "title_2": "row_1_column_2"}, {"title_1": "row2_column_1", "title_2": "row_2_column_2"}]
    """
    file_content = read_to_table(robots_path)
    out_list = []
    for row_num, row in enumerate(file_content):
        title_list = list(row.keys())
        row_checked = {}
        error_dict = {}
        for column_name, value in row.items():
            ### VALUE CHECK ###            
            if column_name == "robot_id":                           # VALUE check for "robot_id"
                if re.fullmatch(pattern_id,value):
                    row_checked[column_name] = value
                else:
                    error_dict[column_name] = value
            elif column_name == "battery_level" :                   # VALUE check for "battery_level"
                if re.fullmatch(pattern_int,value) and int(value)>=0 and int(value)<=100:
                    row_checked[column_name] = int(value)
                else:
                    error_dict[column_name] = value
            elif column_name == "max_load":                         # VALUE check for "max_load"
                if re.fullmatch(pattern_float,value) and float(value)>=0:
                    row_checked[column_name] = float(value)
                else:
                    error_dict[column_name] = value
            elif column_name == "zone":                             # VALUE check for "zone"
                if re.fullmatch(pattern_zone,value):
                    row_checked[column_name] = value
                else:
                    error_dict[column_name] = value
            ### VALUE CHECK ###            
            else:                                                   # Value no need to check
                value = str(value)
                row_checked[column_name] = value
        if error_dict == {}:
            out_list.append(row_checked)                            # add row into outlist
        else:
            for error_item, error_value in error_dict.items():      # print stderr message
                print("Warning:", (title_list[0].split("_"))[0].capitalize(), str(row[title_list[0]]),"has invalid",str(error_item),"("+str(error_value)+").",file=sys.stderr)
    return out_list

def read_destinations(destinations_path:str)->list[dict]:
    """
    This function takes a csv file path and returns a list of dict
    every value will be checked, if any value in a row is illegal, whole row won't be return
    [{"title_1": "row_1_column_1", "title_2": "row_1_column_2"}, {"title_1": "row2_column_1", "title_2": "row_2_column_2"}]
    """
    file_content = read_to_table(destinations_path)
    out_list = []
    for row_num, row in enumerate(file_content):
        title_list = list(row.keys())
        row_checked = {}
        error_dict = {}
        for column_name, value in row.items():
            ### VALUE CHECK ###
            if column_name == "destination_id":                      # VALUE check for "destination_id"
                if re.fullmatch(pattern_id,value):
                    row_checked[column_name] = value
                else:
                    error_dict[column_name] = value
            elif column_name == "zone":                             # VALUE check for "zone"
                if re.fullmatch(pattern_zone,value):
                    row_checked[column_name] = value
                else:
                    error_dict[column_name] = value
            ### VALUE CHECK ###            
            else:                                                   # Value no need to check
                value = str(value)
                row_checked[column_name] = value
        if error_dict == {}:
            out_list.append(row_checked)                            # add row into outlist
        else:
            for error_item, error_value in error_dict.items():      # print stderr message
                print("Warning:", (title_list[0].split("_"))[0].capitalize(), str(row[title_list[0]]),"has invalid",str(error_item),"("+str(error_value)+").",file=sys.stderr)
    return out_list

def read_packages(packages_path:str)->list[dict]:
    """
    This function takes a csv file path and returns a list of dict
    every value will be checked, if any value in a row is illegal, whole row won't be return
    [{"title_1": "row_1_column_1", "title_2": "row_1_column_2"}, {"title_1": "row2_column_1", "title_2": "row_2_column_2"}]
    """
    file_content = read_to_table(packages_path)
    out_list = []
    for row_num, row in enumerate(file_content):
        title_list = list(row.keys())
        row_checked = {}
        error_dict = {}
        for column_name, value in row.items():
            ### VALUE CHECK ###
            if column_name == "package_id":                           # VALUE check for "package_id"
                if re.fullmatch(pattern_id,value):
                    row_checked[column_name] = value
                else:
                    error_dict[column_name] = value
            elif column_name == "weight":                             # VALUE check for "weight"
                if re.fullmatch(pattern_float,value) and float(value)>=0:
                    row_checked[column_name] = float(value)
                else:
                    error_dict[column_name] = value
            ### VALUE CHECK ###
            else:                                                   # Value no need to check
                value = str(value)
                row_checked[column_name] = value
        if error_dict == {}:
            out_list.append(row_checked)                            # add row into outlist
        else:
            for error_item, error_value in error_dict.items():      # print stderr message
                print("Warning:", (title_list[0].split("_"))[0].capitalize(), str(row[title_list[0]]),"has invalid",str(error_item),"("+str(error_value)+").",file=sys.stderr)
    return out_list

def read_tasks(tasks_path:str, destination_ids:list, package_ids:list)->list[dict]:
    """
    This function takes a csv file path and returns a list of dict
    every value will be checked, if any value in a row is illegal, whole row won't be return
    [{"title_1": "row_1_column_1", "title_2": "row_1_column_2"}, {"title_1": "row2_column_1", "title_2": "row_2_column_2"}]
    """
    file_content = read_to_table(tasks_path)
    out_list = []
    for row_num, row in enumerate(file_content):
        title_list = list(row.keys())
        row_checked = {}
        error_dict = {}
        for column_name, value in row.items():
            ### VALUE CHECK ###
            if column_name == "task_id":                            # VALUE check for "task_id"
                if re.fullmatch(pattern_id,value):
                    row_checked[column_name] = value
                else:
                    error_dict[column_name] = value
            elif column_name == "status":                           # VALUE check for "status"
                if value in ["pending", "complete"]:
                    row_checked[column_name] = value
                else:
                    error_dict[column_name] = value
            elif column_name in ["source_id","target_id"]:          # VALUE check for "source_id" and "target_id"
                if re.fullmatch(pattern_id,value) and value in destination_ids:
                    row_checked[column_name] = value
                else:
                    error_dict[column_name] = value
            elif column_name == "package_id":                       # VALUE check for "package_id"
                if re.fullmatch(pattern_id,value) and value in package_ids:
                    row_checked[column_name] = value
                else:
                    error_dict[column_name] = value
            ### VALUE CHECK ###
            else:                                                   # Value no need to check
                value = str(value)
                row_checked[column_name] = value
        if error_dict == {}:
            out_list.append(row_checked)                            # add row into outlist
        else:
            for error_item, error_value in error_dict.items():      # print stderr message
                print("Warning:", (title_list[0].split("_"))[0].capitalize(), str(row[title_list[0]]),"has invalid",str(error_item),"("+str(error_value)+").",file=sys.stderr)
    return out_list

def read_schedules(schedules_path:str,robot_ids:list,task_ids:list)->list[dict]:
    """
    """
    out_list = []
    with open(schedules_path,"r") as fileref:
        file_lines = fileref.readlines()
        for row_num,row in enumerate(file_lines):
            line = list(row.strip().split(","))
            if len(line) < 3 :
                print("Warning, line",str(row_num), "is too short.",file=sys.stderr)
                continue
            error_dict = {}
            line_checked = []
            if re.fullmatch(pattern_id,line[0]):
                line_checked.append(line[0])
            else:
                error_dict["schedule_id"]=line[0]
            if re.fullmatch(pattern_id,line[1]) and line[1] in robot_ids:
                line_checked.append(line[1])
            else:
                error_dict["robot_id"]=line[1]
            for task_num,task_id in enumerate(line[2:]):
                if re.fullmatch(pattern_id,task_id) and task_id in task_ids :
                    line_checked.append(task_id)
                else:
                    error_dict["task"+str(task_num)]=task_id
            if error_dict=={}:
                out_list.append(dict(schedule_id=line[0],robot_id=line[1],task_ids=line[2:]))
            else:
                for err_name,err_value in error_dict.items():
                    if err_name == "schedule_id":
                        print("Warning: invalid schedule_id","("+str(err_value)+").",file=sys.stderr)
                    elif err_name == "robot_id":
                        print("Warning: invalid robot_id","("+str(err_value)+").",file=sys.stderr)
                    else:
                        print("Warning: invalid task_id","("+str(err_value)+").",file=sys.stderr)
        return(out_list)

def read_distances(distances_path:str)->list[list]:
    """
    """
    with open(distances_path,"r") as fileref:
        out_list=[]
        lines = fileref.readlines()
        for line in lines:
            row = []
            for value in list(line.strip().split(",")):
                row.append(float(value))
            out_list.append(row)
        return(out_list)
    










# if __name__ == "__main__":
#     # Write your test code here.
#     print("robots")
#     print(read_robots       ("Assignment_2/task_csv/robots.csv"))
#     print("destinations")
#     print(read_destinations ("Assignment_2/task_csv/destinations.csv"))
#     print("packages")
#     print(read_packages     ("Assignment_2/task_csv/packages.csv"))
#     print("tasks")
#     destination_ids = []
#     for row_num, row in enumerate(read_destinations("Assignment_2/task_csv/destinations.csv")):
#         destination_ids.append(row["destination_id"])
#     package_ids = []
#     for row_num, row in enumerate(read_packages("Assignment_2/task_csv/packages.csv")):
#         package_ids.append(row["package_id"])
#     print(read_tasks        ("Assignment_2/task_csv/tasks.csv",destination_ids,package_ids))

  

