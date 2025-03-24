
def filter_logs_by_level(logs: list, level: str) -> list:
    # Фільтруємо лог-записи з відповідним рівнем логування
    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: list):
    counts = {}
    for log in logs:
        level = log["level"]
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts