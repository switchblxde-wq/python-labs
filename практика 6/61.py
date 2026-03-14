from itertools import product

def find_numbers(mask, n, max_num=10**9):
   
    parts = mask.split('*')
    if len(parts) == 1:
       
        template = parts[0]
        q_count = template.count('?')
        results = []
        for digits in product('0123456789', repeat=q_count):
            num_str = template
            for d in digits:
                num_str = num_str.replace('?', d, 1)
            num = int(num_str)
            if num <= max_num and num % n == 0:
                results.append(num // n)
        return results
    elif len(parts) == 2:
        
        left, right = parts
        base_len = len(left) + len(right)
        max_star_len = len(str(max_num)) - base_len
        if max_star_len < 0:
            return []
        results = []
     
        for star_len in range(max_star_len + 1):
           
            for star_digits in product('0123456789', repeat=star_len):
                star_str = ''.join(star_digits)
               
                q_left = left.count('?')
                for left_digits in product('0123456789', repeat=q_left):
                    left_str = left
                    for d in left_digits:
                        left_str = left_str.replace('?', d, 1)
                   
                    q_right = right.count('?')
                    for right_digits in product('0123456789', repeat=q_right):
                        right_str = right
                        for d in right_digits:
                            right_str = right_str.replace('?', d, 1)
                        
                        num_str = left_str + star_str + right_str
                        num = int(num_str)
                        if num <= max_num and num % n == 0:
                            results.append(num // n)
        return results
    else:
       
        raise NotImplementedError("Поддерживается только одна '*' в маске.")


mask = "1?*93?1?"   
n = 6254
sp1 = find_numbers(mask, n)
print(sp1)
