from telegram.utils.helpers import escape_markdown as es


def start_msg(name):
    msg = f"""*Hey {es(name,version=2)}* ✋✋ *welcome to Pagalworldsongs Bot* ⚡⚡\n
    _Just send me a Jiosaavn song or album link and I will send you the audio_\n
made by @pagalworldsongs 😈😈"""
    return msg


def help_msg():
    help = """ℹ️⁉⁉ *help*\n
*just send me a jiosaavn song, album or playlist link, I will send you the audio with lyrics*⚡⚡"""
    return help
