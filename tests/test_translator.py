from src.translator import translate_to_emoji

def test_translate_to_emoji():
    output = translate_to_emoji("I love pizza")
    assert "❤️" in output
    assert "🍕" in output
