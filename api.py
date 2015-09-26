import urllib2
import json

locu_api = '756b03cefb059a8884816326b28c94a1a1bd7629'

url = "https://api.locu.com/v1_0/venue/search/?api_key=756b03cefb059a8884816326b28c94a1a1bd7629"


def locu_search(query):
    api_key = locu_api
    locality = query.replace(" ", "%20")
    final_url = "https://api.locu.com/v1_0/venue/search/?" + "locality=" + locality + "&category=restaurant" + "&api_key=" + api_key

    json_object = urllib2.urlopen(final_url)
    data = json.load(json_object)

    for item in data["objects"]:
        print item["name"], item["phone"]

locu_search("chicago")
