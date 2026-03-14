# Создаём класс для хранения фильмов.
class MovieLibrary:
    # Инициализируем пустую библиотеку.
    def __init__(self):
        # Храним фильмы в обычном списке словарей.
        self.movies = []

    # Добавляем фильм в библиотеку после проверок.
    def add_movie(self, title, director, year):
        # Проверяем корректность названия.
        if not isinstance(title, str) or not title:
            # Выбрасываем ошибку при некорректном названии.
            raise ValueError('Название должно быть непустой строкой')
        # Проверяем корректность режиссёра.
        if not isinstance(director, str) or not director:
            # Выбрасываем ошибку при некорректном режиссёре.
            raise ValueError('Режиссёр должен быть непустой строкой')
        # Проверяем корректность года.
        if not isinstance(year, int) or year < 1888:
            # Выбрасываем ошибку при некорректном годе.
            raise ValueError('Год должен быть целым и не меньше 1888')
        # Добавляем новый фильм в коллекцию.
        self.movies.append({'title': title, 'director': director, 'year': year})

    # Удаляем фильм по названию.
    def remove_movie(self, title):
        # Проходим по всем фильмам вместе с индексами.
        for index, movie in enumerate(self.movies):
            # Сравниваем название текущего фильма с искомым.
            if movie['title'] == title:
                # Удаляем найденный фильм.
                del self.movies[index]
                # Завершаем метод после удаления.
                return
        # Выбрасываем ошибку, если фильм не нашли.
        raise KeyError(f'Фильм с названием {title} не найден')

    # Возвращаем список фильмов за указанный год.
    def get_movies_by_year(self, year):
        # Проверяем, что год целый.
        if not isinstance(year, int):
            # Выбрасываем ошибку при неверном типе.
            raise TypeError('Год должен быть целым числом')
        # Возвращаем отфильтрованный список по году.
        return [movie for movie in self.movies if movie['year'] == year]
