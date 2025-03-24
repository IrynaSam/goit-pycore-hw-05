from collections import Counter

def filter_logs_by_level(logs: list, level: str) -> list:
    # Фільтруємо лог-записи з відповідним рівнем логування
    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: list):
    levels = [log["level"] for log in logs]
    return dict(Counter(levels))
    