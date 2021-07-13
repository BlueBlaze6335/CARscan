import cv2
import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
print("Enter path of original pic of Car")
ORI=input() # example "assets/input/view2.jpeg" ** dont forget to change "\" to "/"
print("Enter 0 to remove Background or 1 to add new Background")
x=int(input())

if x==0:
    output=change_bg.change_bg_img(f_image_path = ORI,b_image_path = "assets/input/nobg.jpg" , detect="car",output_image_name="nobgview1.jpg")
    output=cv2.resize(output,(512,512))
    cv2.imshow('Without BG',output)
    cv2.waitKey()
else:
    print("Enter path of background image")
    NEW=input() # example "assets/input/roadbg.jpg" ** dont forget to change "\" to "/"
    output=change_bg.change_bg_img(f_image_path = ORI,b_image_path =NEW, detect="car" ,output_image_name="newbgview1.jpg")
    output = cv2.resize(output, (512, 512))
    cv2.imshow('With new BG',output)
    cv2.waitKey()
