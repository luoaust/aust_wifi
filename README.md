# aust_wifi
实现校园网的自动连接

#### 介绍
以下是 _**aust校园网自动登录**_ 脚本使用的说明，根据自己情况来选择是否开机自启exe程序

#### 程序简介
- 使用语言：python
- 工具：pycharm 或者 python自带的编辑器 或者VScode
- 第三方库：requests，pyinstaller

#### 使用说明

准备步骤：电脑已经 **_安装完成python3_** 的版本，我使用的是pyhton3.7.8版本，安装好第三方库 _**requests**_ 库， _**才能确保你的py文件可以正常运行！**_ 

1.  在代码学号和密码处填写自己的学号和密码即可
2.  将py文件放到C:\Users\******\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
    （介于有朋友反应找不到该目录，可以使用win+r，输入shell:startup也是可以的)
3.  （可选择）完成后将文件打包成exe文件，在生成的dist文件夹下可以找到exe文件

ps:建议选择打包成exe文件，室友的电脑放在文件夹下出现了一些问题，也可以尝试一下，再选择打包成exe文件，然后将exe文件放进windows自启动任务里，即可开机自动连接校园网。

#### 参与贡献

作者：罗清澈

如果觉得好用的话，麻烦点个star，谢谢！
