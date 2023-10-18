# TODO Найдите количество книг, которое можно разместить на дискете
disketa = 1.44
stranic_in_book = 100
number_str_na_stranice = 50
count_sumbols = 25
ves_sumbol = 4

ves_sumbols_in_book = stranic_in_book * number_str_na_stranice * count_sumbols * ves_sumbol
ves_kb = ves_sumbols_in_book / 1024
disketa_kb = disketa * 1024
book_in_disketa = disketa_kb // ves_kb

print("Количество книг, помещающихся на дискету:", int(book_in_disketa))
