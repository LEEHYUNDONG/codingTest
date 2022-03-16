def solution(gems):
    answer = [1, 1000000]
    size = len(gems)
    msize = len(set(gems))
    l, r = 0, 0
    gemsDict = dict()
    ans = len(gems) + 1

    while r < size:
        if gems[r] not in gemsDict:
            gemsDict[gems[r]] = 1
        else:
            gemsDict[gems[r]] += 1
        r += 1
        if len(gemsDict) == msize:
            while l < r:
                if gemsDict[gems[l]] > 1:
                    gemsDict[gems[l]] -= 1
                    l += 1
                elif r - l < ans:
                    ans = r - l
                    answer = [l+1, r]
                    break
                else:
                    break

    return answer
