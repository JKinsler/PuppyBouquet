"""File for media image links of dogs and puppies"""

import random

# set of all video and image urls
puppies = set()

def choose_image():
    """pick a random image from the video / image library."""

    return random.choice(tuple(puppies))


# add images and URLs to the set
puppies.add('https://media.spokesman.com/photos/2019/11/14/Unicorn_Puppy.JPG_Bqodudn_t1170.jpg?e2225bc5c1a75a1036ca3021fecba2b47792abfe')
puppies.add('https://s.abcnews.com/images/Lifestyle/puppy-ht-3-er-170907_16x9_992.jpg')
puppies.add('https://assets3.thrillist.com/v1/image/2861619/size/tmg-article_tall;jpeg_quality=20.jpg')
puppies.add('https://compote.slate.com/images/24c26e48-a422-4843-90c3-927c3268f51e.jpg')
puppies.add('https://dynaimage.cdn.cnn.com/cnn/c_fill,g_auto,w_1200,h_675,ar_16:9/https%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F200217140048-02-puppy-pigeon-friendship-rescue.jpg')
puppies.add('https://i.insider.com/5e600587a9f40c6f39701245?width=1100&format=jpeg&auto=webp')
puppies.add('https://icdn6.themanual.com/image/themanual/connor-the-puggle-puppy-photo-credit-dan-baker-416x416.jpg')
puppies.add('https://media.spokesman.com/photos/2019/04/25/Puppy1.jpg')
puppies.add('https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQkotfX7XDrI_F8JDglHyO0Yoko4k8Vu7Id92D4niakdReSsf8V&usqp=CAU')
puppies.add('https://3.bp.blogspot.com/_juSx6zGROwg/Spx2MHlY-lI/AAAAAAAAAGE/T-bV4XcsehY/s400/naughty-puppy-dog-destroying-toilet-paper.jpg')
puppies.add('https://secure.i.telegraph.co.uk/multimedia/archive/02893/puppy_2893720b.jpg')
puppies.add('https://i.ytimg.com/vi/FeLV0vA7ZJA/hqdefault.jpg')
puppies.add('')
puppies.add('')
puppies.add('')
puppies.add('')


if __name__ == '__main__':
    print(puppies)
    print(choose_image())
