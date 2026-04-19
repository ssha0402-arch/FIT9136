import sys

# Write your functions here.

def read_robots(robots_path:str)->list:
    """
    This function should take a path to a CSV file containing information on the robots 
    and return an aligned list for each of the field contained in the CSV file, 
    in the order that they appear.
    """
    out_list = []
    with open(robots_path,"r") as fileref:
        file_lines = fileref.readlines()                            # stroe file as a list of lines
        title_list = list(file_lines[0].strip().split(","))         # stroe titles(columns) as a list from first line
        for column in title_list:                                   # create lists with the same quantity of titles(columns) in title_list
            out_list.append(list())
        for row_num, row in enumerate(file_lines[1:],start=1):      # read the part under the title
            row_list = list(row.strip().split(","))                 # stroe values in row as a list
            row_list_checked = [None]*len(title_list)               # set a temp list wait to be fill
            error_dict = {}
            for column_num, column_name in enumerate(title_list):

                ### VALUE CHECK ###
                if column_name == "battery_level" :                 # VALUE check for "battery_level"
                    try:
                        row_value = int(row_list[column_num])
                        if row_value >= 0 and row_value <= 100:
                            row_list_checked[column_num]=row_value
                        else:
                            error_dict[column_name]=row_list[column_num]
                    except:
                        error_dict[column_name]=row_list[column_num]
                elif column_name == "max_load":                     # VALUE check for "max_load"
                    try:
                        row_value = float(row_list[column_num])
                        if row_value >= 0 :
                            row_list_checked[column_num]=row_value
                        else:
                            error_dict[column_name]=row_list[column_num]
                    except:
                        error_dict[column_name]=row_list[column_num]
                elif column_name == "zone":                         # VALUE check for "zone"
                    try:
                        row_value = str(row_list[column_num])
                        if row_value != "" and row_value.isalpha() and row_value.isupper():
                            row_list_checked[column_num]=row_value
                        else:
                            error_dict[column_name]=row_list[column_num]
                    except:
                        error_dict[column_name]=row_list[column_num]
                ### VALUE CHECK ###

                else:                                               # Value no need to check
                    row_value = str(row_list[column_num])
                    row_list_checked[column_num]=row_value
            for error_item, error_value in error_dict.items():      # print stderr message
                name = (title_list[0].split("_"))[0]
                print("Warning:",name.capitalize(),str(row_list[0]),"has invalid",str(error_item),"("+str(error_value)+").",file=sys.stderr)
            if None not in row_list_checked:                        # check if temp list legal 
                for column_num, row_value in enumerate(row_list_checked):
                    out_list[column_num].append(row_value)          # write value in out_list
    return out_list

def read_destinations(destinations_path:str)->list:
    """
    This function should take a CSV file containing information on the destinations 
    and return an aligned list for each of the fields contained in the CSV file, 
    in the order that they appear.
    """
    out_list=[]
    with open(destinations_path,"r") as fileref:
        file_lines = fileref.readlines()                            # stroe file as a list of lines
        title_list = list(file_lines[0].strip().split(","))         # stroe titles(columns) as a list from first line
        for column in title_list:                                   # create lists with the same quantity of titles(columns) in title_list
            out_list.append(list())
        for row_num, row in enumerate(file_lines[1:],start=1):      # read the part under the title
            row_list = list(row.strip().split(","))                 # stroe values in row as a list
            row_list_checked = [None]*len(title_list)               # set a temp list wait to be fill
            error_dict = {}
            for column_num, column_name in enumerate(title_list):

                ### VALUE CHECK ###
                if column_name == "zone":                           # VALUE check for "zone"
                    try:
                        row_value = str(row_list[column_num])
                        if row_value != "" and row_value.isalpha() and row_value.isupper():
                            row_list_checked[column_num]=row_value
                        else:
                            error_dict[column_name]=row_list[column_num]
                    except:
                        error_dict[column_name]=row_list[column_num]
                ### VALUE CHECK ###

                else:                                               # Value no need to check
                    row_value = str(row_list[column_num])
                    row_list_checked[column_num]=row_value
            for error_item, error_value in error_dict.items():      # print stderr message
                name = (title_list[0].split("_"))[0]
                print("Warning:",name.capitalize(),str(row_list[0]),"has invalid",str(error_item),"("+str(error_value)+").",file=sys.stderr)                
            if None not in row_list_checked:                        # check if temp list legal 
                for column_num, row_value in enumerate(row_list_checked):
                    out_list[column_num].append(row_value)          # write value in out_list
    return out_list


def read_packages(packages_path:str)->list:
    """
    This function should take a CSV file containing information on the packages 
    and return an aligned list for each of the fields contained in the CSV file, 
    in the order that they appear.
    """
    out_list=[]
    with open(packages_path,"r") as fileref:
        file_lines = fileref.readlines()                            # stroe file as a list of lines
        title_list = list(file_lines[0].strip().split(","))         # stroe titles(columns) as a list from first line
        for column in title_list:                                   # create lists with the same quantity of titles(columns) in title_list
            out_list.append(list())
        for row_num, row in enumerate(file_lines[1:],start=1):      # read the part under the title
            row_list = list(row.strip().split(","))                 # stroe values in row as a list
            row_list_checked = [None]*len(title_list)               # set a temp list wait to be fill
            error_dict = {}
            for column_num, column_name in enumerate(title_list):
                
                ### VALUE CHECK ###
                if column_name == "weight":                         # VALUE check for "weight"
                    try:
                        row_value = float(row_list[column_num])
                        if row_value >= 0 :
                            row_list_checked[column_num]=row_value
                        else:
                            error_dict[column_name]=row_list[column_num]
                    except:
                        error_dict[column_name]=row_list[column_num]
                ### VALUE CHECK ###

                else:                                               # Value no need to check
                    row_value = str(row_list[column_num])
                    row_list_checked[column_num]=row_value
            for error_item, error_value in error_dict.items():      # print stderr message
                name = (title_list[0].split("_"))[0]
                print("Warning:",name.capitalize(),str(row_list[0]),"has invalid",str(error_item),"("+str(error_value)+").",file=sys.stderr)                
            if None not in row_list_checked:                        # check if temp list legal 
                for column_num, row_value in enumerate(row_list_checked):
                    out_list[column_num].append(row_value)          # write value in out_list
    return out_list


def read_tasks(tasks_path:str, destination_ids:list, package_ids:list)->list:
    """
    This function should take a CSV file containing information on the tasks 
    and return an aligned list for each of the fields contained in the CSV file, 
    in the order that they appear. 
    """
    out_list=[]
    with open(tasks_path,"r") as fileref:
        file_lines = fileref.readlines()                            # stroe file as a list of lines
        title_list = list(file_lines[0].strip().split(","))         # stroe titles(columns) as a list from first line
        for column in title_list:                                   # create lists with the same quantity of titles(columns) in title_list
            out_list.append(list())
        for row_num, row in enumerate(file_lines[1:],start=1):      # read the part under the title
            row_list = list(row.strip().split(","))                 # stroe values in row as a list
            row_list_checked = [None]*len(title_list)               # set a temp list wait to be fill
            error_dict = {}
            for column_num, column_name in enumerate(title_list):
                
                ### VALUE CHECK ###
                if column_name == "status":                         # VALUE check for "status"
                    if str(row_list[column_num]) == "pending" or str(row_list[column_num]) == "complete":
                        row_list_checked[column_num]=row_list[column_num]
                    else:
                        error_dict[column_name]=row_list[column_num]
                elif column_name == "source_id":                    # VALUE check for "source_id"
                    if row_list[column_num] in destination_ids:
                        row_list_checked[column_num]=row_list[column_num]
                    else:
                        error_dict[column_name]=row_list[column_num]
                elif column_name == "target_id":                    # VALUE check for "target_id"
                    if row_list[column_num] in destination_ids:
                        row_list_checked[column_num]=row_list[column_num]
                    else:
                        error_dict[column_name]=row_list[column_num]
                elif column_name == "package_id":                   # VALUE check for "package_id"
                    if row_list[column_num] in package_ids:
                        row_list_checked[column_num]=row_list[column_num]
                    else:
                        error_dict[column_name]=row_list[column_num]
                ### VALUE CHECK ###

                else:                                               # Value no need to check
                    row_value = str(row_list[column_num])
                    row_list_checked[column_num]=row_value
            for error_item, error_value in error_dict.items():      # print stderr message
                name = (title_list[0].split("_"))[0]
                print("Warning:",name.capitalize(),str(row_list[0]),"has invalid",str(error_item),"("+str(error_value)+").",file=sys.stderr)                
            if None not in row_list_checked:                        # check if temp list legal 
                for column_num, row_value in enumerate(row_list_checked):
                    out_list[column_num].append(row_value)          # write value in out_list
    return out_list




def is_task_executable(task_id, package_ids, package_weights, robot_ids, max_loads, robot_zones, destination_ids, destination_zones, task_ids, source_ids, target_ids, task_package_ids):
    """

    """
    return 0






if __name__ == "__main__":
    # Write your test code here.
    print("robots")
    print(read_robots       ("Assignment_2/Task1CSV26.04.14/robots.csv"))
    print("destinations")
    print(read_destinations ("Assignment_2/Task1CSV26.04.14/destinations.csv"))
    print("packages")
    print(read_packages     ("Assignment_2/Task1CSV26.04.14/packages.csv"))
    # print("tasks")
    print(read_tasks(
        "Assignment_2/Task1CSV26.04.14/tasks.csv",
        read_destinations("Assignment_2/Task1CSV26.04.14/destinations.csv")[0],
        read_packages("Assignment_2/Task1CSV26.04.14/packages.csv")[0]
    ))

