
from reader import read_robots, read_destinations, read_packages, read_tasks
from tasker import is_task_executable

def write_feasability_report(report_path:str,results:list[dict]):
    report_ = "Task Feasibility Report\n\n"
    executable_count = 0
    for result in results:
        if result["result"]:
            report_ += result["task_id"]+": "+str("executable\n")
            executable_count += 1
        else:
            report_ += result["task_id"]+": "+str("not executable\n")

    report_ += "\nExecutable tasks: "+ str(executable_count)+"\nNon-executable tasks: "+str(len(results)-executable_count)
    
    with open(report_path,"w") as report:
        report.write(report_)
    return 0

def main(robots_path:str, destinations_path:str, packages_path:str, tasks_path:str, report_path:str):
    robots          = read_robots(robots_path)
    destinations    = read_destinations(destinations_path)
    packages        = read_packages(packages_path)

    destination_ids = []
    package_ids = []
    for destination in destinations:
        destination_ids.append(destination["destination_id"])
    for package in packages:
        package_ids .append(package["package_id"])

    tasks           = read_tasks(tasks_path,destination_ids,package_ids)

    results = []
    for task in tasks:
        if is_task_executable(task,robots,destinations,packages):
            results.append(dict(task_id=task["task_id"],result=True))
        else:
            results.append(dict(task_id=task["task_id"],result=False))
    
    write_feasability_report(report_path,results)
