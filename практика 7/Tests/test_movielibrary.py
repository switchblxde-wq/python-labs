import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import unittest
from movielibrary import MovieLibrary

class TestMovieLibrary(unittest.TestCase):
  

    def setUp(self):
       
        self.lib = MovieLibrary()
        self.lib.add_movie("Inception", "Christopher Nolan", 2010)
        self.lib.add_movie("The Matrix", "Lana Wachowski, Lilly Wachowski", 1999)
        self.lib.add_movie("Interstellar", "Christopher Nolan", 2014)
        self.lib.add_movie("The Godfather", "Francis Ford Coppola", 1972)

    def test_add_movie(self):
       
        initial_count = len(self.lib.movies)
        self.lib.add_movie("Pulp Fiction", "Quentin Tarantino", 1994)
        self.assertEqual(len(self.lib.movies), initial_count + 1)
        # Проверяем, что фильм действительно добавился
        titles = [m["title"] for m in self.lib.movies]
        self.assertIn("Pulp Fiction", titles)

    def test_add_movie_invalid_input(self):
       
        with self.assertRaises(ValueError):
            self.lib.add_movie("", "Director", 2000)          
        with self.assertRaises(ValueError):
            self.lib.add_movie("Title", "", 2000)             
        with self.assertRaises(ValueError):
            self.lib.add_movie("Title", "Director", 1800)     
        with self.assertRaises(ValueError):
            self.lib.add_movie("Title", "Director", "2000")   

    def test_remove_movie(self):
        """Проверка удаления существующего фильма."""
        self.lib.remove_movie("The Matrix")
        titles = [m["title"] for m in self.lib.movies]
        self.assertNotIn("The Matrix", titles)
     
        self.assertIn("Inception", titles)
        self.assertEqual(len(self.lib.movies), 3)

    def test_remove_movie_not_found(self):
        """Проверка удаления несуществующего фильма — должно быть исключение."""
        with self.assertRaises(KeyError):
            self.lib.remove_movie("Avatar")

    def test_get_movies_by_year(self):
        """Проверка поиска фильмов по году."""
        movies_2010 = self.lib.get_movies_by_year(2010)
        self.assertEqual(len(movies_2010), 1)
        self.assertEqual(movies_2010[0]["title"], "Inception")

        movies_1999 = self.lib.get_movies_by_year(1999)
        self.assertEqual(len(movies_1999), 1)
        self.assertEqual(movies_1999[0]["title"], "The Matrix")

        movies_1972 = self.lib.get_movies_by_year(1972)
        self.assertEqual(len(movies_1972), 1)
        self.assertEqual(movies_1972[0]["title"], "The Godfather")

    
        movies_2020 = self.lib.get_movies_by_year(2020)
        self.assertEqual(movies_2020, [])

    def test_get_movies_by_year_invalid_type(self):
        """Передача нецелого года должна вызывать TypeError."""
        with self.assertRaises(TypeError):
            self.lib.get_movies_by_year("2010")

if __name__ == "__main__":
    unittest.main()