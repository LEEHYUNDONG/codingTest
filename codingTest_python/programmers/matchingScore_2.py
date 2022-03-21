import re


def solution(word, pages):
    webpage = []
    webpageName = []
    webpageGraph = dict()

    for page in pages:
        url = re.search(
            '<meta property="og:url" content="(\S+)"', page).group(1)
        score = 0
        for f in re.findall(r'[a-zA-Z]+', page.lower()):
            if f == word.lower():
                score += 1
        exLink = re.findall('<a href="(https://[\S]*)"', page)

        for link in exLink:
            if link not in webpageGraph.keys():
                webpageGraph[link] = [url]
            else:
                webpageGraph[link].append(url)
        webpageName.append(url)
        webpage.append([url, score, len(exLink)])
    maxV = 0
    res = 0
    for i in range(len(webpage)):
        url = webpage[i][0]
        score = webpage[i][1]

        if url in webpageGraph.keys():
            for link in webpageGraph[url]:
                a, b, c = webpage[webpageName.index(link)]
                score += (b/c)
        if maxV < score:
            maxV = score
            res = i
    return res
