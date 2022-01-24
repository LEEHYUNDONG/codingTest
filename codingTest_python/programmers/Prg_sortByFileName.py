def solution(files):
    answer = []
    tmp = []
    for i in range(len(files)):
        f = files[i].lower().strip()
        tmp.append(f)

    file = []
    idx = 0

    for i in tmp:
        head, num, tail = '', '', ''
        j = 0
        while not i[j].isdigit():
            head += i[j]
            j += 1

        while i[j].isdigit() and j < len(i)-1:
            if j == len(i) or len(num) >= 5:
                break
            num += i[j]
            j += 1
        if j == len(i)-1 and i[j].isdigit():
            num += i[j]
        tail = i[j:]
        file.append([head.lower(), int(num), tail, idx])
        idx += 1
    file.sort(key=lambda x: (x[0], x[1], x[-1]))
    answer = list(map(lambda x: files[x[-1]], file))

    return answer

# import re

# def string_split(s):
#     s = s.lower()
#     head= re.match('[\D]+',s)
#     number = re.search('[0-9]+',s)
#     file = [head[0], int(number[0]), s[number.end():]]
#     return file

# def solution(files):
#     new_files = []
#     for i, file in enumerate(files):
#         s_file = string_split(file.lower())
#         s_file.append(i)
#         new_files.append(s_file)
#     new_files.sort(key = lambda x : (x[0], x[1], x[-1]))
#     answer = list(map(lambda x : files[x[-1]], new_files))
#     return answer
