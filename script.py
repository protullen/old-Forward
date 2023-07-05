class ChatMSG(object):
    HELP_TXT = "HI"

    FORWARDING = """<i>File Forwarding Started😉</i>
<b>From Chat:</b> {from_chat.name}
<b>ID:</b> <code>{from_chat.id}</code>

<b>To Chat:</b> {to_chat.name}
<b>ID:</b> <code>{to_chat.id}</code>

start message ID: <code>{start_id}</code>
end message ID: <code>{stop_id}</code>
"""
