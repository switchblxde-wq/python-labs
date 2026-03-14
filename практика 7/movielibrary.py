class MovieLibrary:
    """Простая библиотека фильмов."""

    def __init__(self):
        self.movies = []  # список фильмов, каждый фильм — словарь с ключами title, director, year

    def add_movie(self, title, director, year):
        """Добавляет фильм в библиотеку."""
        if not isinstance(title, str) or not title:
            raise ValueError("Title must be a non-empty string")
        if not isinstance(director, str) or not director:
            raise ValueError("Director must be a non-empty string")
        if not isinstance(year, int) or year < 1888:  # первый фильм снят примерно в 1888
            raise ValueError("Year must be an integer >= 1888")
        self.movies.append({"title": title, "director": director, "year": year})

    def remove_movie(self, title):
        """Удаляет фильм по названию. Если фильм не найден, возбуждает KeyError."""
        for i, movie in enumerate(self.movies):
            if movie["title"] == title:
                del self.movies[i]
                return
        raise KeyError(f"Movie with title '{title}' not found")

    def get_movies_by_year(self, year):
        """Возвращает список фильмов за указанный год."""
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        return [movie for movie in self.movies if movie["year"] == year]
