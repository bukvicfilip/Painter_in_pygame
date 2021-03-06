import pygame
import numpy
import random
from collections import deque

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
saved_screens=[]
fill_button=False
save_button=False
plus=False
minus=False
grids=False
grids1=False
######
width_of_box=23
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color_of_box = [color_inactive, color_inactive, color_inactive]
active = [False, False, False]
input_box=[]
thickness=[5, 5]
n=0

for num in range(3):
	input_box.append(pygame.Rect(702+n, 32, width_of_box, 13))
	n+=26

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
		for cl in clr:
			#print(cl)
			if type(cl) is int: 
				if cl>255:
					cl=255
				elif cl=="":
					cl=0
		clr=[int(clr[0]), int(clr[1]), int(clr[2])]

		self.screen=screen
		self.toolbar = pygame.draw.rect(self.screen, color, position, border_radius=50)
		self.central = pygame.draw.rect(screen, clr, (x_rect, 5, 40, 30))
		self.color=(190,190, 190)
		self.color_pressed=(115, 115, 115)

	#Draws a palette on the toolbar
	def draw_palette(self, c):
		for n in range(len(x1)):
			colors[c]=[int(color) for color in colors[c]]
			pygame.draw.rect(self.screen, colors[c], (x1[n], 5, 20, 20))
			pygame.draw.rect(self.screen, colors[c+6], (x2[n], 5, 20, 20))
			pygame.draw.rect(self.screen, colors[c+18], (x1[n], 30, 20, 20))
			pygame.draw.rect(self.screen, colors[c+12], (x2[n], 30, 20, 20))
			c+=1
			n+=1

	#Draws buttons on the toolbar
	def draw_circle(self, x_pos, y_pos, pressed, plus, minus):
		x=595
		y=14
		if plus==False:
			pygame.draw.circle(screen, self.color, (x, y), 9)
		elif plus==True:
			pygame.draw.circle(screen, self.color_pressed, (x, y), 9)	
		if minus==False:
			pygame.draw.circle(screen, self.color, (x, y+25), 9)
		elif minus==True:
			pygame.draw.circle(screen, self.color_pressed, (x, y+25), 9)
		if pressed[0]==True:
			pygame.draw.circle(screen, self.color_pressed, (x+120, y+3), 12)
		elif pressed[0]==False:
			pygame.draw.circle(screen, self.color, (x+120, y+3), 12)
		if pressed[1]==True:
			pygame.draw.circle(screen, self.color_pressed, (x+145, y+3), 12)
		elif pressed[1]==False:
			pygame.draw.circle(screen, self.color, (x+145, y+3), 12)
		if pressed[2]==True:
			pygame.draw.circle(screen, self.color_pressed, (x+170, y+3), 12)
		elif pressed[2]==False:
			pygame.draw.circle(screen, self.color, (x+170, y+3), 12)
		screen.blit(plus_button, (587, 6))
		screen.blit(minus_button, (587, 31))
		screen.blit(letter_r, (707, 9))
		screen.blit(letter_b, (732, 9))
		screen.blit(letter_g, (757, 9))

	#Draws undo, remove and save button on the toolbar
	def draw_undo_and_x(self, fill_color, grids, grids1):
		screen.blit(undo_button, (620, 11))
		screen.blit(x_button, (660, 11))
		if fill_color==True:
			pygame.draw.circle(screen, self.color_pressed, (91, 27), 23)
		elif fill_color==False:
			pygame.draw.circle(screen, self.color, (91, 27), 23)
		screen.blit(save_button, (30, 11))
		if fill_color==True:
			pygame.draw.circle(screen, self.color_pressed, (91, 27), 23)
		elif fill_color==False:
			pygame.draw.circle(screen, self.color, (91, 27), 23)
		screen.blit(paint_bucket,(75, 11))
		if grids==True:
			pygame.draw.circle(screen, self.color_pressed, (144, 27), 23)
		elif grids==False:
			pygame.draw.circle(screen, self.color, (144, 27), 23)
		if grids1==True:
			pygame.draw.circle(screen, self.color_pressed, (195, 27), 23)
		elif grids1==False:
			pygame.draw.circle(screen, self.color, (195, 27), 23)
		screen.blit(grid_pic, (128, 13))
		screen.blit(grid1_pic, (179, 13))

	def text_rgb(self, text, color_of_box):
		n=0
		for box in input_box:
			txt_surface = base_font.render(str(round(int(text[n]))), True, (0, 0, 0))
			# Resize the box if the text is too long.
			input_box[n].w = width_of_box
			# Blit the text.
			screen.blit(txt_surface, (input_box[n].x+3, input_box[n].y+3))
			# Blit the input_box rect.
			pygame.draw.rect(screen, color_of_box[n], input_box[n], 2)
			n+=1

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
def pixel(surface, pos, color, thickness):
	color=[int(c) for c in color]
	surface.fill(color, (pos, thickness))

def draw_line(surface, color, start_pos, end_pos, width=1):
	pygame.draw.line(screen, color, start_pos, end_pos, width)

def coordinates(x1, x2, x0, x02, n):
	for num in range(6):
		x1.append(x0)
		x2.append(x02)
		x0+=25
		x02-=25

def fill(surface, position, fill_color):
    fill_color = surface.map_rgb(fill_color)  # Convert the color to mapped integer value.
    surf_array = pygame.surfarray.pixels2d(surface)  # Create an array from the surface.
    current_color = surf_array[position]

    frontier = [position]
    while len(frontier) > 0:
        x, y = frontier.pop()
        try:  # Add a try-except block in case the position is outside the surface.
            if surf_array[x, y] != current_color:
                continue
        except IndexError:
            continue
        surf_array[x, y] = fill_color
        # Then we append the neighbours of the pixel in the current position to our 'frontier' list.
        frontier.append((x + 1, y))  # Right.
        frontier.append((x - 1, y))  # Left.
        frontier.append((x, y + 1))  # Down.
        frontier.append((x, y - 1))  # Up.

    pygame.surfarray.blit_array(surface, surf_array)

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
paint_bucket=pygame.image.load("paint-bucket.png")
grid_pic=pygame.image.load("pixels.png")
grid1_pic=pygame.image.load("pixels1.png")

pygame.mouse.set_cursor(*pygame.cursors.diamond)

running = True
while running:
            

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONUP:
			xcor, ycor=pygame.mouse.get_pos()
			if 800>xcor>0 and 600>ycor>55:
				setsurface = screen.copy()
				saved_screens.append(setsurface)
			if 604>x>586 and 23>y>5 and plus==True:
				plus=False
			if 604>x>586 and 50>y>31 and minus==True:
				minus=False
			if 167>x>121 and 50>y>4 and grids==False:
				grids=True
			elif 167>x>121 and 50>y>4 and grids==True:
				grids=False
			if 217>x>171 and 50>y>4 and grids1==False:
				grids1=True
			elif 217>x>171 and 50>y>4 and grids1==True:
				grids1=False
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
			if 652>x>620 and 43>y>11:
				if len(saved_screens)>1:
					saved_screens.pop(-1)
					screen.blit(saved_screens[-1], (0, 0))
				else:
					print(saved_screens)
					screen.fill((255, 255, 255))
			if 167>x>121 and 50>y>4 and grids==False:
				grids=True
			elif 167>x>121 and 50>y>4 and grids==True:
				grids=False
			if 217>x>171 and 50>y>4 and grids1==False:
				grids1=True
			elif 217>x>171 and 50>y>4 and grids1==True:
				grids1=False
			if 102>x>75 and 43>y>11 and fill_button==False:
				fill_button=True
			elif 102>x>75 and 43>y>11 and fill_button==True:
				fill_button=False
			if event.button == 1 and fill_button==True:
				clr=[int(c) for c in clr]
				fill(screen, event.pos, clr)
			#Logic when you press "Save" button
			if 62>x>30 and 43>y>11:
				rect = pygame.Rect(0, 55, 800, 545)
				sub = screen.subsurface(rect)
				pygame.image.save(sub, "screenshot.png")
			if 604>x>586 and 23>y>5 and plus==False:
				plus=True
			if 604>x>586 and 50>y>31 and minus==False:
				minus=True

			for n, box in enumerate(input_box):
				if box.collidepoint(pygame.mouse.get_pos()):
					# Toggle the active variable.
					active[n]=True
					color_of_box[n]=color_active
				else:
					active[n]=False
					color_of_box[n]=color_inactive

		if event.type == pygame.KEYDOWN:
			for n, box in enumerate(input_box):
				if active[n]:
					if event.key == pygame.K_RETURN:
						clr[n]=str(clr[n])
					elif event.key == pygame.K_BACKSPACE:
						clr[n] = str(clr[n])
						clr[n]=clr[n][:-1]
					else:
						clr[n] = str(clr[n])
						clr[n] += event.unicode
				
	x, y = pygame.mouse.get_pos()

	#Checks when we press right button with mouse
	if pygame.mouse.get_pressed()[0]:
		if grids==True:
			draw_line(screen, clr, (x, y), (x+20,y+20))
		else:
			pixel(screen, (x, y), clr, thickness)

		for i in range(len(x1)):
			if x1[i]+25>x>x1[i] and 8<y<28:
				clr=colors[i]
				pixel(screen, (x, y), clr, thickness)
			if x2[i]+25>x>x2[i] and 8<y<28:
				clr=colors[i+6]
				pixel(screen, (x, y), clr, thickness)
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

		if grids==True:
			 thickness[0]-=0.2
			 thickness[1]-=0.2
			 if thickness[0]<1:
			 	thickness[0]=1
			 if thickness[1]<1:
			 	thickness[1]=1
		if grids1==True:
			thickness[0]+=0.2
			thickness[1]+=0.2

	paint=Menu([227,223, 245], (0, 0, width, 55), clr)
	paint.tap_to_save()
	paint.draw_palette(c)
	paint.draw_circle(x, y, pressed, plus, minus)
	paint.draw_undo_and_x(fill_button, grids, grids1)
	paint.text_rgb(clr, color_of_box)
	pygame.display.update()
	clock.tick(60)
pygame.quit()

 