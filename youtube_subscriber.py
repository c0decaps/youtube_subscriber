from xml.etree import ElementTree
import sys, os.path

def extract_rss_urls_from_opml(filename):
    channels = {}
    with open(filename, 'rt') as f:
        tree = ElementTree.parse(f)
    for channel in tree.findall('.//outline'):
        title = channel.attrib.get('title')
        url = channel.attrib.get('xmlUrl')
        if url and title:
            channels[title] = url.split("channel_id=")[1]
    return channels

def create_html_file(channel_id_dict):
    file = open('subscriptions.html', 'w')
    file.write('<html>')
    file.write('<center>')
    for channel in channel_id_dict:
        file.write('<a target="_blank" href="https://www.youtube.com/channel/'+str(channel_id_dict[channel])+'?sub_confirmation=1">'+str(channel)+'</a><br><br>')
    file.write('</html>')
    file.close()
    print('Sucessfully created file.')


if __name__ == '__main__':
    filename = 'subscription_manager'
    if(len(sys.argv) > 1):
        filename = sys.argv[1]
    if os.path.isfile(filename):
        urls = extract_rss_urls_from_opml(filename)
        create_html_file(urls)
    else:
        print("Error: Please specify subscription manager file. (python youtube_subscriber.py filename.txt)")
