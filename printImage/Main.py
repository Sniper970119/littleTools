# -*- coding:utf-8 -*-
from PIL import ImageDraw
from PIL import Image


def draw_pic(im, data_list):
    """
    画图
    :param data_list: 坐标点列表
    :return:
    """
    draw = ImageDraw.Draw(im)
    color_list = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (160, 32, 240), (0, 0, 255), (0, 255, 255)]
    for i in range(len(data_list)):
        draw.line((data_list[i][0], data_list[i][1]) + (data_list[i][2], data_list[i][1]),
                  fill=color_list[int(i % len(color_list))], width=1)
        draw.line((data_list[i][0], data_list[i][1]) + (data_list[i][0], data_list[i][3]),
                  fill=color_list[int(i % len(color_list))], width=1)

        draw.line((data_list[i][0], data_list[i][3]) + (data_list[i][2], data_list[i][3]),
                  fill=color_list[int(i % len(color_list))], width=1)
        draw.line((data_list[i][2], data_list[i][1]) + (data_list[i][2], data_list[i][3]),
                  fill=color_list[int(i % len(color_list))], width=1)
    im.save('result.jpg')
    pass


def main():
    im = Image.open('./show/target.jpg')
    data_list = [[159, 125, 219, 335], [197, 110, 261, 373] , [1, 220, 211, 473], [276, 215, 332, 337],
                  [137, 110, 261, 373], [207, 144, 257, 244], [173, 156, 217, 236], [207, 144, 257, 244],
                 [180, 125, 206, 156], [198, 114, 240, 146], [273, 184, 198, 203], [159, 198, 191, 255]]
    draw_pic(im, data_list)
    pass


if __name__ == '__main__':
    main()
