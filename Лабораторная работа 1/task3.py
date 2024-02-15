# TODO Найдите количество книг, которое можно разместить на дискете
disk_volume_Mb = 1.44
disk_volume_byte = disk_volume_Mb*1024*1024
page_number = 100
string_number = 50
symbol_number = 25
symbol_volume = 4
book_volume = page_number*string_number*symbol_number*symbol_volume
books_number = disk_volume_byte//book_volume
print("Количество книг, помещающихся на дискету:", int(books_number))
