class ChatMSG(object):
    HELP_TXT = "HI"

    FORWARDING = f"""Forwarding Started! ✅
    
<b>• Source Chat:</b> {}
<b>• Target Chat:</b> {}
<b>• Start Msg ID:</b> <a href='{}'>{}</a>
<b>• End Msg ID:</b> <a href='{}'>{}</a>
<b>• Status:</b> Forwarding 
"""
    FORWARDING_STOPPED = f"""Forwarding Stopped    
<b>• Source Chat:</b> {}
<b>• Target Chat:</b> {}
<b>• Start Msg ID:</b> <a href='{}'>{}</a>
<b>• End Msg ID:</b> <a href='{}'>{}</a>
<b>• Status:</b> Complete ✅

Successfully Forwarded {} {}
"""
