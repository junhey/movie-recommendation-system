一. 基于Python的数据挖掘 基本架构
 
1. matplotlib， 图形化

2. pandas，数据挖掘的关键， 提供各种挖掘分析的算法

3. numpy， 提供基本的统计
   scipy， 提供各种数学公式

4. python common lib，python基本框架

二. 环境搭建
1. 安装python

2. 安装pip
	pandas依赖的pip版本，最低是8.0.0。如果pip是8以下的版本，如7.2.1，需要升级pip.
	命令是“python -m pip install -U pip”，这是windows版本。
	Linux是”pip install -U pip“	
	
	通过命令“pip --version”， 可以查看pip版本号

3. 安装pandas
  	命令“pip install pandas", 这是windows版本。

		Linux平台可用
     sudo apt-get install python-pandas

4. 安装matplotlib
     pip install matplotlib
     
          
三. 数据类型
pypython common type
	string list tuple  dict set
6钟学列
  list, tuple, string, unicode string, buffer object, xrange
	
pandas type
	ndarray, series    dateFrame 
	
	ndarray, 数组类型，	新增原因：
	   list, tuple是基于指针+对象设计的。即list，tuple存储的是void*指针，指针指向具体对象的数据。
	   因为是void*指针，所以二者可以存储各种数据类型，即数据类型可以不统一。
	   虽然存储丰富，但如果数据量过大时，即处理大数据时，有弊端。
	   1. 存储空间大，浪费内存。因为存两部分，指针+数据
	   2. 读取慢，通过index，找到指针；基于指针，找到数据
	所以在大数据处理时，新增ndarray，数字类型，类似C++ 数组。存储相同，读取、修改快捷。
	别名：array, 有利于节省内存、提高CPU的计算时间，有丰富的处理函数 
  
  series，变长字典， 	
  	类似一维数组的对象；有数据和索引组成  	
  新增原因：
    dict是无序的，它的key和value存在映射关系。但key和value之间是不独立的，存储在一起。
    如果需要对一项进行操作，会影响到另外一项。所以有了series， series的key和value是独立的，独立存储。
    series的key是定长有序的。通过series.key获取整个索引， 通过series.values获取所有values.
    series的key,可以通过series.index.name，设置唯一的名称。
    series整体也可以设置唯一名称，通过series.name
  
  DataFrame:
    1. 一个表格型的数据结构
    2. 含有一组有序的列（类似于index)
    3. 可以认为是，共享一个index的Series集合
    
    data1={'name':['java', 'c', 'python'], 'year': [2,2,3]}
    frame = pd.DataFrame(data1)
    
    
 ------------------------------------------------
 四. 基本的数据分析流程：
 	1. 数据的获取
 	
 	2. 数据准备--规格化，建立各种索引index
 	
 	3. 数据的显示、描述，用于调试
 	   如df.index, df.values， df.head(n), df.tail(n） df.describe
 	   
 	4. 数据的选择
 	   index获取， 切片获取, 行、列获取， 矩形区域获取
 	   
 	   index获取，df.row1 或者 df['row1'] 	   
 	   行列，df.loc[行list, 列list], 如df.loc[0:1,['co1','col2'] ]
 	        通过二位索引，取二维左上角，df.iloc[0,0],也可以列表 df.iloc[0:2,0:2]，取前2行。
 	        
 	5. 简单的统计与处理
 		统计平均值、最大值等
 		
 	6. Grouping 分组
 		df.groupby(df.row1)
 		
 	7. Merge合并
 	   append追加, 
 	   contact连接， 包含append功能，也可以两个不同的二维数据结构合并
 	   join连接， SQL连接，基于相同字段连接，如 sql的where, a.row1 = b.row1
  
  
 ------------------------------------------------
 五. 高级的数据处理与可视化：   
   1. 聚类分析
   	 聚类是数据挖掘描述性任务和预测性任务的一个重要组成部分，它以相似性为基础，
   	 把相似的对象通过静态分类，分成不同的组别和子集。
   	 在python中，有很多第三方库提供了聚类算法。
   	 
   	 聚类算法有很多， 其中K-均值算法，因为其简单、快捷的特点，被广泛使用。
   	 基本原理是，
   	 					1. 查找某数据集的中心，
   	 					2. 使用均方差，计算距离。使得每一个数据点都收敛在一个组内；各个组是完全隔离的
   	 					
   	 案例：
   	  >>> from pylab import *
			>>> from scipy.cluster.vq import *
			>>>
			>>> list1=[88,64,96,85]
			>>> list2=[92,99,95,94]
			>>> list3=[91,87,99,95]
			>>> list4 = [78,99,97,81]
			>>> list5=[88,78,98,84]
			>>> list6=[100,95,100,92]
			>>> tempdate = (list1, list2, list3, list4, list5, list6)
			>>>
			>>> tempdate
			([88, 64, 96, 85], [92, 99, 95, 94], [91, 87, 99, 95], [78, 99, 97, 81], [88, 78
			, 98, 84], [100, 95, 100, 92])
			>>> date = vstack(tempdate)
			>>>
			>>> date
			array([[ 88,  64,  96,  85],
			       [ 92,  99,  95,  94],
			       [ 91,  87,  99,  95],
			       [ 78,  99,  97,  81],
			       [ 88,  78,  98,  84],
			       [100,  95, 100,  92]])
			
			>>> centroids,abc=kmeans(date,2) #查找聚类中心，第二个参数是设置分N类，如5类，则为5
			
			>>> centroids  # 基于每列查找的中心点，可能是平均值
			array([[88, 71, 97, 84],
			       [90, 95, 97, 90]])
			>>>
			>>> result,cde=vq(date,centroids) #对数据集，基于聚类中心进行分类
			>>> result
			array([0, 1, 1, 1, 0, 1])
  
  2. 绘图基础
    python描绘库，包含两部分，
    	绘图api, matplotlib提供各种描绘接口。
    	集成库，pylab（包含numpy和matplotlib中的常用方法），描绘更快捷、方便。
    	
		import numpy as np
		import matplotlib.pyplot as plt
		t = np.arange(0,10)
		
		plt.plot(t, t+2）
		plt.plot(t,t, 'o', t,t+2, t,t**2, 'o') #（x,y)一组，默认是折线；‘o'是散点，
	  plt.bar(t,t**2) # 柱状图	  
	  plt.show()
	  
	  --------------------
	  import pylab as pl
	  t = np.arange(0,10)		
		plt.plot(t, t+2)
		plt.show()
		
	3. matplotlib图像属性控制
	   色彩、样式
	   名称： 图、横、纵轴, 
	   				plt.title('philip\'s python plot')
						plt.xlabel('date')
						plt.ylabel('value')
	   其他： pl.figure(figsize=(8,6),dpi=100)
	   				pl.plot(x,y, color='red', linewidth=3, lable='line1')
	   				pl.legend(loc='upper left')
	   				
	   				子图
	   				pl.subplot(211) # 整体图片，可以分为二维部分；
	   					#第一个是图的行，第二个是列；第三个是index, 从左上开始0遍历 当前行，再下一行。
	   					#如果是2位数，如11，需要‘，’
	   				axes(left, bottom, width, height) # 参数取值范围是(0,1), left,是到左边的距离，bottom是到下面的距离
	   				
	 4. pandas作图
	    Series、DataFrame支持直接描绘，封装了调用matplotlib的接口，如
	    series.close.plot()  
	    df.close.plot() #具体参数类似matplotlib普通接口
	    
	    属性控制
	    类似matplotlib普通接口，修改各种图片的类型，柱形图、折线等


  --------common-----------------
  list, tuple, dict
 
  --------numpy-----------------
  ndarray, Series, DataFrame