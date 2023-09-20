# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#
# В случае с английским алфавитом очки распределяются так:
#
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
#
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
#
# Пример:
#
#
# k = 'ноутбук'
# # 12

k = 'ноутбук'
k = k.lower()
count = 0
o1 = 'АВЕИНОРСТ'.lower()
o2 = 'ДКЛМПУ'.lower()
o3 = 'БГЁЬЯ'.lower()
o5 = 'ЖЗХЦЧ'.lower()
o8 = 'ШЭЮ'.lower()
o10 = 'ФЩЪ'.lower()
o_1 = 'AEIOULNSTR'.lower()
o_2 = 'DG'.lower()
o_3 = 'BCMP'.lower()
o_4 = 'FHVWY'.lower()
o_5 = 'K'.lower()
o_8 = 'JX'.lower()
o_10 = 'QZ'.lower()


for i in range(len(k)):
    for j in range(len(o1)):
        if k[i] == o1[j]:
            count += 1
    for j in range(len(o2)):
        if k[i] == o2[j]:
            count += 2
    for j in range(len(o3)):
        if k[i] == o3[j]:
            count += 3
    for j in range(len(o5)):
        if k[i] == o5[j]:
            count += 5
    for j in range(len(o8)):
        if k[i] == o8[j]:
            count += 8
    for j in range(len(o10)):
        if k[i] == o10[j]:
            count += 10
    for j in range(len(o_1)):
        if k[i] == o_1[j]:
            count += 1
    for j in range(len(o_2)):
        if k[i] == o_2[j]:
            count += 2
    for j in range(len(o_3)):
        if k[i] == o_3[j]:
            count += 3
    for j in range(len(o_4)):
        if k[i] == o_4[j]:
            count += 4
    for j in range(len(o_5)):
        if k[i] == o_5[j]:
            count += 5
    for j in range(len(o_8)):
        if k[i] == o_8[j]:
            count += 8
    for j in range(len(o_10)):
        if k[i] == o_10[j]:
            count += 10
print(count)