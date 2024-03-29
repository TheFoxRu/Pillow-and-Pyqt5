# -*- coding: utf-8 -*-

#  Copyright (©) 2020.  TheFox

import os
import sys

import requests
from PIL import Image, ImageFilter
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap


def exit_func():
    """Выход из приложения"""
    sys.exit()


def visible_rotate_window_func():
    """Показ окна с переворотом"""
    # Всё, что показываем
    rotate_window.show()
    # Всё, что скрываем
    main_window.hide()


def visible_main_window_func():
    """Показ главного окна"""
    # Всё, что показываем
    main_window.show()
    # Всё, что скрываем
    rotate_window.hide()
    convert_window.hide()
    black_window.hide()
    filter_window.hide()


def visible_convert_window_func():
    """Показ окна конвертера"""
    # Всё, что показываем
    convert_window.show()
    # Всё, что скрываем
    main_window.hide()


def visible_black_window_func():
    """Показ окна превращения в чёрно - белое изображение"""
    # Всё, что показываем
    black_window.show()
    # Всё, что скрываем
    main_window.hide()


def visible_filter_window_func():
    """Показ окна фильтров"""
    # Всё, что показываем
    filter_window.show()
    # Всё, что скрываем
    main_window.hide()


def upload_image_func():
    """Загрузка изображения по ссылке и вывод его на экран"""

    url_line_edit = rotate_window.url_line_edit.text()
    if url_line_edit != '':
        response = requests.get(url_line_edit, stream=True)
        if url_line_edit.find('png') != -1:

            with open('original.png', 'wb') as f:
                f.write(response.content)

        elif url_line_edit.find('jpg') != -1:

            with open('original.jpg', 'wb') as f:
                f.write(response.content)

            image = Image.open('original.jpg')
            image.save('original.png', 'png')
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'original.jpg')
            os.remove(path)

        pixmap = QPixmap("original.png")

        rotate_window.first_image_label.setPixmap(pixmap)

        rotate_window.itog_image_label.setPixmap(pixmap)

        rotate_window.rotate_90_left_button.setEnabled(True)
        rotate_window.rotate_90_right_button.setEnabled(True)
        rotate_window.rotate_180_button.setEnabled(True)


    elif url_line_edit == '':

        filename = QtWidgets.QFileDialog.getOpenFileName(rotate_window, ("Open Image"), "", ("Image Files (*.png *.jpg)"))

        itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

        if itog_name.find('jpg') != -1:
            image = Image.open(itog_name)
            image.save('original.png', 'png')

        elif itog_name.find('png') != -1:
            image = Image.open(itog_name)
            image.save('original.png')

        pixmap = QPixmap("original.png")

        rotate_window.first_image_label.setPixmap(pixmap)

        rotate_window.itog_image_label.setPixmap(pixmap)

        rotate_window.rotate_90_left_button.setEnabled(True)
        rotate_window.rotate_90_right_button.setEnabled(True)
        rotate_window.rotate_180_button.setEnabled(True)


def rotate_left_90_func():
    """Перевернуть изображение на 90 градусов влево"""

    try:
        rotate_retry = Image.open('rotated.png')
        rotated_retry_one = rotate_retry.rotate(90, expand=True)
        rotated_retry_one.save('rotated.png')
        pixmap = QPixmap("rotated.png")


    except:
        isxodnoe = Image.open("original.png")
        rotated = isxodnoe.rotate(90, expand=True)
        rotated.save('rotated.png')
        pixmap = QPixmap("rotated.png")

    rotate_window.itog_image_label.setPixmap(pixmap)


def rotate_right_90_func():
    """Перевернуть изображение на 90 градусов вправо"""

    try:
        rotate_retry = Image.open('rotated.png')
        rotated_retry_one = rotate_retry.rotate(-90, expand=True)
        rotated_retry_one.save('rotated.png')
        pixmap = QPixmap("rotated.png")


    except:
        isxodnoe = Image.open("original.png")
        rotated = isxodnoe.rotate(-90, expand=True)
        rotated.save('rotated.png')
        pixmap = QPixmap("rotated.png")

    rotate_window.itog_image_label.setPixmap(pixmap)


def rotate_180_func():
    """Перевернуть изображение на 180 градусов"""

    try:
        rotate_retry = Image.open('rotated.png')
        rotated_retry_one = rotate_retry.rotate(180, expand=True)
        rotated_retry_one.save('rotated.png')
        pixmap = QPixmap("rotated.png")


    except:
        isxodnoe = Image.open("original.png")
        rotated = isxodnoe.rotate(180, expand=True)
        rotated.save('rotated.png')
        pixmap = QPixmap("rotated.png")

    rotate_window.itog_image_label.setPixmap(pixmap)


def convert_jpg_to_png_func():
    """Конвертировать из jpg в png"""
    convert_line_edit = convert_window.convert_line_edit.text()
    if convert_line_edit != '':
        response = requests.get(convert_line_edit, stream=True)

        with open('Jpg_Image.jpg', 'wb') as f:
            f.write(response.content)

        jpg = Image.open("Jpg_Image.jpg")
        jpg.save('Png_Image.png', 'png')
        QtWidgets.QMessageBox.about(convert_window, "Уведомление", "Ваше изображение успешно конвертировано")

    elif convert_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(rotate_window, ("Open Image"), "", ("Image Files (*.jpg)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.save('Png_Image.png', 'png')
            QtWidgets.QMessageBox.about(convert_window, "Уведомление", "Ваше изображение успешно конвертировано")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(convert_window, "Ошибка", "Что-то пошло не так")


def convert_png_to_jpg_func():
    """Конвертировать из png в jpg"""
    convert_line_edit = convert_window.convert_line_edit.text()
    if convert_line_edit != '':
        response = requests.get(convert_line_edit, stream=True)

        with open('Png_Image.png', 'wb') as f:
            f.write(response.content)

        png = Image.open("Png_Image.png")

        png.convert("RGB").save('Jpg_Image.jpg')

        QtWidgets.QMessageBox.about(convert_window, "Уведомление", "Ваше изображение успешно конвертировано")
    elif convert_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(rotate_window, ("Open Image"), "", ("Image Files (*.png)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.save('Jpg_Image.jpg', 'jpg')
            QtWidgets.QMessageBox.about(convert_window, "Уведомление", "Ваше изображение успешно конвертировано")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(convert_window, "Ошибка", "Что-то пошло не так")


def sketch_black_and_white_func():
    """Сделать чёрно - белое изображение"""
    black_line_edit = black_window.black_and_white_line_edit.text()
    if black_line_edit != '':
        response = requests.get(black_line_edit, stream=True)
        if black_line_edit.find('png') != -1:

            with open('Regular_Image.png', 'wb') as f:
                f.write(response.content)

            black_and_white = Image.open("Regular_Image.png")
            black_and_white.convert("L").save('Black_And_White_Image.png')

        elif black_line_edit.find('jpg') != -1:
            with open('Regular_Image.jpg', 'wb') as f:
                f.write(response.content)

            black_and_white = Image.open("Regular_Image.jpg")

            black_and_white.convert("L").save('Black_And_White_Image.png')

        QtWidgets.QMessageBox.about(black_window, "Уведомление", "Ваше изображение успешно сделано чёрно-белым")
    elif black_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(black_window, ("Open Image"), "", ("Image Files (*.png *.jpg)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.convert('L').save('Black_And_White_Image.png')

            QtWidgets.QMessageBox.about(black_window, "Уведомление", "Ваше изображение успешно сделано чёрно-белым")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(black_window, "Ошибка", "Что-то пошло не так")


def blur_filter_image_func():
    """Сделать размытие на изображение"""
    filter_line_edit = filter_window.filter_line_edit.text()
    if filter_line_edit != '':
        response = requests.get(filter_line_edit, stream=True)
        if filter_line_edit.find('png') != -1:

            with open('Without_Filter.png', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.png")
            with_filter.filter(ImageFilter.BLUR).save('With_Blur_Filter.png')

            QtWidgets.QMessageBox.about(black_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Размытие")


        elif filter_line_edit.find('jpg') != -1:

            with open('Without_Filter.jpg', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.jpg")
            with_filter.filter(ImageFilter.BLUR).save('With_Blur_Filter.jpg')

            QtWidgets.QMessageBox.about(black_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Размытие")
    elif filter_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(filter_window, ("Open Image"), "", ("Image Files (*.png *.jpg)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.filter(ImageFilter.BLUR).save('With_Blur_Filter.png')

            QtWidgets.QMessageBox.about(black_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Размытие")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(black_window, "Ошибка", "Что-то пошло не так")


def contour_filter_image_func():
    """Сделать контур на изображение"""
    filter_line_edit = filter_window.filter_line_edit.text()
    if filter_line_edit != '':
        response = requests.get(filter_line_edit, stream=True)
        if filter_line_edit.find('png') != -1:

            with open('Without_Filter.png', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.png")

            with_filter.filter(ImageFilter.CONTOUR).save('With_Contour_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Контур")


        elif filter_line_edit.find('jpg') != -1:

            with open('Without_Filter.jpg', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.jpg")
            with_filter.filter(ImageFilter.CONTOUR).save('With_Contour_Filter.jpg')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Контур")
    elif filter_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(filter_window, ("Open Image"), "", ("Image Files (*.png *.jpg)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.filter(ImageFilter.CONTOUR).save('With_Contour_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Контур")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(filter_window, "Ошибка", "Что-то пошло не так")


def detail_filter_image_func():
    """Сделать детализацию на изображение"""
    filter_line_edit = filter_window.filter_line_edit.text()
    if filter_line_edit != '':
        response = requests.get(filter_line_edit, stream=True)
        if filter_line_edit.find('png') != -1:

            with open('Without_Filter.png', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.png")

            with_filter.filter(ImageFilter.DETAIL).save('With_Detail_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Детализация")


        elif filter_line_edit.find('jpg') != -1:

            with open('Without_Filter.jpg', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.jpg")
            with_filter.filter(ImageFilter.DETAIL).save('With_Detail_Filter.jpg')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Детализация")
    elif filter_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(filter_window, ("Open Image"), "", ("Image Files (*.png *.jpg)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.filter(ImageFilter.DETAIL).save('With_Detail_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Детализация")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(filter_window, "Ошибка", "Что-то пошло не так")


def edge_enhance_filter_image_func():
    """Сделать усиление краёв на изображение"""
    filter_line_edit = filter_window.filter_line_edit.text()
    if filter_line_edit != '':
        response = requests.get(filter_line_edit, stream=True)
        if filter_line_edit.find('png') != -1:

            with open('Without_Filter.png', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.png")

            with_filter.filter(ImageFilter.EDGE_ENHANCE).save('With_Edge_Enhance_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Усиление рельефа")


        elif filter_line_edit.find('jpg') != -1:

            with open('Without_Filter.jpg', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.jpg")
            with_filter.filter(ImageFilter.EDGE_ENHANCE).save('With_Edge_Enhance_Filter.jpg')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Усиление рельефа")
    elif filter_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(filter_window, ("Open Image"), "", ("Image Files (*.png *.jpg)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.filter(ImageFilter.EDGE_ENHANCE).save('With_Edge_Enhance_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Усиление рельефа")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(filter_window, "Ошибка", "Что-то пошло не так")


def edge_enhance_more_filter_image_func():
    """Сделать сильное усиление краёв на изображение"""
    filter_line_edit = filter_window.filter_line_edit.text()
    if filter_line_edit != '':
        response = requests.get(filter_line_edit, stream=True)
        if filter_line_edit.find('png') != -1:

            with open('Without_Filter.png', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.png")

            with_filter.filter(ImageFilter.EDGE_ENHANCE_MORE).save('With_Edge_Enhance_More_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Усиление рельефа(сильное)")


        elif filter_line_edit.find('jpg') != -1:

            with open('Without_Filter.jpg', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.jpg")
            with_filter.filter(ImageFilter.EDGE_ENHANCE_MORE).save('With_Edge_Enhance_More_Filter.jpg')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Усиление рельефа(сильное)")
    elif filter_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(filter_window, ("Open Image"), "", ("Image Files (*.png *.jpg)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.filter(ImageFilter.EDGE_ENHANCE_MORE).save('With_Edge_Enhance_More_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Усиление рельефа(сильное)")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(filter_window, "Ошибка", "Что-то пошло не так")


def emboss_filter_image_func():
    """Сделать тиснение на изображение"""
    filter_line_edit = filter_window.filter_line_edit.text()
    if filter_line_edit != '':
        response = requests.get(filter_line_edit, stream=True)
        if filter_line_edit.find('png') != -1:

            with open('Without_Filter.png', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.png")

            with_filter.filter(ImageFilter.EMBOSS).save('With_Emboss_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Тиснение")


        elif filter_line_edit.find('jpg') != -1:

            with open('Without_Filter.jpg', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.jpg")
            with_filter.filter(ImageFilter.EMBOSS).save('With_Emboss_Filter.jpg')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Тиснение")
    elif filter_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(filter_window, ("Open Image"), "", ("Image Files (*.png *.jpg)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.filter(ImageFilter.EMBOSS).save('With_Emboss_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Тиснение")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(filter_window, "Ошибка", "Что-то пошло не так")


def find_edges_filter_image_func():
    """Сделать выделение краёв на изображение"""
    filter_line_edit = filter_window.filter_line_edit.text()
    if filter_line_edit != '':
        response = requests.get(filter_line_edit, stream=True)
        if filter_line_edit.find('png') != -1:

            with open('Without_Filter.png', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.png")

            with_filter.filter(ImageFilter.FIND_EDGES).save('With_Find_Edges_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Выделение краёв")


        elif filter_line_edit.find('jpg') != -1:

            with open('Without_Filter.jpg', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.jpg")
            with_filter.filter(ImageFilter.FIND_EDGES).save('With_Emboss_Filter.jpg')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Выделение краёв")
    elif filter_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(filter_window, ("Open Image"), "", ("Image Files (*.png *.jpg)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.filter(ImageFilter.FIND_EDGES).save('With_Find_Edges_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Выделение краёв")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(filter_window, "Ошибка", "Что-то пошло не так")


def smooth_filter_image_func():
    """Сделать сглаживание на изображение"""
    filter_line_edit = filter_window.filter_line_edit.text()
    if filter_line_edit != '':
        response = requests.get(filter_line_edit, stream=True)
        if filter_line_edit.find('png') != -1:

            with open('Without_Filter.png', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.png")

            with_filter.filter(ImageFilter.SMOOTH).save('With_Smooth_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Сглаживание")


        elif filter_line_edit.find('jpg') != -1:

            with open('Without_Filter.jpg', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.jpg")
            with_filter.filter(ImageFilter.SMOOTH).save('With_Smooth_Filter.jpg')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Сглаживание")
    elif filter_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(filter_window, ("Open Image"), "", ("Image Files (*.png *.jpg)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.filter(ImageFilter.SMOOTH).save('With_Smooth_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Сглаживание")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(filter_window, "Ошибка", "Что-то пошло не так")


def more_smooth_filter_image_func():
    """Сделать сильное сглаживание на изображение"""
    filter_line_edit = filter_window.filter_line_edit.text()
    if filter_line_edit != '':
        response = requests.get(filter_line_edit, stream=True)
        if filter_line_edit.find('png') != -1:

            with open('Without_Filter.png', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.png")

            with_filter.filter(ImageFilter.SMOOTH_MORE).save('With_Smooth_More_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Сильное сглаживание")


        elif filter_line_edit.find('jpg') != -1:

            with open('Without_Filter.jpg', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.jpg")
            with_filter.filter(ImageFilter.SMOOTH_MORE).save('With_Smooth_More_Filter.jpg')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Сильное сглаживание")
    elif filter_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(filter_window, ("Open Image"), "", ("Image Files (*.png *.jpg)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.filter(ImageFilter.SMOOTH_MORE).save('With_Smooth_More_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Сильное сглаживание")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(filter_window, "Ошибка", "Что-то пошло не так")
def sharpen_filter_image_func():
    """Сделать резкость на изображение"""
    filter_line_edit = filter_window.filter_line_edit.text()
    if filter_line_edit != '':
        response = requests.get(filter_line_edit, stream=True)
        if filter_line_edit.find('png') != -1:

            with open('Without_Filter.png', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.png")

            with_filter.filter(ImageFilter.SHARPEN).save('With_Sharpen_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Резкость")


        elif filter_line_edit.find('jpg') != -1:

            with open('Without_Filter.jpg', 'wb') as f:
                f.write(response.content)

            with_filter = Image.open("Without_Filter.jpg")
            with_filter.filter(ImageFilter.SHARPEN).save('With_Sharpen_Filter.jpg')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Резкость")
    elif filter_line_edit == '':
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(filter_window, ("Open Image"), "", ("Image Files (*.png *.jpg)"))

            itog_name = str(filename).replace('(', '').replace(')', '').replace('Image Files *.png *.jpg', '').replace(',', '').replace("'", "")

            image = Image.open(itog_name)

            image.filter(ImageFilter.SHARPEN).save('With_Sharpen_Filter.png')

            QtWidgets.QMessageBox.about(filter_window, "Уведомление", "На Ваше изображение успешно наложен фильтр-Резкость")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(filter_window, "Ошибка", "Что-то пошло не так")


# Создание приложения
app = QtWidgets.QApplication(sys.argv)
# Создание главного окна
main_window = uic.loadUi("Main_window.ui")

main_window.exit_button.clicked.connect(exit_func)

main_window.rotate_image_button.clicked.connect(visible_rotate_window_func)

main_window.convert_button.clicked.connect(visible_convert_window_func)

main_window.black_and_white_button.clicked.connect(visible_black_window_func)

main_window.add_filter_button.clicked.connect(visible_filter_window_func)

main_window.show()

# Создание окна поворота
rotate_window = uic.loadUi("Rotate_window.ui")

rotate_window.upload_photo_button.clicked.connect(upload_image_func)

rotate_window.back_button.clicked.connect(visible_main_window_func)

rotate_window.rotate_90_left_button.clicked.connect(rotate_left_90_func)

rotate_window.rotate_90_right_button.clicked.connect(rotate_right_90_func)

rotate_window.rotate_180_button.clicked.connect(rotate_180_func)
# Создание окна конвертирования
convert_window = uic.loadUi("Convert_window.ui")

convert_window.convert_jpg_to_png_button.clicked.connect(convert_jpg_to_png_func)

convert_window.convert_png_to_jpg_button.clicked.connect(convert_png_to_jpg_func)

convert_window.back_button.clicked.connect(visible_main_window_func)

# Создание окна черно-белого изображения
black_window = uic.loadUi("Black_window.ui")

black_window.black_and_white_button.clicked.connect(sketch_black_and_white_func)

black_window.back_button.clicked.connect(visible_main_window_func)

# Создание окна наложения фильтров на фотографию
filter_window = uic.loadUi("Filter_window.ui")

filter_window.blur_button.clicked.connect(blur_filter_image_func)

filter_window.contour_button.clicked.connect(contour_filter_image_func)

filter_window.detail_button.clicked.connect(detail_filter_image_func)

filter_window.edge_enhance_button.clicked.connect(edge_enhance_filter_image_func)

filter_window.edge_enhance_more_button.clicked.connect(edge_enhance_more_filter_image_func)

filter_window.emboss_button.clicked.connect(emboss_filter_image_func)

filter_window.edges_button.clicked.connect(find_edges_filter_image_func)

filter_window.smooth_button.clicked.connect(smooth_filter_image_func)

filter_window.more_smooth_button.clicked.connect(more_smooth_filter_image_func)

filter_window.sharpen_button.clicked.connect(sharpen_filter_image_func)

filter_window.back_button.clicked.connect(visible_main_window_func)

app.exec_()
