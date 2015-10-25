#-*- coding: utf-8 -*-
RELEASE_TYPE          = "py"
GITHUB_HOME           = "https://github.com/uname/PySockDebuger"
TCP_SERVER_ENTRY_TEXT = u"TCP服务器"
TCP_CLIENT_ENTRY_TEXT = u"TCP客户端"
RECV_TAG              = "[RECV]: "
SEND_TAG              = "[SEND]: "

DEFAULT_SERVER_IP_LIST       = ["127.0.0.1", "0.0.0.0"]
DEFAULT_CLIENT_IP_LIST       = ["127.0.0.1"]

RANDOM_MIN_PORT       = 8000
RANDOM_MAX_PORT       = 9000

TCP_SERVER_ROOT_ID = -1
TCP_CLIENT_ROOT_ID = -2

TCP_SERVER_ICON               = ":app/icons/app/tcp_server.png"
TCP_CLIENT_ICON_REMOTE        = ":app/icons/app/tcp_client_remote.png"
TCP_CLIENT_ICON_REMOTE_UNREAD = ":app/icons/app/tcp_client_remote_unread.png"
TCP_CLIENT_ICON_LOCAL         = ":app/icons/app/tcp_client_local.png"
TCP_CLIENT_ICON_LOCAL_UNREAD  = ":app/icons/app/tcp_client_local_unread.png"

TCP_CLIENT_ICON_REMOTE_SET    = (TCP_CLIENT_ICON_REMOTE, TCP_CLIENT_ICON_REMOTE_UNREAD)
TCP_CLIENT_ICON_LOCAL_SET     = (TCP_CLIENT_ICON_LOCAL, TCP_CLIENT_ICON_LOCAL_UNREAD)

TEXT_DISCONNECT = u"断开"

STATUS_CONNECTED = u'<font style="BACKGROUND-COLOR:#00FF00">已连接</font>'