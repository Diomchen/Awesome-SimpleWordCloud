#-*-coding:utf-8-*-
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import ctfc
import os

#设置背景图片
background = np.array(Image.open("F:\\PythonDemo\\词云\\venv\\CiYunToFriendsCircle\\timg.jpg"))

#设置生成图片的属性
wc = WordCloud(background_color="white",max_words=1000,mask=background,max_font_size=500,random_state=444,font_path='F:\\PythonDemo\\词云\\venv\\CiYunToFriendsCircle\\simsun.ttc')

# keyword = ctfc.main()
# print(dict(keyword))

#根据ctfc的提取出来的关键词和其权重进行图片生成词云
wc.generate_from_frequencies(dict(keyword))

#颜色从背景图片中提取
image_colors = ImageColorGenerator(background)

#下面的都是特定格式，具体参考
plt.figure(figsize=(10,8))
plt.imshow(wc,interpolation="bilinear")
plt.axis("off")

#绘制词云
plt.imshow(wc.recolor(color_func=image_colors),interpolation="bilinear")
plt.axis("off")


plt.figure()
plt.imshow(background, cmap=plt.cm.gray)
plt.axis("off")

#保存图片
wc.to_file(os.path.join('C:\\Users\\Shuhan Chen\\Desktop',"sishi.png"))