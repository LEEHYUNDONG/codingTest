def solution(word, pages):
    answer = 0
    page = dict()
    pageInx = []
    res = dict()
    for i in range(len(pages)):
        s = ''
        link = ''
        cnt = 0
        for j in range(len(pages[i])-17):
            if "content=\"https://" == pages[i][j:j+17]:
                idx = j+17
                while pages[i][idx] != "\"":
                    s += pages[i][idx]
                    idx += 1
                pageInx.append([s, i])
                page[s] = []
                if s not in res.keys():
                    res[s] = [0, 0, 0, 0]

            if "<a href=\"https://" == pages[i][j:j+17]:
                idx = j+17
                while pages[i][idx] != "\"":
                    link += pages[i][idx]
                    idx += 1
                page[s].append(link)
                res[s][1] += 1
                link = ''

            # 기본 점수
            if word.lower() == pages[i][j:j+len(word)].lower() and not pages[i][j-1].isalpha() and not pages[i][j+len(word)].isalpha():
                res[s][0] += 1

        # print(page)

    for i in res.keys():
        if res[i][1] != 0:
            res[i][-1] = res[i][0]
            res[i][2] = res[i][0]/res[i][1]
        else:
            res[i][-1] = res[i][0]
            res[i][2] = 0

    for i in page.keys():
        for j in page[i]:
            if j in res.keys():
                res[j][-1] += res[i][2]

    res = sorted(res.items(), key=lambda x: x[-1])
    ans = []
    for i in pageInx:
        if res[-1][0] == i[0]:
            ans.append(i[1])

    ans.sort()
    return ans[0]
