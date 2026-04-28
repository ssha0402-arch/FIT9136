def is_task_executable(task:dict, robots:list[dict], destinations:list[dict], packages:list[dict])->bool:
    """
   

    """
    
    source_zone = "source zone"
    target_zone = "target zone"
    for destination in destinations:
        if destination["destination_id"] == task["source_id"]:
            source_zone = destination["zone"]
        if destination["destination_id"] == task["target_id"]:
            target_zone = destination["zone"]
    if source_zone != target_zone:
        return False

    package = {}
    for row in packages:
        if row["package_id"] == task["package_id"]:
            package = row.copy()
            break

    robot_in_zone = []
    for robot in robots:
        if robot["zone"] == source_zone:
            robot_in_zone.append(robot)
    if robot_in_zone != []:
        available_robots = []
        for robot in robot_in_zone:
            if robot["max_load"] >= package["weight"]:
                available_robots.append(robot)
        if available_robots != []:
            return True
        else:
            return False
    else:
        return False

