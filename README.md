# PySockDebuger

###使用PyQt4编写跨平台GUI客户端，用于TCP和UDP的通信调试
#####环境依赖
1. Python2.7
2. PyQt4
3. py2exe(Version for Python2.7，用于在Windows下生成EXE)

![](/resource/exticons/snapshot.png)

#####进度
######2015/8/28
使用Qt Designer设计了简单的主窗体UI，编写了简单的代码，双击main.py可启动程序。功能还未开始编写。

######2015/9/4
完成创建TCP服务器和TCP客户端的输入参数弹框

######2015/10/13
TCP服务器已经可用（ASCII文本数据模式）
TCP客户端内部逻辑基本完成

######2015/10/30
TCP服务器，TCP客户端和UDP客户端都可用了
暂未实现重复发送功能
暂未实现UDP服务器功能

