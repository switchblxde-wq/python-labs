from pathlib import Path  # Импортирую путь к файлу.
import importlib.util  # Импортирую загрузку модуля по пути.

_module_path = Path(__file__).with_name('72.py')  # Указываю файл с заданием 72.
_spec = importlib.util.spec_from_file_location('practice7_task72', _module_path)  # Готовлю описание модуля.
_module = importlib.util.module_from_spec(_spec)  # Создаю пустой модуль.
_spec.loader.exec_module(_module)  # Загружаю код из файла.

MovieLibrary = _module.MovieLibrary  # Пробрасываю класс со старым именем модуля.
