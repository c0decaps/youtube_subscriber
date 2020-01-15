# youtube_subscriber

YouTube has the option to [export your subscriptions into a xml/opml file](https://www.youtube.com/subscription_manager), e.g. for rss feeds. Because there is no option to transfer ones subscriptions to a new account this script uses the exported file to create a html file for a human readable list of the channels subscribed to.  
When clicked on the URLs one will be directed to a youtube page with a prompt which lets you decide whether or not to subscribe the depending account.  

The URLs are constructed like the following: 
```
https://www.youtube.com/channel/ID?sub_confirmation=1
```
where ID corresponds to the channels ID, which is inserted in that URL when iterating through the channels in the list
