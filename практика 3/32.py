import random
letters_upper = 'ABCDEFGHIRJKLMNOPQRSTUVWXYZ'  
letters_lower = 'abcdefghijklmnopqrstuvwxyz'  
digits = '0123456789'                         
symbols = '@#%_^!)(*?'                          
all_chars = letters_upper + letters_lower + digits + symbols
password = ''.join(random.choice(all_chars) for _ in range(12))
print("Сгенерированный пароль:", password)
