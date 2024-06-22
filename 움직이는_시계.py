#제작자: 5702523 안나원
#제작일: 2021년 4월 23일
#작품명: 세련된 남색의 현대적인 움직이는 아날로그 시계 프로그램

import sys, random, math, pygame
from pygame.locals import *
from datetime import datetime, date, time

def print_text(font,x,y,text,color=(255,255,255)):
    imgText = font.render(text,True,color)
    SURFACE.blit(imgText,(x,y))

def wrap_angle(angle):
    return angle % 360

#화면 크기 설정
sWidth = 600 
sHeight = 500
wCircle = 3

clBackground = (255, 255, 255)
clCircle = (0, 0, 0)
clTriangle = (0, 255, 0)
clLine = (255, 0, 0)

pygame.init() #초기화
SURFACE= pygame.display.set_mode((sWidth, sHeight))#서페이스 크기
pygame.display.set_caption("Analog Clock Demo") #게임 이름
font = pygame.font.Font(None,36) #폰트설정(기본폰트)

FPS = 60 # 프레임률
fpsClock = pygame.time.Clock()

#색 지정 및 변수 지정
black = 0,0,0
white = 255,255,255
blue= 0,255,0
red = 250,0,0

pos_x = 300
pos_y = 250
radius = 250
angle = 360
angle_c = 360

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    SURFACE.fill((0, 0, 100)) #배경색 새로 고침, 초침이 움직인 그림을 이 자리에 놓고 덮어쓰기
    pygame.draw.circle(SURFACE, clCircle, (sWidth/2, sHeight/2), sHeight/3, wCircle)#원 그리기

    for n in range(1,13):

        today = datetime.today() #datetime함수 사용
        hours = today.hour % 12 #시
        minutes = today.minute #분
        seconds = today.second #초

        hour_angle = wrap_angle(hours * (360/12) - 90) #시침 각도
        hour_angle = math.radians(hour_angle) 
        hour_x = math.cos(hour_angle)*(radius-80)
        hour_y = math.sin(hour_angle)*(radius-80)
        target = (pos_x+hour_x,pos_y+hour_y)
        pygame.draw.line(SURFACE,black,(pos_x,pos_y),target,25) 

        min_angle = wrap_angle(minutes*(360/60)-90) #분침 각도
        min_angle = math.radians(min_angle)
        min_x = math.cos(min_angle)*(radius-60)
        min_y = math.sin(min_angle)*(radius-60)
        target = (pos_x+min_x,pos_y+min_y)
        pygame.draw.line(SURFACE,blue,(pos_x,pos_y),target,12)

        sec_angle = wrap_angle(seconds*(360/60)-90) #초침 각도
        sec_angle = math.radians(sec_angle)
        sec_x = math.cos(sec_angle)*(radius-40)
        sec_y = math.sin(sec_angle)*(radius-40)
        target = (pos_x+sec_x,pos_y+sec_y)
        pygame.draw.line(SURFACE,red,(pos_x,pos_y),target,6)

        pygame.draw.circle(SURFACE,white,(pos_x,pos_y),15)
        print_text(font,0,0,"5702523 Ahn Na Won", white) #이름기재


    angle_c += 1
    if angle_c >= 360:
        angle_c = 0
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = r, g, b
    x = math.cos(math.radians(angle_c)) * radius
    y = math.sin(math.radians(angle_c)) * radius
    pos = (int(pos_x + x), int(pos_y + y))
    pygame.draw.circle(SURFACE, white, pos, 8, 0)

    #숫자
    for n in range(1, 13):
        angle = math.radians(n * (360 / 12)-90)
        x = math.cos(angle) * (radius - 20) - 10
        y = math.sin(angle) * (radius - 20) - 10
        print_text(font, pos_x + x, pos_y + y, str(n))
        print(pos_x+x,pos_y+y)

    #눈금
    for n in range(1, 61):
        min_angle = wrap_angle(n*(360/60)-90)
        min_angle = math.radians(min_angle)
        minOut_x = math.cos(min_angle)*(radius+5)-5 #5픽셀 눈금이동
        minOut_y = math.sin(min_angle)*(radius+5)
        min_x = math.cos(min_angle)*(radius-5)-5
        min_y = math.sin(min_angle)*(radius-5)
        target = (pos_x + minOut_x, pos_y + minOut_y)
        pygame.draw.line(SURFACE, white, (pos_x+min_x, pos_y+min_y), target, 2)


    pygame.display.update()
    fpsClock.tick(FPS)
