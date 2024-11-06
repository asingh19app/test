from datetime import datetime

def clock_in(employee_id):
    time_in = datetime.now()
    print(f"Employee {employee_id} clocked in at {time_in}")
