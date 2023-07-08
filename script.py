class ChatMSG(object):
    FORWARDING = """Forwarding Started! ✅

<b>• Source Chat:</b> {}
<b>• Target Chat:</b> {}
<b>• Start Msg ID:</b> <a href='{}'>{}</a>
<b>• End Msg ID:</b> <a href='{}'>{}</a>
<b>• Status:</b> Forwarding 

send /cancel to stop forwarding
"""

    FORWARDING_STOPPED = """Forwarding Stopped!

<b>• Source Chat:</b> {}
<b>• Target Chat:</b> {}
<b>• Start Msg ID:</b> <a href='{}'>{}</a>
<b>• End Msg ID:</b> <a href='{}'>{}</a>
<b>• Status:</b> Complete ✅

Successfully Forwarded {} {}
"""
