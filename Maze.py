# 입력값 0 1 2 3 str
# 0 = 빈 공간
# 1 = 벽
# 2 = 시작점
# 3 = 도착점

def main():
    # 1. 미로를 읽어들인다.
    maze = read_maze()


    #   -필요한 데이터를 추출한다.(시작점, 도착점)
    start_point(maze)
    end_point(maze)
    # 2. 미로의 경로를 계산한다.
    find_path(maze, start_point, end_point)

    pass

def read_maze():
    pass

def start_point(maze):
    pass

def end_point(maze):
    pass

def find_path(maze,start, end):
    pass