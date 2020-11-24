import pygame

#Initializing the pygame
pygame.init()
clock = pygame.time.Clock()

width=800
height=600
x_rect=380
clr=[255, 255, 255]
pressed=[False, False, False]
base_font=pygame.font.Font(None, 15)
base_font2=pygame.font.Font(None, 11)

#Colors from the palette
colors=[[0, 80, 239],[27, 161, 226], [0, 171, 169],
		[100, 118, 135], [109, 135, 100], [118, 96, 138],
		[229, 20, 0], [162, 0, 37], [216, 0, 115],
		[250, 104, 0], [240, 163, 10], [227, 200, 0],
		[0, 255, 0], [0, 128, 0], [128, 128, 0], 
		[0, 51, 0], [51, 51, 51], [0, 0, 0],
		[102, 0, 102], [153, 51, 102], [255, 128, 128],
		[128, 128, 128], [204, 204, 255], [255, 255, 255]]
x0=430
x02=350		
x1=[]
x2=[]
n=0
c=0
a=0

#Toolbar class
class Menu:
	def __init__(self, color, position, clr):
		self.screen=screen
		self.toolbar = pygame.draw.rect(self.screen, color, position, border_radius=50)
		self.central = pygame.draw.rect(screen, clr, (x_rect, 5, 40, 30))

	#Draws a palette on the toolbar
	def draw_palette(self, c):
		for n in range(len(x1)):
			pygame.draw.rect(self.screen, colors[c], (x1[n], 5, 20, 20))
			pygame.draw.rect(self.screen, colors[c+6], (x2[n], 5, 20, 20))
			pygame.draw.rect(self.screen, colors[c+18], (x1[n], 30, 20, 20))
			pygame.draw.rect(self.screen, colors[c+12], (x2[n], 30, 20, 20))
			c+=1
			n+=1

	#Draws buttons on the toolbar
	def draw_circle(self, x_pos, y_pos, pressed):
		x=595
		y=14
		color=(208,202, 230)
		color_pressed=(115, 115, 115)
		pygame.draw.circle(screen, color, (x, y), 9)
		pygame.draw.circle(screen, color, (x, y+25), 9)
		if pressed[0]==True:
			pygame.draw.circle(screen, color_pressed, (x+120, y+3), 12)
		elif pressed[0]==False:
			pygame.draw.circle(screen, color, (x+120, y+3), 12)
		if pressed[1]==True:
			pygame.draw.circle(screen, color_pressed, (x+145, y+3), 12)
		elif pressed[1]==False:
			pygame.draw.circle(screen, color, (x+145, y+3), 12)
		if pressed[2]==True:
			pygame.draw.circle(screen, color_pressed, (x+170, y+3), 12)
		elif pressed[2]==False:
			pygame.draw.circle(screen, color, (x+170, y+3), 12)
		screen.blit(plus_button, (587, 6))
		screen.blit(minus_button, (587, 31))
		screen.blit(letter_r, (707, 9))
		screen.blit(letter_b, (732, 9))
		screen.blit(letter_g, (757, 9))

	#Draws undo, remove and save button on the toolbar
	def draw_undo_and_x(self):
		screen.blit(undo_button, (620, 11))
		screen.blit(x_button, (660, 11))
		screen.blit(save_button, (30, 11))

	#Draws text of rgb code
	def rgb_text(self, text):
		n=0
		for num, code in enumerate(text):
			text_surface=base_font.render(str(round(text[num])), True, (0, 0, 0))
			screen.blit(text_surface, (707+n, 35))
			n+=25

	def tap_to_save(self):
		text_surface2=base_font2.render("CLICK TO SAVE", True, (0, 0, 0))
		text_surface3=base_font2.render("THE COLOR", True, (0, 0, 0))
		screen.blit(text_surface2, (374, 37))
		screen.blit(text_surface3, (380, 44))


# Screen creating
screen = pygame.display.set_mode((width, height), 
	flags = pygame.RESIZABLE)
screen.fill((255, 255, 255))

#Filling in pixels
def pixel(surface, pos, color):
    surface.fill(color, (pos, (5, 5)))

def coordinates(x1, x2, x0, x02, n):
	for num in range(6):
		x1.append(x0)
		x2.append(x02)
		x0+=25
		x02-=25

coordinates(x1, x2, x0, x02, n)

#Title, pictures and Icon
pygame.display.set_caption("Painter")
icon = pygame.image.load("paintbrush.png")
pygame.display.set_icon(icon)
undo_button=pygame.image.load("undo-arrow.png")
x_button=pygame.image.load("close.png")
plus_button=pygame.image.load("add.png")
minus_button=pygame.image.load("minus.png")
letter_r=pygame.image.load("r.png")
letter_g=pygame.image.load("b.png")
letter_b=pygame.image.load("g.png")
save_button=pygame.image.load("download.png")

pygame.mouse.set_cursor(*pygame.cursors.diamond)

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if 703<x<727 and 5<y<29 and pygame.mouse.get_pressed()[0]==True and pressed[0]==False:
				pressed[0]=True
			elif 703<x<727 and 5<y<29 and pygame.mouse.get_pressed()[0]==True and pressed[0]==True:
				pressed[0]=False
			if 728<x<752 and 5<y<29 and pygame.mouse.get_pressed()[0]==True and pressed[1]==False:
				pressed[1]=True
			elif 728<x<752 and 5<y<29 and pygame.mouse.get_pressed()[0]==True and pressed[1]==True:
				pressed[1]=False
			if 753<x<802 and 5<y<29 and pygame.mouse.get_pressed()[0]==True and pressed[2]==False:
				pressed[2]=True
			elif 753<x<802 and 5<y<29 and pygame.mouse.get_pressed()[0]==True and pressed[2]==True:
				pressed[2]=False
			if 410>x>380 and 48>y>8:
				colors.pop(1)
				colors.append(clr)

	x, y = pygame.mouse.get_pos()

	#Checks when we press right button with mouse
	if pygame.mouse.get_pressed()[0]:
		pixel(screen, (x, y), clr)

		for i in range(len(x1)):
			if x1[i]+25>x>x1[i] and 8<y<28:
				clr=colors[i]
				pixel(screen, (x, y), clr)
			if x2[i]+25>x>x2[i] and 8<y<28:
				clr=colors[i+6]
				pixel(screen, (x, y), clr)
			if x1[i]+25>x>x1[i] and 30<y<50:
				clr=colors[i+18]
			if x2[i]+25>x>x2[i] and 30<y<50:
				clr=colors[i+12]

		#Adding when you press "+"
		if 604>x>586 and 23>y>5 and pressed[0]==True:
			if clr[0]<255:
				clr=(clr[0]+0.1,clr[1],clr[2])
			else:
				pass
		if 604>x>586 and 23>y>5 and pressed[1]==True:
			if clr[1]<255:
				clr=(clr[0],clr[1]+0.1,clr[2])
			else:
				pass
		if 604>x>586 and 23>y>5 and pressed[2]==True:
			if clr[2]<255:
				clr=(clr[0],clr[1],clr[2]+0.1)
			else:
				pass
		#Subtraction when you press "-"
		if 604>x>586 and 48>y>30 and pressed[0]==True:
			if clr[0]>0:
				clr=(clr[0]-0.1,clr[1],clr[2])
			else:
				pass
		if 604>x>586 and 48>y>30 and pressed[1]==True:
			if clr[1]>0:
				clr=(clr[0],clr[1]-0.1,clr[2])
			else:
				pass
		if 604>x>586 and 48>y>30 and pressed[2]==True:
			if clr[2]>0:
				clr=(clr[0],clr[1],clr[2]-0.1)
			else:
				pass

		#Logic when you press "X" button
		if 695>x>660 and 40>y>11:
			screen.fill((255, 255, 255))

		#Logic when you press "Save" button
		if 62>x>30 and 43>y>11:
			rect = pygame.Rect(0, 55, 800, 545)
			sub = screen.subsurface(rect)
			pygame.image.save(sub, "screenshot.png")

	paint=Menu([227,223, 245], (0, 0, width, 55), clr)
	paint.tap_to_save()
	paint.draw_palette(c)
	paint.draw_circle(x, y, pressed)
	paint.draw_undo_and_x()
	paint.rgb_text(clr)
	pygame.display.update()
	clock.tick(60)
pygame.quit()
