# PuppyBouquet

PuppyBouquet is a bot that send messages to users to spread some cheer. Messages include a short inspirational phrase and an image of a dog or puppy being silly.

The bot uses Twilio's SMS api to send texts. Message content is randomly generated from a set of curated phrases and images.

###Contents
* [Technologies](#techstack)
* [Installation](#installation)
* [Features](#features)
* [Features for Version 2.0](#futurefeatures)
* [About The Developer](#aboutme)

## <a name="techstack"></a>Technologies

Tech Stack: Python3, Twilio SMS api

## <a name="installation"></a>Installation
### Prerequisites

The following must be installed to run SolarViz:

- Python3

- Twilio account or trial account:
    - Twilio authorization token
    - Twilio account SID
    - Twilio phone number (sending number)
    - Receiver's phone number (must verify on your Twilio trial account)

### Run PuppyBouquet on your local computer

Clone repository:
```
$ git clone https://github.com/JKinsler/PuppyBouquet.git
```
Create and activate a virtual environment inside your PuppyBoquet directory:
```
$ virtualenv env --always-copy  
$ source env/bin/activate
```
(Mac and Linux users use 'virtualenv env')
<br><br>
Install dependencies:
```
$ pip install -r requirements.txt
```
Get a Twilio authorization token, SID, and phone number:
<a href="https://www.twilio.com/try-twilio"> Twilio create user account </a>
<a href="https://www.twilio.com/docs/sms"> Twilio SMS documentation </a>
<a href="https://www.youtube.com/watch?v=knxlmCVFAZI"> Twilio getting started video </a>
<br><br>
Create a file called **secrets.sh** and add your private keys there: <br> 
- Twilio authorization token
    - Twilio account SID
    - Twilio phone number (sending number)
    - Receiver's phone number (must verify on your Twilio trial account)
<br><br>
Source the private keys:
```
$ source secrets.sh
```
## <a name="futurefeatures"></a>Features for Version 2.0

* Schedule messages so they send on a specific time when the bot is deployed
* expand into a web app that allows users to create an account and select when they'd like to receive PuppyBouquet messages
* Give users the option to upload of their dogs, to be shared.
 

## <a name="aboutme"></a>About the Developer

PuppyBouquet creator, Johanna Kinsler, is a former automotive engineer turned software engineer. Johanna made PuppyBouquet to bring some cheer to friends and family during the covid19 shelter in place orders. Johanna learned her full stack software engineering skills at Hackbright's fellowship program, which she completed in March 2020. She can be found on [LinkedIn](https://www.linkedin.com/in/johanna-kinsler-76562463/) and on [Github](https://github.com/JKinsler).