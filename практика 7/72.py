# class for simple movie storage
class MovieLibrary:
    # create empty movies list
    def __init__(self):
        # store movie records here
        self.movies = []

    # add movie after validation
    def add_movie(self, title, director, year):
        # validate title field
        if not isinstance(title, str) or not title:
            # raise invalid title error
            raise ValueError('Title must be a non-empty string')
        # validate director field
        if not isinstance(director, str) or not director:
            # raise invalid director error
            raise ValueError('Director must be a non-empty string')
        # validate year field
        if not isinstance(year, int) or year < 1888:
            # raise invalid year error
            raise ValueError('Year must be an integer >= 1888')
        # append movie row
        self.movies.append({'title': title, 'director': director, 'year': year})

    # remove movie by title
    def remove_movie(self, title):
        # iterate over movie list
        for index, movie in enumerate(self.movies):
            # compare current title
            if movie['title'] == title:
                # remove found movie
                del self.movies[index]
                # finish method
                return
        # raise error when movie is missing
        raise KeyError(f"Movie with title '{title}' not found")

    # return movies for selected year
    def get_movies_by_year(self, year):
        # validate year type
        if not isinstance(year, int):
            # raise invalid year type error
            raise TypeError('Year must be an integer')
        # return filtered rows
        return [movie for movie in self.movies if movie['year'] == year]
