# 两种方法载入

1. 手动启动：
适合在调试阶段使用
在任意路径下运行manual_start.bash

2. 自动启动：
适合在成熟阶段使用 
    1. 在.bashrc最后加入代码

    ```bash
    case $(tty) in
    (/dev/tty[1-9])
            xinit ${repository_path}/auto_start.bash -- -nocursor vt$(fgconsole) &
            ;;
    esac
    ```
    使用 X 服务器来使用auto_start.bash脚本启动UI

    2. 使用`sudo raspi-config`命令配置树莓派的Console Autologin终端自动登陆（注意是终端自动登陆，并不是Desktop Autologin桌面自动登录）
    3. 重启之后ui即可自动打开