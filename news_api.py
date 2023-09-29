from pprint import pprint as print
from newsapi import NewsApiClient
import datetime
import streamlit as st

# Init
newsapi = NewsApiClient(api_key='b387963621d7483cb48dbc1162a08a5f') #b387963621d7483cb48dbc1162a08a5f

# @st.cache_data
def get_news(query: str, from_date: datetime.datetime, to_date: datetime.datetime, sorty_by='popularity',
             language="en",num_articles=10):
    """

    out_put = {'data': [{'description': 'For all of CarPlay’s perks, the one downside is it '
                          'requires one phone to be connected at a time. For '
                          'the most part, that’s just fine—except when a '
                          'passenger\xa0wants to play music from their iPhone. '
                          'Suddenly, a choice must be made: Attempt to find '
                          'the song on th…',
           'publishedAt': '2023-09-25T20:30:00Z',
           'title': "Now Anyone Can Play Music in Your Car, No Matter Who's "
                    'Connected to CarPlay',
           'url': 'https://lifehacker.com/now-anyone-can-play-music-in-your-car-no-matter-whos-c-1850871141'},
          {'description': 'ChatGPT\r\n'
                          ' is getting some significant updates that will '
                          'enable the chatbot to deal with voice commands and '
                          'image-based queries. Users will be able to have a '
                          'voice conversation with ChatGPT on Android and iOS '
                          'and to feed images into it on all platforms. '
                          'OpenAI…',
           'publishedAt': '2023-09-25T14:47:18Z',
           'title': 'ChatGPT now supports voice chats and image-based queries',
           'url': 'https://www.engadget.com/chatgpt-now-supports-voice-chats-and-image-based-queries-144718179.html'},
          {'description': 'Artifact, the AI-powered news app from Instagram’s '
                          'co-founders, is going to let you post directly to '
                          'the app. So far, the app has been an aggregator for '
                          'news and links from around the internet.',
           'publishedAt': '2023-09-27T18:32:07Z',
           'title': 'Artifact is becoming Twitter, too',
           'url': 'https://www.theverge.com/2023/9/27/23887416/artifact-mike-krieger-code-2023-posts'},
          {'description': 'The iPhone 15 and 15 Pro have officially launched. '
                          'They offer some big upgrades over previous models, '
                          'including a switch from Lightning to USB-C. Here’s '
                          'our coverage.',
           'publishedAt': '2023-09-22T15:32:05Z',
           'title': 'The iPhone 15 lineup has arrived, and here’s everything '
                    'you need to know about it',
           'url': 'https://www.theverge.com/23885548/apple-iphone-15-everything-need-know-news-announcement'},
          {'description': 'One of Windows 11’s biggest updates is now '
                          'available. Microsoft is rolling out Copilot and AI '
                          'enhancements to Paint, Snipping Tool, and more.',
           'publishedAt': '2023-09-26T17:00:00Z',
           'title': 'Windows 11’s next big update is now available with '
                    'Copilot, AI-powered Paint, and more',
           'url': 'https://www.theverge.com/2023/9/26/23890621/microsoft-windows-11-update-copilot-paint-snipping-tool-features'},
          {'description': 'The Microsoft Surface Laptop Studio 2, the Amazon '
                          'Echo Hub, the Orion app for iPad, The Continental, '
                          'and everything else you need in this week’s '
                          'Installer newsletter.',
           'publishedAt': '2023-09-24T12:00:00Z',
           'title': 'Apple’s new software is widgets all the way down',
           'url': 'https://www.theverge.com/23885600/ios-ipados-interactive-widgets-dalle-3-amazon-echo-installer-newsletter'},
          {'description': 'Image recognition and voice features aim to make '
                          "the AI bot's interface more intuitive.",
           'publishedAt': '2023-09-25T18:38:26Z',
           'title': 'ChatGPT update enables its AI to “see, hear, and speak,“ '
                    'according to OpenAI',
           'url': 'https://arstechnica.com/information-technology/2023/09/chatgpt-goes-multimodal-with-image-recognition-and-speech-synthesis/'},
          {'description': 'YouTube Music brings "Song details" to users on '
                          'Android and iOS.',
           'publishedAt': '2023-09-27T18:40:12Z',
           'title': "YouTube Music adds 'Song details' for extra "
                    'discoverability',
           'url': 'https://www.androidcentral.com/apps-software/youtube-music-song-details'},
          {'description': 'Threads rolls out a profile switcher and it looks '
                          'like an edit button is on the way.',
           'publishedAt': '2023-09-22T18:31:01Z',
           'title': 'Threads could get an edit button, with one condition',
           'url': 'https://www.androidcentral.com/apps-software/threads-rolls-out-profile-switcher'},
          {'description': 'Are you trying to understand how USB-C on the '
                          'iPhone 15 affects you? This is what it means for '
                          'accessory makers and the rest of the world.',
           'publishedAt': '2023-09-27T06:00:35Z',
           'title': 'USB-C on the iPhone 15: What it means for accessory '
                    'makers and the rest of the world',
           'url': 'https://www.androidcentral.com/phones/usb-c-iphone-15-what-this-means-for-accessory-makers'}],
 'status': 'SUCCESS'}
    """
    out_dict = {"data": []}
    from_date = from_date.strftime('%Y-%m-%d')
    to_date = to_date.strftime('%Y-%m-%d')
    all_articles = newsapi.get_everything(q=query,
                                          from_param=from_date,
                                          to=to_date,
                                          language=language,
                                          sort_by=sorty_by,
                                          page=1
                                          )
    if all_articles["status"] == "ok" and all_articles["totalResults"] > 0:
        out_dict["status"] = "SUCCESS"
    elif all_articles["status"] == "ok" and all_articles["totalResults"] <= 0:
        out_dict["status"] = "NO ARTICLES FOUND"
    else:
        out_dict["status"] = all_articles["status"]

    if out_dict["status"] == "SUCCESS":
        articles = all_articles["articles"][0:num_articles]
        for adict in articles:
            record =dict(title=adict["title"],
                         url=adict["url"],
                         publishedAt=adict["publishedAt"],
                         description=adict["description"])
            out_dict["data"].append(record)
    return out_dict




if __name__ == "__main__":
    query = "android ios"
    from_date = datetime.datetime.now()
    to_date = datetime.datetime.now() - datetime.timedelta(days=7)
    out_dict=get_news(query, from_date, to_date)
    print(out_dict)
