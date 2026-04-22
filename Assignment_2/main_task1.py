import sys

# Write your functions here.import sys

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
                    if str(row_list[column_num]) in ["pending", "complete"]:
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

def is_task_executable(task_id:str, package_ids:list[str], package_weights:list[float], robot_ids:list[str], max_loads:list[float], robot_zones:list[str], destination_ids:list[str], destination_zones:list[str], task_ids:list[str], source_ids:list[str], target_ids:list[str], task_package_ids:list[str])->bool:
    """
    task_id is required to fill
    package_ids         package_weights                                         are from read_packages
    robot_ids           max_loads           robot_zones                         are from read_robots
    destination_ids     destination_zones                                       are from read_destinations
    task_ids            source_ids          target_ids      task_package_ids    are from read_tasks
    """
    source_id = source_ids[task_ids.index(task_id)]
    target_id = target_ids[task_ids.index(task_id)]
    task_package_id = task_package_ids[task_ids.index(task_id)]
    package_weight = package_weights[package_ids.index(task_package_id)]
    source_zone = destination_zones[destination_ids.index(source_id)]
    target_zone = destination_zones[destination_ids.index(target_id)]
    if source_zone != target_zone:
        return False
    robot_in_zone = []
    for robot_num, robot in enumerate(robot_ids):
        if str(robot_zones[robot_num]) == source_zone:
            robot_in_zone.append(robot)
    available_robots = []
    for rob_in_zone_num, robot in enumerate(robot_in_zone):
        if float(max_loads[robot_ids.index(robot)]) >= package_weight:
            available_robots.append(robot)
    if available_robots != []:
        return True
    else:
        return False

def write_feasability_report(report_path:str,task_ids:list,results:list[bool]):
    report_ = "Task Feasibility Report\n\n"
    for task_num, task_id in enumerate(task_ids):
        if results[task_num]:
            report_ += str(task_id)+": "+str("executable\n")
        else:
            report_ += str(task_id)+": "+str("not executable\n")

    report_ += "\nExecutable tasks: "+ str(results.count(True))+"\nNon-executable tasks: "+str(results.count(False))
    
    with open(report_path,"w") as report:
        report.write(report_)
    return 0

def main(robots_path:str, destinations_path:str, packages_path:str, tasks_path:str, report_path:str)-> bool:
    robots_data         = read_robots(robots_path)
    destinations_data   = read_destinations(destinations_path)
    packages_data       = read_packages(packages_path)
    tasks_data          = read_tasks(tasks_path,destinations_data[0],packages_data[0])
    result = []
    for task_num, task_id in enumerate(tasks_data[0]):
        if is_task_executable(task_id,packages_data[0],packages_data[1],robots_data[0],robots_data[2],robots_data[3],destinations_data[0],destinations_data[1],tasks_data[0],tasks_data[1],tasks_data[2],tasks_data[3]):
            result.append(True)
        else:
            result.append(False)
    write_feasability_report(report_path,tasks_data[0],result)
    return 0










if __name__ == "__main__":
    # Write your test code here.
    robots_path         = "Assignment_2/task_csv/robots.csv"
    packages_path       = "Assignment_2/task_csv/packages.csv"
    destinations_path   = "Assignment_2/task_csv/destinations.csv"
    tasks_path          = "Assignment_2/task_csv/tasks.csv"
    report_path         = "Assignment_2/feasibility_report.txt"
    main(robots_path, destinations_path, packages_path, tasks_path, report_path)
