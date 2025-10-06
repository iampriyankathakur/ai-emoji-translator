import argparse
from translator import translate_to_emoji

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True, help="Text to translate to emojis")
    args = parser.parse_args()

    translation = translate_to_emoji(args.text)
    print(f"🗣️ Input: {args.text}")
    print(f"✨ Output: {translation}")
