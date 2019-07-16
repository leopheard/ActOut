from xbmcswift2 import Plugin, xbmcgui
from resources.lib import actout

plugin = Plugin()

URL = "https://actout.libsyn.com/page/1/size/1600"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://popularresistance-uploads.s3.amazonaws.com/uploads/2018/12/act-out.jpg"},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://popularresistance-uploads.s3.amazonaws.com/uploads/2018/12/act-out.jpg"},
    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = actout.get_soup(URL)
    
    playable_podcast = actout.get_playable_podcast(soup)
    
    items = actout.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = actout.get_soup(URL)
    
    playable_podcast1 = actout.get_playable_podcast1(soup)
    
    items = actout.compile_playable_podcast1(playable_podcast1)

    return items


if __name__ == '__main__':
    plugin.run()
