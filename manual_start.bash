
xset s noblank
xset s off
xset -dpms

# sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
# sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

matchbox-window-manager -use_titlebar no &
unclutter -idle 0 &    # 自动隐藏鼠标
source $(dirname "$(readlink -f "$0")")/bin/activate
python $(dirname "$(readlink -f "$0")")/app.py &
chromium-browser file://$(dirname "$(readlink -f "$0")")/home.html
