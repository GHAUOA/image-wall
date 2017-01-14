# -*- coding: utf-8 -*-
import os

"""
    Author: Grey Li
    Email: withlihui@gmail.com
    Git repository: https://github.com/greyli/image-wall
    This work based on impress.js which can be found at https://github.com/impress/impress.js
"""

class Impress(object):

    def __init__(self, username):
        self.slides = []
        self.z = 0
        self.username = username
        self.photo_folder = os.getcwd() + '/static/photos/' + username
        self.result = []

    def overview(self):
        x = self.half_row
        y = self.half_col
        z = self.z * 2

        return [x, y, z]

    def create(self):
        images = []
        # According the sum of images(multiple of 10, 10~100), use different layout: {sum: (col, row, height)}
        pos = {10: (2, 5, 5000), 20: (4, 5, 5000), 30: (5, 6, 5000), 40: (5, 8, 6000), 50: (5, 10, 7000),
               60: (6, 10, 8000), 70: (7, 10, 8000), 80: (8, 10, 8000), 90: (9, 10, 9000), 100: (10, 10, 10000)}

        for img in os.listdir(self.photo_folder):
            images.append(img)

        pic_sum = len(images)

        for length in pos.keys():
            if pic_sum in range(length - 10, length):
                col, row, self.z = pos[length-10]

        for x in range(400, 900 * row, 900):
            for y in range(300, 700 * col, 700):
                self.result.append((self.username + '/' + images.pop(), x, y, self.z))

        # find the center of the image wall
        self.half_row = 900 * row / 2
        self.half_col = 700 * col / 2

    def save(self):
        return self.result
