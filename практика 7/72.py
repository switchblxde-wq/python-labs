class MovieLibrary:  # Создаю класс простой библиотеки фильмов.
    def __init__(self):  # Конструктор класса.
        self.movies = []  # Тут храню список фильмов.

    def add_movie(self, title, director, year):  # Метод для добавления фильма.
        if not isinstance(title, str) or not title:  # Проверяю корректность названия.
            raise ValueError('Title must be a non-empty string')  # Ошибка при пустом названии.
        if not isinstance(director, str) or not director:  # Проверяю корректность режиссёра.
            raise ValueError('Director must be a non-empty string')  # Ошибка при пустом режиссёре.
        if not isinstance(year, int) or year < 1888:  # Проверяю год выпуска.
            raise ValueError('Year must be an integer >= 1888')  # Ошибка при неверном годе.
        self.movies.append({'title': title, 'director': director, 'year': year})  # Добавляю запись в список.

    def remove_movie(self, title):  # Метод удаления фильма по названию.
        for i, movie in enumerate(self.movies):  # Иду по всем фильмам с индексом.
            if movie['title'] == title:  # Сравниваю название.
                del self.movies[i]  # Удаляю найденный фильм.
                return  # Выхожу после удаления.
        raise KeyError(f"Movie with title '{title}' not found")  # Ошибка, если фильма нет.

    def get_movies_by_year(self, year):  # Метод поиска фильмов по году.
        if not isinstance(year, int):  # Проверяю тип года.
            raise TypeError('Year must be an integer')  # Ошибка при неверном типе.
        return [movie for movie in self.movies if movie['year'] == year]  # Возвращаю подходящие фильмы.
