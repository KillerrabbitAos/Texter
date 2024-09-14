from lib2to3.pgen2.token import NEWLINE


def convert_to_string(text):
    bar = ""
    return bar.join(text)


def write(text):
    return f"test: {text}"


def draw(txt, totalTime: int, wait):
    import time

    for character in txt:
        print(character, end="""""", flush=True)
        time.sleep(totalTime / len(txt))
    time.sleep(wait)
    print("")
