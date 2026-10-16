from src.file_service import RunnerJsonFileReader, ActivityJsonDataReader, RunnerJsonFileWriter, ActivityJsonDataWriter
import logging
from src.validator import ActivityDataDictValidator

logging.basicConfig(level=logging.ERROR)

def main():
    pass
    
#     validator = ActivityDataDictValidator()

# # Invalid activity type
#     activity_1 = {"activity_id": "A001", "runner_id": "R001", "date": "2026-09-01", "activity_type": "Other", "duration_minutes": 45}

#     validator.validate(activity_1)

# # Invalid date
#     activity_2 = { "activity_id": "A002", "runner_id": "R001", "date": "2026-02-30", "activity_type": "Running", "duration_minutes": 45}

#     validator.validate(activity_2)

    
  
    # runners_json_file_reader = RunnerJsonFileReader()
    # runners = runners_json_file_reader.read('./data/runners.json')

    # for runner in runners:
    #     print(runner)

    # activity_json_file_reader = ActivityJsonDataReader()
    # activities = activity_json_file_reader.read('./data/activities.json')

    # for activity in activities:
    #     print(activity)

    
    # runners_data = [
    #     {"runner_id" : "R001", "first_name" : "Anna", "last_name":"Kowalska", "age": 32, "email": "anna.kowalska@example.com"},
    #     {"runner_id":"R002", "first_name":"Piotr", "last_name":"Nowak", "age":41, "email":"piotr.nowak@example.com"},
    #     {"runner_id":"R003", "first_name":"Marta", "last_name":"Wiśniewska", "age":27, "email":"marta.wisniewska@example.com"}
    # ]
    # runners = RunnerJsonFileWriter()
    # runners.write('./data/r_test.json', runners_data)



    # activity_data = [
    #     {"activity_id":"A001", "runner_id":"R001", "date": "2026-09-01", "activity_type": "RUNNING", "duration_minutes":45},
    #     {"activity_id":"A002", "runner_id":"R001", "date": "2026-09-03", "activity_type": "STRENGTH", "duration_minutes":50},
    #     {"activity_id":"A003", "runner_id":"R001", "date": "2026-09-05", "activity_type": "RUNNING", "duration_minutes":60},
    #     {"activity_id":"A004", "runner_id":"R002", "date": "2026-09-02", "activity_type": "RUNNING", "duration_minutes":55},
    #     {"activity_id":"A005", "runner_id":"R002", "date": "2026-09-04", "activity_type": "PILATES", "duration_minutes":45},
    #     {"activity_id":"A006", "runner_id":"R003", "date": "2026-09-01", "activity_type": "SWIMMING", "duration_minutes":40},
    #     {"activity_id":"A007", "runner_id":"R003", "date": "2026-09-06", "activity_type": "RUNNING", "duration_minutes":50},
    #     {"activity_id":"A008", "runner_id":"R001", "date": "2026-09-08", "activity_type": "PILATES", "duration_minutes":60}
    # ]

    # activities = ActivityJsonDataWriter()
    # activities.write('./data/a_test.json', activity_data)



if __name__ == "__main__":
    main()
