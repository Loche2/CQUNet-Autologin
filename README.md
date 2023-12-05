# CQUNet-Autologin
重庆大学（虎溪校区）校园网自动登录/掉线重连

新增通过推送加API微信发送当前主机IP（便于快捷进行远程访问PC，避免因校园网IP更换找不到主机）

（程序每300秒检查一次是否可访问外网，可根据需要修改）

## 使用方法（release）

下载并解压release版，在config.ini配置文件中，修改为你的用户名和密码以及推送加Token（可不填），双击Autologin.exe运行

## 使用方法（code）

在config.ini配置文件中，修改为你的用户名和密码以及推送加Token（可不填），使用以下命令：

```
pip install -r requirements.txt
python Autologin.py
```

## 设置开机自启动(可选)

给Autologin.exe创建快捷方式，并放入启动项文件夹(win+R运行以下命令打开)中：

`shell:startup`

