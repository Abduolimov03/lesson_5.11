### Short Long Short
def solution(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b
### Correct the mistakes of the character recognition software
# def correct(s):
#     natija = ''
#     for i in s:
#         if i == '5':
#             natija += 'S'
#         elif i == '0':
#             natija += 'O'
#         elif i == '1':
#             natija += 'I'
#         else:
#             natija += i
#     return natija

### Fake Binary
# def fake_bin(x):
#     natija = ''
#     for i in x:
#         if i < '5':
#             natija += '0'
#         else:
#             natija += '1'
#     return natija

### Abbreviate a Two Word Name
# def abbrev_name(name):
#     x = name.split()
#     a = x[0][0].upper()
#     b = x[1][0].upper()
#     return f"{a}.{b}"

### Convert a string to an array
# def string_to_array(s):
#     return s.split() if s else ['']







# import os
#
# cpu_cores = os.cpu_count()
# print(cpu_cores)
from fileinput import filename
# import asyncio
#
# async def salom_ber():
#     print("Salom")
#     await asyncio.sleep(2)
#     print('Yana salom')
#
# async def world():
#     print("World")
#     await asyncio.sleep(3)
#     print("Yana world")
#
# async def xayr():
#     print("Xayr")
#     await asyncio.sleep(1)
#     print('Yana xayr')
#
# async def main():
#     await asyncio.gather(salom_ber(), world(), xayr())
#
# asyncio.run(main())

from multiprocessing import Pool
import os

from multiprocessing import Pool
import os

# def hisobla_fayl(fayl_nomi):
#     with open(fayl_nomi, 'r') as f:
#         tekst = f.read()
#         if tekst.isalpha():
#             return tekst
#     return len(tekst.split())

# print(hisobla_fayl(text1.txt))
# if __name__ == '__main__':
#     fayllar = ['text1.txt', 'text2.txt', 'text3.txt']
#     with Pool(processes=3) as pool:
#         natijalar = pool.map(hisobla_fayl, fayllar)
#




from multiprocessing import Pool

# from multiprocessing import Pool
#
#
# def fayl_yoz(args):
#     oqiladigan_fayl, yoziladigan_fayl = args
#     natija = []
#     with open(oqiladigan_fayl, 'r') as f:
#         for qator in f:
#             qator = qator.strip()
#             if qator.isalpha():
#                 natija.append(qator)
#
#     with open(yoziladigan_fayl, 'a') as f:
#         for qator in natija:
#             f.write(qator + '\n')
#
#     return f"{oqiladigan_fayl} → {yoziladigan_fayl}: {len(natija)} qator yozildi."
#
#
# if __name__ == '__main__':
#     fayllar = [
#         ('text1.txt', 'text11.txt'),
#         ('text2.txt', 'text22.txt'),
#         ('text3.txt', 'text33.txt')
#     ]
#     with Pool(processes=3) as pool:
#         natijalar = pool.map(fayl_yoz, fayllar)
#         for n in natijalar:
#             print(n)

