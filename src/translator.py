import emoji
import re
from emoji_map import emoji_dict

def translate_to_emoji(text):
    words = re.findall(r'\w+', text.lower())
    result = []

    for word in words:
        if word in emoji_dict:
            result.append(emoji_dict[word])
        else:
            result.append(word)

    return " ".join(result)
