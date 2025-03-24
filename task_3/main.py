import sys
from loader import load_logs
from filter import filter_logs_by_level
from filter import count_logs_by_level

def main():
    if len(sys.argv) < 2:
        print("Please provide the path to the log file.")
        return
    
    file_path = sys.argv[1]
    level = sys.argv[2].upper() if len(sys.argv) > 2 else None
    
    # Завантажуємо лог-файл
    logs = load_logs(file_path)
    
    # Рахуємо кількість логів по рівнях
    counts = count_logs_by_level(logs)
    
    # Виводимо загальну статистику
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for lvl, count in counts.items():
        print(f"{lvl:<17}| {count}")
    
    # Якщо заданий рівень — фільтруємо та виводимо повідомлення цього рівня
    if level:
        print(f"\nДеталі логів для рівня '{level}':")
        filtered_logs = filter_logs_by_level(logs, level)
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

    
if __name__ == "__main__":
    main()    

