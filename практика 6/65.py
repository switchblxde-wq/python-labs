import unittest

def f4(numbers):
  
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    
    avg_even = sum(evens) / len(evens) if evens else 0
    avg_odd = sum(odds) / len(odds) if odds else 0
    
    if avg_even > avg_odd:
        return f"Среднее чётных ({avg_even:.2f}) больше среднего нечётных ({avg_odd:.2f})"
    elif avg_odd > avg_even:
        return f"Среднее нечётных ({avg_odd:.2f}) больше среднего чётных ({avg_even:.2f})"
    else:
        return f"Средние равны ({avg_even:.2f})"

def f5(a, b):
    
    if a > b:
        return b  
    else:
        return a


class TestFunctions(unittest.TestCase):
    
    
    def test_f4_mixed(self):
        self.assertEqual(f4([1, 2, 3, 4]), "Среднее чётных (3.00) больше среднего нечётных (2.00)")
    
    def test_f4_only_even(self):
        self.assertEqual(f4([2, 4, 6]), "Среднее чётных (4.00) больше среднего нечётных (0.00)")
    
    def test_f4_only_odd(self):
        self.assertEqual(f4([1, 3, 5]), "Среднее нечётных (3.00) больше среднего чётных (0.00)")
    
    def test_f4_empty(self):
        self.assertEqual(f4([]), "Средние равны (0.00)")
    
    def test_f4_equal(self):
        self.assertEqual(f4([1, 2, 3]), "Средние равны (2.00)")
    
  
    def test_f5_first_greater(self):
       
        self.assertEqual(f5(5, 3), 5, "Должен вернуть максимум 5, но вернул 3")
    
    def test_f5_second_greater(self):
       
        self.assertEqual(f5(3, 5), 5)
    
    def test_f5_equal(self):
     
        self.assertEqual(f5(4, 4), 4)

if __name__ == '__main__':
    unittest.main()