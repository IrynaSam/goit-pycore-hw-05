import os
from parser import parse_log_line
def load_logs(file_path):
    log_list = []
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    data = line.strip("\n")
                    log_entry = parse_log_line(data)
                    if log_entry is not None:
                        log_list.append(log_entry)
                        
        except FileNotFoundError:
            print("File not founded")
    return log_list