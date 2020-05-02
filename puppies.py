"""Puppy video vidwo URLs and images.
Contains a set of all URLs and images"""

import random

# set of all images and videos
puppies = set()

def choose_image():
    """pick a random image from the video / image library."""

    return random.choice(tuple(puppies))


# add images and URLs to the set
puppies.add('https://www.facebook.com/WoofWoofTV/videos/327233211582966/')
puppies.add('https://www.facebook.com/WoofWoofTV/videos/684470895451119/')
puppies.add('https://www.facebook.com/thepetcollective/videos/665127894310782/')


if __name__ == '__main__':
    print(puppies)
    print(choose_image())
