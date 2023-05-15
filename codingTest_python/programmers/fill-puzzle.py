import copy
def solution(game_board, table):
    answer = 0
    '''
    1. 우선 테이블에서 퍼즐 조각의 종류에 대하여 정리
    2. 게임 보드에서 퍼즐 조각이 들어갈 수 있는 자리 추출
    3. 1번에서 계산한 퍼즐 조각의 상하좌우를 막 돌려 게임보드에서 추출한 퍼즐조각의 모양과 일치하면 cnt++
    
    --- 퍼즐 조각 추출법 ---
    현위치에서 상하좌우를 기록 예를 들어
    시작->(0, 0), (0, 1), (0, 2) -> ㅁㅁㅁ 이런 모양
    시작->(0, 0), (1, 0), (2, 0) -> ㅁㅁㅁ -> 세로로된 모양 이렇게 원래 시작점에서의 더해진 좌표값을 구해야할듯
    end(끝점) - start(시작점)
    '''
    # 경계 체크
    def OOB(dx, dy):
        return 0 <= dx < N and 0 <= dy < M
    
    # 퍼즐 모양 추출
    def dfs(board, start_x, start_y, before_x, before_y, tmp, shape):
        for i in range(4):
            rx, ry = before_x + dx[i], before_y + dy[i]
            if OOB(rx, ry) and board[rx][ry] == shape:
                tmp.append([rx, ry])
                board[rx][ry] = 2
                dfs(board, start_x, start_y, rx, ry, tmp, shape)
        return board
    
    # 회전
    def rotate(game_board):
        n = len(game_board)
        rotated = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated[j][n - i - 1] = game_board[i][j]

        return rotated
    
    
    # 변수
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    N, M = len(game_board), len(game_board[0])
    puzzle = []
    g_board = copy.deepcopy(game_board)
    
    # table에서 퍼즐 구하기
    for i in range(N):
        for j in range(M):
            if table[i][j] == 1:
                tmp = []
                table[i][j] = 2
                tmp.append([i, j])
                dfs(table, i, j, i, j, tmp, 1)
                # puzzle 절대 좌표로 변형
                for k in range(len(tmp)):
                    tmp[k][0], tmp[k][1] = tmp[k][0]-i, tmp[k][1]-j
                puzzle.append(tmp)

    
    # game_board에서 모양 뽑기
    for q in range(4):
        game_board = rotate(game_board)
        g_board = copy.deepcopy(game_board)
        for i in range(N):
            for j in range(M):
                if g_board[i][j] == 0:
                    tmp = []
                    g_board[i][j] = 2
                    tmp.append([i, j])
                    g_board = dfs(g_board, i, j, i, j, tmp, 0)
                    # 계산한 빈 공간 모양을 돌려가면 puzzle에서 찾는 코드
                    # 만약에 돌린게 안에 있다면 puzzle에서 지우고 answer += len(puzzle)
                    for k in range(len(tmp)):
                        tmp[k][0], tmp[k][1] = tmp[k][0]-i, tmp[k][1]-j
                    if tmp in puzzle:
                        answer += len(tmp)
                        puzzle.remove(tmp)
                        game_board = copy.deepcopy(g_board)
                    else:
                        g_board = copy.deepcopy(game_board)
                        
                        
                        
    
    return answer