# CQUNet-Autologin
重庆大学（虎溪校区）校园网自动登录/掉线重连



## 使用方法

在Autologin.py文件中，修改为你的用户名和密码，使用以下命令：

```
pip install -r requirements.txt
python Autologin.py
```

## 设置开机自启动

1. 通过以下命令打包为exe：

   `pyinstaller --onefile --noconsole Autologin.py`

2. 给打包好的exe创建快捷方式，并放入启动项(运行以下命令打开)中：

   `shell:startup`
