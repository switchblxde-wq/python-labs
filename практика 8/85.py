import pathlib  # Подключаю пути, чтобы аккуратно обращаться к файлам.
import subprocess  # Подключаю запуск внешних команд.
import sys  # Подключаю доступ к текущему интерпретатору.

base_dir = pathlib.Path(__file__).resolve().parent  # Определяю папку текущей практики.
report_path = base_dir / 'coverage_report.txt'  # Задаю путь, куда сохранить отчёт.

command = [sys.executable, '-m', 'coverage', 'run', '-m', 'unittest', 'test_84_nose2.py']  # Собираю команду запуска покрытия.
result = subprocess.run(command, cwd=base_dir, capture_output=True, text=True)  # Выполняю команду и собираю вывод.

if result.returncode != 0:  # Если тесты завершились с ошибкой.
    print('Не получилось запустить coverage. Сначала проверьте установку пакета coverage.')  # Печатаю понятную подсказку.
    print(result.stdout)  # Показываю стандартный вывод.
    print(result.stderr)  # Показываю текст ошибки.
else:  # Если запуск прошёл успешно.
    report_command = [sys.executable, '-m', 'coverage', 'report', '-m']  # Собираю команду текстового отчёта.
    report = subprocess.run(report_command, cwd=base_dir, capture_output=True, text=True)  # Получаю отчёт по покрытию.
    report_path.write_text(report.stdout, encoding='utf-8')  # Сохраняю отчёт в файл.
    print('Отчёт по покрытию сохранён в coverage_report.txt')  # Сообщаю о готовом результате.
    print(report.stdout)  # Печатаю отчёт на экран.
