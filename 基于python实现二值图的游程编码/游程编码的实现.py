import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
def Compress(img):

    img_f=img.flatten()  # 图像数组扁平化
    for i in range(len(img_f)):
        if img_f[i] >= 127:
            img_f[i] = 255
        if img_f[i] < 127:
            img_f[i] = 0
    compress_seq=[]   # 输出序列
    elemt=[0,255]   # 序列元素种类，因为是二值图，所以元素只有0和1
    flag=0   # 连续元素的值，假设第一个为0
    count=0  # 连续元素个数
    for i in range(len(img_f)):  # 开始遍历
        if img_f[i]==flag:
            count+=1
            if i==len(img_f)-1:  # 遍历到最后一个元素
                if flag == 0:
                    compress_seq.append(-1 * count)
                elif flag == 255:
                    compress_seq.append(count)
        else:
            if count>=1:
                 if flag==0:
                    compress_seq.append(-1*count)
                 elif flag==255:
                    compress_seq.append(count)
            count=1
            temp=list(elemt.copy()) # 不更改elemt的值
            temp.remove(flag)       # 元素不同，更换flag
            flag=temp[0]
            if i==len(img_f)-1:     # 与上面相同，遍历到最后一个元素，避免bug
                if flag == 0:
                    compress_seq.append(-1 * count)
                elif flag == 255:
                    compress_seq.append(count)
    print("压缩率：",len(compress_seq)/len(img_f)*100,"%")
    return compress_seq                 # 输出的是列表，不是二维数组


def UnCompress(seq,rows,cols):  # 这里要输入压缩后的序列（就是列表）以及源图像的尺寸
    uncompress_seq=[] # 结果列表
    for i in range(len(seq)):
        if seq[i]>0:
            for m in range(seq[i]):
                uncompress_seq.append(255)
        else:
            for n in range(np.abs(seq[i])):  # seq[i]小于0,循环时要取绝对值
                uncompress_seq.append(0)
    return np.reshape(uncompress_seq,(rows,cols))

def main():
    path = 'img.png'
    img = cv.imread(path,1)
    grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    l = Compress(grayimg)
    r = UnCompress(l,grayimg.shape[0],grayimg.shape[1])

    r=np.array(r,dtype=np.uint8)

    cv.imwrite('reoutput_{}.png'.format(path[:(len(path)-4)]),r)
    cv.imshow('rec_image',r) #重新输出二值化图像
    cv.waitKey(0)
if __name__ == '__main__':
    main()
