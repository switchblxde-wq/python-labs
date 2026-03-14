from pathlib import Path  # Импортирую путь к файлу.
import importlib.util  # Импортирую загрузку модуля по пути.

_module_path = Path(__file__).with_name('71.py')  # Указываю файл с заданием 71.
_spec = importlib.util.spec_from_file_location('practice7_task71', _module_path)  # Готовлю описание модуля.
_module = importlib.util.module_from_spec(_spec)  # Создаю пустой модуль.
_spec.loader.exec_module(_module)  # Загружаю код из файла.

filter_by_type = _module.filter_by_type  # Пробрасываю функцию со старым именем модуля.
