def solution(word, pages):
    answer = 0
    page = dict()
    pageInx = []
    res = dict()
    for i in range(len(pages)):
        s = ''
        link = ''
        cnt = 0
        pag = pages[i].split('<meta property=\"og:url\" content=\"')[1].split('\"')[0]
        page[pag] = []
        for link_long in page.split('a href=\"')[1:]:
            tmp = link_long.split('\"')
            page[pag].append(tmp)
            if pag not in res.keys():
                res[tmp] = [0, 1, 0, 0]
            else:
                res[tmp][1] += 1
        pageInx.append([pag, i])
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

