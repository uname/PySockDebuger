#-*- coding: utf-8 -*-
RELEASE_TYPE          = "py"
GITHUB_HOME           = "https://github.com/uname/PySockDebuger"
TCP_SERVER_ENTRY_TEXT = u"TCP Server"
TCP_CLIENT_ENTRY_TEXT = u"TCP Client"
UDP_SERVER_ENTRY_TEXT = u"UDP Server"
UDP_CLIENT_ENTRY_TEXT = u"UDP Client"
RECV_TAG              = "[RECV]: "
SEND_TAG              = "[SEND]: "

DEFAULT_SERVER_IP_LIST       = ["127.0.0.1", "0.0.0.0"]
DEFAULT_CLIENT_IP_LIST       = ["127.0.0.1"]

RANDOM_MIN_PORT       = 8000
RANDOM_MAX_PORT       = 9000

TCP_SERVER_ROOT_ID = -1
TCP_CLIENT_ROOT_ID = -2
UDP_SERVER_ROOT_ID = -3
UDP_CLIENT_ROOT_ID = -4

LOGO_ICON = ":app/icons/app/logo1.png"

TCP_SERVER_ICON               = ":app/icons/app/tcp_server.png"
UDP_SERVER_ICON               = ":app/icons/app/udp_server.png"
UDP_SERVER_ICON_UNREAD        = ":app/icons/app/udp_server_unread.png"
TCP_CLIENT_ICON_REMOTE        = ":app/icons/app/tcp_client_remote.png"
TCP_CLIENT_ICON_REMOTE_UNREAD = ":app/icons/app/tcp_client_remote_unread.png"
TCP_CLIENT_ICON_LOCAL         = ":app/icons/app/tcp_client_local.png"
TCP_CLIENT_ICON_LOCAL_UNREAD  = ":app/icons/app/tcp_client_local_unread.png"
UDP_CLIENT_ICON_LOCAL         = ":app/icons/app/udp_client_local.png"
UDP_CLIENT_ICON_LOCAL_UNREAD  = ":app/icons/app/udp_client_local_unread.png"
QRCODE_ZFB                    = ":qrcode/icons/qrcode/weixin.png"
GITHUB_LOGO                   = ":ext/icons/ext/github_logo.png"

TCP_CLIENT_ICON_REMOTE_SET    = (TCP_CLIENT_ICON_REMOTE, TCP_CLIENT_ICON_REMOTE_UNREAD)
TCP_CLIENT_ICON_LOCAL_SET     = (TCP_CLIENT_ICON_LOCAL, TCP_CLIENT_ICON_LOCAL_UNREAD)
UDP_CLIENT_ICON_LOCAL_SET     = (UDP_CLIENT_ICON_LOCAL, UDP_CLIENT_ICON_LOCAL_UNREAD)
UDP_SERVER_ICON_SET           = (UDP_SERVER_ICON, UDP_SERVER_ICON_UNREAD)

TEXT_DISCONNECT = u"断开"
TEXT_CONNECT    = u"连接"


STATUS_CONNECTED     = u'<font style="BACKGROUND-COLOR:#00FF00">已连接</font>'
STATUS_NOT_CONNECTED = u'<font style="BACKGROUND-COLOR:#C0C0C0">未连接</font>'
STATUS_DISCONNECTED  = u'<font style="BACKGROUND-COLOR:#FF0000">已断开</font>'
STATUS_UDP           = u'<font style="BACKGROUND-COLOR:#93FF93">UDP-CLIENT</font>'
STATUS_UDP_SERVER    = u'<font style="BACKGROUND-COLOR:#93FF93">UDP-SERVER</font>'