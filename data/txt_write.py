import numpy as np

""" 
img_filename = np.loadtxt("/home/recep/dataprocessing/data/image_names-0.txt", dtype=str)

train_img_txt = open("/home/recep/dataprocessing/data/test_img.txt","w")

for i in range(581):
    train_img_txt.write(str(img_filename[i+7000]) + "\n") """
    
labels = np.loadtxt("/home/recep/dataprocessing/data/image_labels-0.txt", dtype=str)

filename = open("train_img.txt","w")
file = open("train_label.txt","w")
a=0
for i in labels:
    s = i[0]
    filename.write(s[1:]+"\n")
    file.write(i[1] + " " + i[2] + " " + i[3] + " " + i[4] + "\n")
    a=a+1
filename.close()
file.close()