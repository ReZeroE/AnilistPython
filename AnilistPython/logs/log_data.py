import json
import os
import datetime


class LogData:
    '''
    Class responsible for logging the data generated from running the lib. Not in use.
    '''
    def __init__(self):
        self.log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs.json")

    def log_data(self, category, input, output):
        now = datetime.datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        log_dict = self.load_json(self.log_file_path)
        log_dict[date_time] = [category, input, output]

        with open(self.log_file_path, "w", encoding="utf-8") as f:
            json.dump(log_dict, f, indent=4)

    def load_json(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
