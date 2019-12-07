import sys
import pygame
import math
from pygame.locals import *

pygame.init()
my_font = pygame.font.SysFont('宋体', 50)
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("五子棋")
screen.fill((249,214,91))

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
class Five():
	who=0
	white_site=[]
	black_site=[]
	show = 1
	def __init__(self):
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
						if [r_x,r_y] not in self.white_site and [r_x,r_y] not in self.black_site:
							if self.who == 0:
								self.who = 1
								self.black_site.append([r_x,r_y])
								if self.is_success('black') :
									self.show_win('Black')
							else:
								self.who =0
								self.white_site.append([r_x,r_y])
								if self.is_success('white') :
									self.show_win('White')
			if self.show ==1 :
				for b in self.black_site:
					pygame.draw.circle(screen,(0,0,0),(b[0],b[1]),20)
				for w in self.white_site:
					pygame.draw.circle(screen,(255,255,255),(w[0],w[1]),20)
				pygame.display.update()
	def is_success(self,who):
		if who =='black':
			if self.left_top(self.black_site) or self.left_down(self.black_site) or self.x_line(self.black_site) or self.y_line(self.black_site) :
				return True
			else:
				return False
		else:
			if self.left_top(self.white_site) or self.left_down(self.white_site) or self.x_line(self.white_site) or self.y_line(self.white_site) :
				return True
			else:
				return False

	def left_top(self,who):
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

	def left_down(self,who):
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

	def x_line(self,who):
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

	def y_line(self,who):
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
	def show_win(self,who):
		self.show =0
		text_show = my_font.render(who+'------win------',True,(255,0,0))
		screen.blit(text_show,(100,400))
		screen.fill((0,0,0))
		screen.blit(text_show,(300,400))
		pygame.display.update()
f =Five()



