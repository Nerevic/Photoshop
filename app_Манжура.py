import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, 
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
 
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap 
from PIL import Image, ImageFilter, ImageEnhance
 
app = QApplication([])
win = QWidget()      
win.resize(700, 500)
win.setWindowTitle('Easy Editor')
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()
 
btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_blur = QPushButton("розмити")
btn_sharp_plus = QPushButton("контраст +")
btn_sharp_minus = QPushButton("контраст -")
btn_bw = QPushButton("Ч/Б")
btn_smooth = QPushButton("згладити")
btn_mirror_LR = QPushButton("відзеркалити ◀▶")
btn_mirror_UD = QPushButton("відзеркалити 🔼🔽")
btn_upend = QPushButton("перевернути")
 
row = QHBoxLayout()   

col1 = QVBoxLayout()        
col2 = QVBoxLayout()
col1.addWidget(btn_dir)      
col1.addWidget(lw_files)
col2.addWidget(lb_image, 95)

row_tools = QHBoxLayout()
row_tools_2 = QHBoxLayout()

row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_blur)
row_tools.addWidget(btn_sharp_plus)
row_tools.addWidget(btn_sharp_minus)

row_tools_2.addWidget(btn_bw)
row_tools_2.addWidget(btn_smooth)
row_tools_2.addWidget(btn_mirror_LR)
row_tools_2.addWidget(btn_mirror_UD)
row_tools_2.addWidget(btn_upend)

col2.addLayout(row_tools)
col2.addLayout(row_tools_2)
 
row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)
 
win.show()
workdir = ''
 

def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result
 

def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()
 

def showFilenamesList():
   extensions = ['.jpg', '.PNG', '.png', '.jpeg', '.gif', '.ico', '.bmp']
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)
 
   lw_files.clear()
   for filename in filenames:
       lw_files.addItem(filename)
 
 
btn_dir.clicked.connect(showFilenamesList)
 
class ImageProcessor():
    def init(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"

    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
 
    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w = lb_image.width()
        h = lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

    def do_left(self, filename):
        if lw_files.currentRow() >= 0:
            file_name = lw_files.currentItem().text()
            workimage.loadImage(workdir, file_name)
            image_path = os.path.join(workimage.dir, workimage.filename)
            name_img = self.filename
            split_img =  name_img.split('.')
            a = len(split_img)
            a = a - 1
            name_new_img = name_img.replace('.' + split_img[a],'')
            with Image.open(image_path) as pic:
                left_pic = pic.transpose(Image.ROTATE_270)
                left_pic.save(name_new_img + '_left_pic.' + split_img[a])

    def do_right(self, filename):
        if lw_files.currentRow() >= 0:
            file_name = lw_files.currentItem().text()
            workimage.loadImage(workdir, file_name)
            image_path = os.path.join(workimage.dir, workimage.filename)
            name_img = self.filename
            split_img =  name_img.split('.')
            a = len(split_img)
            a = a - 1
            name_new_img = name_img.replace('.' + split_img[a],'')
            with Image.open(image_path) as pic:
                right_pic = pic.transpose(Image.ROTATE_90)
                right_pic.save(name_new_img + '_right_pic.' + split_img[a])

    def do_blur(self, filename):
        if lw_files.currentRow() >= 0:
            file_name = lw_files.currentItem().text()
            workimage.loadImage(workdir, file_name)
            image_path = os.path.join(workimage.dir, workimage.filename)
            name_img = self.filename
            split_img =  name_img.split('.')
            a = len(split_img)
            a = a - 1
            name_new_img = name_img.replace('.' + split_img[a],'')
            with Image.open(image_path) as pic:
                blur_pic = pic.filter(ImageFilter.BLUR)
                blur_pic.save(name_new_img + '_blur_pic.' + split_img[a])

    def do_sharp_plus(self, filename):
        if lw_files.currentRow() >= 0:
            file_name = lw_files.currentItem().text()
            workimage.loadImage(workdir, file_name)
            image_path = os.path.join(workimage.dir, workimage.filename)
            name_img = self.filename
            split_img =  name_img.split('.')
            a = len(split_img)
            a = a - 1
            name_new_img = name_img.replace('.' + split_img[a],'')
            with Image.open(image_path) as pic:
                sharp_plus_pic = ImageEnhance.Contrast(pic)
                sharp_plus_pic = sharp_plus_pic.enhance(4)
                sharp_plus_pic.save(name_new_img + '_sharp_plus_pic.' + split_img[a])

    def do_sharp_minus(self, filename):
        if lw_files.currentRow() >= 0:
            file_name = lw_files.currentItem().text()
            workimage.loadImage(workdir, file_name)
            image_path = os.path.join(workimage.dir, workimage.filename)
            name_img = self.filename
            split_img =  name_img.split('.')
            a = len(split_img)
            a = a - 1
            name_new_img = name_img.replace('.' + split_img[a],'')
            with Image.open(image_path) as pic:
                sharp_minus_pic = ImageEnhance.Contrast(pic)
                sharp_minus_pic = sharp_minus_pic.enhance(-4)
                sharp_minus_pic.save(name_new_img + '_sharp_minus_pic.' + split_img[a])

    def do_bw(self, filename):
        if lw_files.currentRow() >= 0:
            file_name = lw_files.currentItem().text()
            workimage.loadImage(workdir, file_name)
            image_path = os.path.join(workimage.dir, workimage.filename)
            name_img = self.filename
            split_img =  name_img.split('.')
            a = len(split_img)
            a = a - 1
            name_new_img = name_img.replace('.' + split_img[a],'')
            with Image.open(image_path) as pic:
                gray_pic = pic.convert('L')
                gray_pic.save(name_new_img + '_gray_pic.' + split_img[a])

    def do_smooth(self, filename):
        if lw_files.currentRow() >= 0:
            file_name = lw_files.currentItem().text()
            workimage.loadImage(workdir, file_name)
            image_path = os.path.join(workimage.dir, workimage.filename)
            name_img = self.filename
            split_img =  name_img.split('.')
            a = len(split_img)
            a = a - 1
            name_new_img = name_img.replace('.' + split_img[a],'')
            with Image.open(image_path) as pic:
                smooth_pic = pic.filter(ImageFilter.SMOOTH)
                smooth_pic.save(name_new_img + '_smooth_pic.' + split_img[a])

    def do_mirror_LR(self, filename):
        if lw_files.currentRow() >= 0:
            file_name = lw_files.currentItem().text()
            workimage.loadImage(workdir, file_name)
            image_path = os.path.join(workimage.dir, workimage.filename)
            name_img = self.filename
            split_img =  name_img.split('.')
            a = len(split_img)
            a = a - 1
            name_new_img = name_img.replace('.' + split_img[a],'')
            with Image.open(image_path) as pic:
                mirror_LR_pic = pic.transpose(Image.FLIP_LEFT_RIGHT)
                mirror_LR_pic.save(name_new_img + '_mirror_LR_pic.' + split_img[a])

    def do_mirror_UD(self, filename):
        if lw_files.currentRow() >= 0:
            file_name = lw_files.currentItem().text()
            workimage.loadImage(workdir, file_name)
            image_path = os.path.join(workimage.dir, workimage.filename)
            name_img = self.filename
            split_img =  name_img.split('.')
            a = len(split_img)
            a = a - 1
            name_new_img = name_img.replace('.' + split_img[a],'')
            with Image.open(image_path) as pic:
                mirror_UD_pic = pic.transpose(Image.FLIP_TOP_BOTTOM)
                mirror_UD_pic.save(name_new_img + '_mirror_UD_pic.' + split_img[a])

    def do_upend(self, filename):
        if lw_files.currentRow() >= 0:
            file_name = lw_files.currentItem().text()
            workimage.loadImage(workdir, file_name)
            image_path = os.path.join(workimage.dir, workimage.filename)
            name_img = self.filename
            split_img =  name_img.split('.')
            a = len(split_img)
            a = a - 1
            name_new_img = name_img.replace('.' + split_img[a],'')
            with Image.open(image_path) as pic:
                upend_pic = pic.transpose(Image.ROTATE_180)
                upend_pic.save(name_new_img + '_upend_pic.' + split_img[a])


workimage = ImageProcessor()
 
def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)

lw_files.currentRowChanged.connect(showChosenImage)

workimage = ImageProcessor()

btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_blur.clicked.connect(workimage.do_blur)
btn_sharp_plus.clicked.connect(workimage.do_sharp_plus)
btn_sharp_minus.clicked.connect(workimage.do_sharp_minus)
btn_bw.clicked.connect(workimage.do_bw)
btn_smooth.clicked.connect(workimage.do_smooth)
btn_mirror_LR.clicked.connect(workimage.do_mirror_LR)
btn_mirror_UD.clicked.connect(workimage.do_mirror_UD)
btn_upend.clicked.connect(workimage.do_upend)

win.show()
app.exec()

print()