def translate(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


words = {"mother": "madre", "father": "padre", 
         "grandmother": "abuela", "grandfather": "abuelo"}

translate(**words)
