from xml.etree import ElementTree
def extract_rss_urls_from_opml(filename):
    #urls = []
    channels = {}
    with open(filename, 'rt') as f:
        tree = ElementTree.parse(f)
    for channel in tree.findall('.//outline'):
        title = channel.attrib.get('title')
        url = channel.attrib.get('xmlUrl')
        if url and title:
            #urls.append(url)
            channels[title] = url.split("channel_id=")[1]
    #return urls
    return channels

def create_html_file(channel_id_dict):
    file = open('subscriptions.html', 'w')
    file.write('<html>')
    file.write('<center>')
    for channel in channel_id_dict:
        file.write('<a href="https://www.youtube.com/channel/'+str(channel_id_dict[channel])+'?sub_confirmation=1">'+str(channel)+'</a><br><br>')
    file.write('</html>')


urls = extract_rss_urls_from_opml('subscription_manager')
print(urls)
create_html_file(urls)