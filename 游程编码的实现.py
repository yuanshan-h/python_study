import numpy as np

def BRLE(img):
    img=np.array(img)
    img_f=img.flatten()  # 图像数组扁平化
    BRLE_seq=[]   # 输出序列
    elemt=[0,1]   # 序列元素种类，因为是二值图，所以元素只有0和1
    flag=0   # 连续元素的值，假设第一个为0
    count=0  # 连续元素个数

    for i in range(len(img_f)):  # 开始遍历
        if img_f[i]==flag:
            count+=1
            if i==len(img_f)-1:  # 遍历到最后一个元素
                if flag == 0:
                    BRLE_seq.append(-1 * count)
                elif flag == 1:
                    BRLE_seq.append(count)
        else:
            if count>=1:
                 if flag==0:
                    BRLE_seq.append(-1*count)
                 elif flag==1:
                    BRLE_seq.append(count)
            count=1
            temp=list(elemt.copy()) # 不更改elemt的值
            temp.remove(flag)       # 元素不同，更换flag
            flag=temp[0]
            if i==len(img_f)-1:     # 与上面相同，遍历到最后一个元素，避免bug
                if flag == 0:
                    BRLE_seq.append(-1 * count)
                elif flag == 1:
                    BRLE_seq.append(count)
    return BRLE_seq                 # 输出的是列表，不是二维数组


def IBRLE(seq,rows,cols):  # 这里要输入压缩后的序列（就是列表）以及源图像的尺寸
    ORG_seq=[] # 结果列表
    for i in range(len(seq)):
        if seq[i]>0:
            for m in range(seq[i]):
                ORG_seq.append(1)
        else:
            for n in range(np.abs(seq[i])):  # seq[i]小于0,循环时要取绝对值
                ORG_seq.append(0)
    return np.array(ORG_seq).reshape(rows,cols)

def main():
    i = [[1,1,1,0,0,0,0],[0,0,0,0,1,1,1],[0,0,1,1,0,0,1],[0,0,0,0,1,1,0]]
    l = BRLE(i)
    print(l)
    r = IBRLE(l,4,7)
    print(r)
if __name__ == '__main__':
    main()
