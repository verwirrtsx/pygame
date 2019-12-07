import sys
import pygame
import math
from pygame.locals import *

white_site=[]
black_site=[]
text_show=''
pygame.init()
my_font = pygame.font.SysFont('宋体', 50)
size = width, height =800,800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("五子棋")
color=(249,214,91)
white =(255,255,255)
black =(0,0,0)
screen.fill(color)
def main():
	who = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pressed_array = pygame.mouse.get_pressed()
				if pressed_array[0] == 1:
					x = pygame.mouse.get_pos()[0]
					y = pygame.mouse.get_pos()[1]
					r_x = round(x/50)*50
					r_y= round(y/50)*50
					if [r_x,r_y] not in white_site and [r_x,r_y] not in black_site:
						if who == 0:
							who = 1
							black_site.append([r_x,r_y])
							if is_success('black') :
								show_win('Black')
						else:
							who =0
							white_site.append([r_x,r_y])
							if is_success('white') :
								show_win('White')
		for b in black_site:
			pygame.draw.circle(screen,black,(b[0],b[1]),20)
		for w in white_site:
			pygame.draw.circle(screen,white,(w[0],w[1]),20)
			# print(event)
		for i in range(17):
			pygame.draw.line(screen, (0, 0, 0), (0,i*50), (800, i*50),1)
			pygame.draw.line(screen, (0, 0, 0), (i*50,0), (i*50,800),1)
			pygame.draw.circle(screen,(0, 0, 0),(400,400),5)
			pygame.draw.circle(screen,(0, 0, 0),(200,200),5)
			pygame.draw.circle(screen,(0, 0, 0),(600,200),5)
			pygame.draw.circle(screen,(0, 0, 0),(200,600),5)
			pygame.draw.circle(screen,(0, 0, 0),(600,200),5)
			pygame.draw.circle(screen,(0, 0, 0),(600,600),5)
		pygame.display.flip()
def is_success(who):
	if who =='black':
		if left_top(black_site) or left_down(black_site) or x_line(black_site) or y_line(black_site) :
			return True
		else:
			return False
	else:
		if left_top(white_site) or left_down(white_site) or x_line(white_site) or y_line(white_site) :
			return True
		else:
			return False

def left_top(who):
	x_count = 0
	last_x = who[-1][0]
	last_y = who[-1][1]
	for i in range(4):
		if [(i+1)*50+last_x,last_y - (i+1)*50] in who :
			x_count =x_count+1
		if [last_x - (i+1)*50,last_y +(i+1)*50] in who :
			x_count =x_count+1
	if x_count >3:
		return True
	else:
		return False

def left_down(who):
	x_count = 0
	last_x = who[-1][0]
	last_y = who[-1][1]
	for i in range(4):
		if [(i+1)*50+last_x,(i+1)*50+last_y] in who :
			x_count =x_count+1
		if [last_x - (i+1)*50,last_y - (i+1)*50] in who :
			x_count =x_count+1
	if x_count >3:
		return True
	else:
		return False

def x_line(who):
	x_count = 0
	last_x = who[-1][0]
	last_y = who[-1][1]
	for i in range(4):
		if [(i+1)*50 + last_x,last_y] in who:
			x_count =x_count+1
		if [last_x - (i+1)*50 ,last_y] in who:
			x_count =x_count+1
	if x_count >3:
		return True
	else:
		return False

def y_line(who):
	x_count = 0
	last_x = who[-1][0]
	last_y = who[-1][1]
	for i in range(4):
		if [last_x,last_y+(i+1)*50] in who:
			x_count =x_count+1
		if [last_x,last_y-(i+1)*50] in who:
			x_count =x_count+1
	if x_count >3:
		return True
	else:
		return False
def show_win(who):
	text_show = my_font.render(who+'------win------',True,(255,0,0))
	screen.blit(text_show,(300,400))
	restart()
def restart():
	while 1:
		1
main()
