class ChatMSG(object):
    HELP_TXT = "HI"

    @staticmethod
    def FORWARDING():
        return """Forwarding Started! ✅

<b>• Source Chat:</b> {{}}
<b>• Target Chat:</b> {{}}
<b>• Start Msg ID:</b> <a href='{{}}'>{{}}</a>
<b>• End Msg ID:</b> <a href='{{}}'>{{}}</a>
<b>• Status:</b> Forwarding 
"""

    @staticmethod
    def FORWARDING_STOPPED(files_count, forward_type):
        return f"""Forwarding Stopped!

<b>• Source Chat:</b> {{}}
<b>• Target Chat:</b> {{}}
<b>• Start Msg ID:</b> <a href='{{}}'>{{}}</a>
<b>• End Msg ID:</b> <a href='{{}}'>{{}}</a>
<b>• Status:</b> Complete ✅

Successfully Forwarded {files_count} {forward_type}
"""
