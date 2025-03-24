def parse_log_line(line: str):
    parts = line.split(" ")
    if len(parts) < 4:
        return None
    message = " ".join(parts[3:])
    log_data = {"date": parts[0], "time": parts[1], "level": parts[2], "message":message}
    return log_data 