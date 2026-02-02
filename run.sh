#!/usr/bin/env bash

# tạo DBus session nếu chưa có (rất quan trọng trên WSL)
if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
  eval "$(dbus-launch --sh-syntax)"
fi

export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT_QPA_PLATFORM=xcb

pgrep -x ibus-daemon >/dev/null || ibus-daemon -drx

python -m app.main
