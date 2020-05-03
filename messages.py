"""Gives options for messages to send to users"""

import random

msgs = set()

msgs.add('Please remember to pet your local dogs today.')
msgs.add('We hope you see some fluffy friends today.')
msgs.add('Remember the golden rule: treat others like you would treat them if you were a Golden Retreiver.')
msgs.add('You are not alone. A warm and furry friend wants you to pet him.')
msgs.add("A puppy is wagging his tail for you. How nice!")
msgs.add("May you embody all the spirit of this little guy today:")


def choose_msg():
    """pick a random image from the video / image library."""

    return random.choice(tuple(msgs))

if __name__ == '__main__':
    print(msgs)
    print(choose_msg())