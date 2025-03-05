# Input data: List of dictionaries
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"},
]


# Function to be passed to the map() function. Do not change this.
def mod(employee):
    return employee["name"] + "_" + employee["department"]


def to_mod_list(employee_list):
    """Modifies the employee list of dictionaries into list of employee-department strings"""
    return list(map(mod, employee_list))


def generate_usernames(mod_list):
    """Generates a list of usernames replacing spaces with underscores"""
    return [x.replace(" ", "_") for x in mod_list]


def map_id_to_initial(employee_list):
    """Maps employee first initial to their id"""
    return {emp["name"][0]: emp["id"] for emp in employee_list}


def main():
    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list:", mod_emp_list, "\n")

    print("List of usernames:", generate_usernames(mod_emp_list), "\n")

    print("Initials and ids:", map_id_to_initial(employee_list))


if __name__ == "__main__":
    main()
