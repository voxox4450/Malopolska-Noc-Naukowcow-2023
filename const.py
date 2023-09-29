import os
import pygame
import cv2 as cv

WIDTH = 1500
HEIGHT = 850

YELLOW = (255, 255, 0)

planet_names = ['Słońce', 'Merkury', 'Wenus', "Ziemia", 'Mars', 'Jowisz', 'Saturn', 'Uran', 'Neptun']

path = os.path.join('US')
path2 = os.path.join('USG')
file_names = sorted(os.listdir(path))
file_names2 = sorted(os.listdir(path2))
BGs = []
BGs2 = []
for file_name in file_names:
    BGs.append(pygame.image.load(
        os.path.join(path, file_name)))
BGs_copy = BGs[:]

img_0 = cv.imread('US/1slonce.jpg')
img_1 = cv.imread('US/2merkury.jpg')
img_2 = cv.imread('US/3wenus.jpg')
img_3 = cv.imread('US/4ziemia.jpg')
img_4 = cv.imread('US/5mars.jpg')
img_5 = cv.imread('US/6jowisz.jpg')
img_6 = cv.imread('US/7saturn.jpg')
img_7 = cv.imread('US/8uran.jpg')
img_8 = cv.imread('US/9naptun.jpg')
BGs_notgray = [img_0, img_1, img_2, img_3, img_4, img_5, img_6, img_7, img_8]
BGs_gray = []
for BG in BGs_notgray:
    BGs_gray.append(cv.cvtColor(BG, cv.COLOR_BGR2GRAY))


'''Zapis obrazu '''
# for i in range(9):
#     cv.imwrite(f'USG/{i+1}obraz.jpg', BGs_gray[i]);
'''Sprawdzenie poprawnosci ESC wyłącza program'''
# key = ord('a')
# while key != ord('q'):
#     cv.imshow('win', BGs_gray[0])
#     k = cv.waitKey(10) & 0XFF
#     if k == 27:
#         break

for file_name2 in file_names2:
    BGs2.append(pygame.image.load(
        os.path.join(path2, file_name2)))
