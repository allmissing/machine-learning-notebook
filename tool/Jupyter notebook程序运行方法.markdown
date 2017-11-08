# 问题描述

每次打开pycharm中的Jupyter notebook，按下运行按钮，都会弹出对话框让输入token，运行不了。

# 问题解决

## 摘录自https://www.2cto.com/kf/201710/688809.html

在pycharm中打开某个ipynb文件，就会出现大家熟悉的notebook编辑界面，但是和在浏览器中打开的界面还是略有不同。

这时候在第一个cell里输入一些内容，然后shift+return（或者点击运行），pycharm就会弹框提示

![avatar]（github.com/allmissing/machine-learning-notebook/blob/master/tool/MackDownPhotos/1.png）

这里要注意！如果你需要制定的服务器上运行notebook，这时候你可以填写你所使用的服务器地址；但一般情况下，我们只是想本地编辑notebook，这里我们点击“cancel”。接着pycharm会提示”Cannot connect to Jupyter Notebook. Run Jupyter Notebook”。利用这个提示，我们在pycharm中启动本地的notebook服务器（官方的文档就是这么做的，我也觉得很操蛋）

![Aaron Swartz]（）

我们点击”Run Jupyter Notebook”，pycharm就会在本地运行notebook。

![Aaron Swartz]（）

然后再按shift+return就可以像在浏览器中一样编辑notebook了。

![Aaron Swartz]（）
