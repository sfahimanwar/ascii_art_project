import pygame
  
pygame.init()

w = 80
h = 80

drawing_window = pygame.display.set_mode((w, h))

source_image = pygame.image.load("pic.png").convert()

drawing_window.blit(source_image, (0, 0))

external_file = open("Happy_Birthday.txt", "w")

for y in range(h):
	for x in range(w):
		(r, g, b, _) = drawing_window.get_at((x, y))
		luminance = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
		if luminance > 0.875:
			next_character = "@"
		elif luminance > 0.750:
			next_character = "#"
		elif luminance > 0.625:
			next_character = "*"
		elif luminance > 0.500:
			next_character = "+"
		elif luminance > 0.375:
			next_character = "="
		elif luminance > 0.250:
			next_character = "-"
		elif luminance > 0.125:
			next_character = ":"
		else:
			next_character = "."
		print(next_character, end="")
		print(next_character, file=external_file, end="")
	print()
	print(file=external_file)

external_file.close()	
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
