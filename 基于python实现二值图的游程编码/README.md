
# 基于python实现二值图像的游程编码和解码
## 什么是游程编码
游程编码是一种比较简单的压缩算法，其基本思想是将重复且连续出现多次的字符使用（连续出现次数，某个字符）来描述。

游程长度编码是栅格数据压缩的重要编码方法，它的基本思路是：对于一幅栅格图像，常常有行(或列)方向上相邻的若干点具有相同的属性代码，因而可采取某种方法压缩那些重复的记录内容。其编码方案是，只在各行(或列)数据的代码发生变化时依次记录该代码以及相同代码重复的个数，从而实现数据的压缩。
![算法示意图](https://img-blog.csdn.net/20150207113157954)
##游程编码的特点
* 是一种简单的无损数据压缩方式且代码简单易实现
* 压缩比的大小是与图的复杂程度成反比的，在变化多的部分，游程数就多，变化少的部分游程数就少，图件越简单，压缩效率就越高。


##游程编码/解码算法的代码实现
* 压缩代码

``` python

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
```

* 解压代码

``` python

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
```
##运行结果示例
![原图1](https://www.z4a.net/images/2022/05/20/QQ.md.jpg)
![二值化后压缩后的图](https://www.z4a.net/images/2022/05/20/reoutput_QQ.md.png)

![图1压缩率截图](https://www.z4a.net/images/2022/05/19/14de774d0fb134064.png)

![原图2](https://www.z4a.net/images/2022/05/20/bilotus1.jpg)
![二值化后压缩后的图](https://www.z4a.net/images/2022/05/20/reoutput_bilotus1.png)
![图2压缩率截图](https://www.z4a.net/images/2022/05/19/Z4FU1QULQVE7CT45EY.png)