# CQUNet-Autologin
重庆大学（虎溪校区）校园网自动登录/掉线重连

新增通过推送加API微信发送当前主机IP（便于快捷进行远程访问PC，避免因校园网IP更换找不到主机）（如不需要此功能请手动注释相关代码）



## 使用方法

在config.ini配置文件中，修改为你的用户名和密码以及推送加Token（可选），使用以下命令：

```
pip install -r requirements.txt
python Autologin.py
```

## 设置开机自启动(可选)

1. 通过以下命令打包为exe：

   `pyinstaller --onefile --noconsole --add-data "config.ini;." Autologin.py`

2. 给打包好的exe创建快捷方式，并放入启动项(命令行运行以下命令打开)中：

   `shell:startup`

3. 将修改后的config.ini文件复制到生成的Autologin.exe目录下（如下）：

   `/dist/Autologin.exe
   /dist/config.ini`
