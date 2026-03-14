# комментарий
class MovieLibrary:
    # комментарий
    def __init__(self):
        # комментарий
        self.movies = []

    # комментарий
    def add_movie(self, title, director, year):
        # комментарий
        if not isinstance(title, str) or not title:
            # комментарий
            raise ValueError('Title must be a non-empty string')
        # комментарий
        if not isinstance(director, str) or not director:
            # комментарий
            raise ValueError('Director must be a non-empty string')
        # комментарий
        if not isinstance(year, int) or year < 1888:
            # комментарий
            raise ValueError('Year must be an integer >= 1888')
        # комментарий
        self.movies.append({'title': title, 'director': director, 'year': year})

    # комментарий
    def remove_movie(self, title):
        # комментарий
        for index, movie in enumerate(self.movies):
            # комментарий
            if movie['title'] == title:
                # комментарий
                del self.movies[index]
                # комментарий
                return
        # комментарий
        raise KeyError(f"Movie with title '{title}' not found")

    # комментарий
    def get_movies_by_year(self, year):
        # комментарий
        if not isinstance(year, int):
            # комментарий
            raise TypeError('Year must be an integer')
        # комментарий
        return [movie for movie in self.movies if movie['year'] == year]
