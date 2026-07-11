import json
import sys
from datetime import datetime

json_file = "tasks.json"

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

        ids = [task["id"] for task in tasks]
except:
    with open(json_file, "w") as file:
        file.write("[]")


if sys.argv[1] == "add":
    task_id = max(ids, default=0) + 1

    new_entry = {"id": task_id, "description": sys.argv[2], "status": "todo", "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    with open(json_file, "r+") as file:
        data = json.load(file)
        data.append(new_entry)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

    print(f"Task added successfully (ID: {task_id})")



elif sys.argv[1] == "update":
    task_id = int(sys.argv[2])

    with open(json_file, "r+") as file:
        data = json.load(file)
        for item in data:
            if item["id"] == int(sys.argv[2]):
                item['description'] = sys.argv[3]
                item['updatedAt'] =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break

        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

    print(f"Task changed successfully (ID: {task_id})")



elif sys.argv[1] == "delete":
    task_id = int(sys.argv[2])

    with open(json_file, "r+") as file:
        data = json.load(file)

        data = [item for item in data if item["id"] != task_id]

        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

    print(f"Task deleted successfully (ID: {task_id})")



elif sys.argv[1] == "mark-in-progress":
    task_id = int(sys.argv[2])

    with open(json_file, "r+") as file:
        data = json.load(file)
        for item in data:
            if item["id"] == int(sys.argv[2]):
                item['status'] = "in-progress"
                break

        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

    print(f"Task marked successfully (ID: {task_id})")



elif sys.argv[1] == "mark-done":
    task_id = int(sys.argv[2])

    with open(json_file, "r+") as file:
        data = json.load(file)
        for item in data:
            if item["id"] == int(sys.argv[2]):
                item['status'] = "done"
                break

        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

    print(f"Task marked successfully (ID: {task_id})")



elif sys.argv[1] == "list":
    with open(json_file, "r+") as file:
        data = json.load(file)
    try:
        if sys.argv[2] == "todo" or sys.argv[2] == "in-progress" or sys.argv[2] == "done":
            for item in data:
                if item['status'] == sys.argv[2]:
                    print(f"{item['status']}: \"{item['description']}\" (ID {item['id']})")
    except IndexError:
        for item in data:
            print(f"{item['status']}: \"{item['description']}\" (ID {item['id']})")
