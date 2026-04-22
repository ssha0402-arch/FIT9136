import sys,re

def read_to_table(file_path:str)->list[dict]:
    """
    This function takes a csv file path and returns a list of dict
    every dict in returned list is the content of every row(without title row) in csv file
    every key in dict is from title row
    every value in dict is from every row 
    [{"title_1": "row_1_column_1", "title_2": "row_1_column_2"}, {"title_1": "row2_column_1", "title_2": "row_2_column_2"}]
    """
    with open(file_path,"r") as fileref:
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
            if True:
                continue
            
                # ### VALUE CHECK ###
                # if column_name == "battery_level" :                 # VALUE check for "battery_level"
                #     try:
                #         value = int(value)
                #         if value >= 0 and value <= 100:
                #             row_checked[column_name] = value
                #         else:
                #             error_dict[column_name] = value
                #     except:
                #             error_dict[column_name] = value
                # elif column_name == "max_load":                     # VALUE check for "max_load"
                #     try:
                #         value = float(value)
                #         if value >= 0 :
                #             row_checked[column_name] = value
                #         else:
                #             error_dict[column_name] = value
                #     except:
                #             error_dict[column_name] = value
                # elif column_name == "zone":                         # VALUE check for "zone"
                #     try:
                #         value = str(value)
                #         if value != "" and value.isalpha() and value.isupper():
                #             row_checked[column_name] = value
                #         else:
                #             error_dict[column_name] = value
                #     except:
                #             error_dict[column_name] = value
                # ### VALUE CHECK ###
            else:                                               # Value no need to check
                value = str(value)
                row_checked[column_name] = value

        if error_dict == {}:
            out_list.append(row_checked)                            # 
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

            # ### VALUE CHECK ###
            # if column_name == "zone":                               # VALUE check for "zone"
            #     try:
            #         value = str(value)
            #         if value != "" and value.isalpha() and value.isupper():
            #             row_checked[column_name] = value
            #         else:
            #             error_dict[column_name] = value
            #     except:
            #             error_dict[column_name] = value
            #     ### VALUE CHECK ###

            else:                                                   # Value no need to check
                value = str(value)
                row_checked[column_name] = value

        if error_dict == {}:
            out_list.append(row_checked)                            # 
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

            # ### VALUE CHECK ###
            # if column_name == "weight":                             # VALUE check for "weight"
            #     try:
            #         value = float(value)
            #         if value >= 0 :
            #             row_checked[column_name] = value
            #         else:
            #             error_dict[column_name] = error_dict[column_name]= value
            #     except:
            #             error_dict[column_name] = value
            #     ### VALUE CHECK ###

            else:                                                   # Value no need to check
                value = str(value)
                row_checked[column_name] = value

        if error_dict == {}:
            out_list.append(row_checked)                            # 
        else:
            for error_item, error_value in error_dict.items():      # print stderr message
                print("Warning:", (title_list[0].split("_"))[0].capitalize(), str(row[title_list[0]]),"has invalid",str(error_item),"("+str(error_value)+").",file=sys.stderr)
    return out_list

def read_tasks(tasks_path:str, destination_ids:dict, package_ids:dict)->list[dict]:
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

            # ### VALUE CHECK ###
            # if True:                                                ### HERE SHOULD HAVE A CHECK ###
            #     value = str(value)
            #     row_checked[column_name] = value
            # ### VALUE CHECK ###

            # else:                                                   # Value no need to check
            #     value = str(value)
            #     row_checked[column_name] = value

        if error_dict == {}:
            out_list.append(row_checked)                            # 
        else:
            for error_item, error_value in error_dict.items():      # print stderr message
                print("Warning:", (title_list[0].split("_"))[0].capitalize(), str(row[title_list[0]]),"has invalid",str(error_item),"("+str(error_value)+").",file=sys.stderr)
    return out_list



if __name__ == "__main__":
    # Write your test code here.
    # print("robots")
    # print(read_robots       ("Assignment_2/Task1CSV26.04.14/robots.csv"))
    # print("destinations")
    # print(read_destinations ("Assignment_2/Task1CSV26.04.14/destinations.csv"))
    # print("packages")
    # print(read_packages     ("Assignment_2/Task1CSV26.04.14/packages.csv"))
    # print("tasks")
    print(read_tasks        ("Assignment_2/Task1CSV26.04.14/tasks.csv"))

  

