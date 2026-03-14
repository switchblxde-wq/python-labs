# описываем класс
class MovieLibrary:
    # описываем функцию
    def __init__(self):
        # сохраняем значение в переменную
        self.movies = []

    # описываем функцию
    def add_movie(self, title, director, year):
        # проверяем условие
        if not isinstance(title, str) or not title:
            # выбрасываем исключение
            raise ValueError('Title must be a non-empty string')
        # проверяем условие
        if not isinstance(director, str) or not director:
            # выбрасываем исключение
            raise ValueError('Director must be a non-empty string')
        # проверяем условие
        if not isinstance(year, int) or year < 1888:
            # выбрасываем исключение
            raise ValueError('Year must be an integer >= 1888')
        # выполняем действие
        self.movies.append({'title': title, 'director': director, 'year': year})

    # описываем функцию
    def remove_movie(self, title):
        # проходим цикл
        for index, movie in enumerate(self.movies):
            # проверяем условие
            if movie['title'] == title:
                # выполняем действие
                del self.movies[index]
                # выполняем действие
                return
        # выбрасываем исключение
        raise KeyError(f"Movie with title '{title}' not found")

    # описываем функцию
    def get_movies_by_year(self, year):
        # проверяем условие
        if not isinstance(year, int):
            # выбрасываем исключение
            raise TypeError('Year must be an integer')
        # возвращаем результат
        return [movie for movie in self.movies if movie['year'] == year]
