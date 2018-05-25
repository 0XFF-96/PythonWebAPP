def getCountry(ipAddress):

    try:
        response = urlopen('http://freegeoip.net/json/'
                            + ipAddress).read().decode('utf-8')
    except HTTPError:
        return None 
    responseJson = json.loads(response)

    return responseJson.get('country_code')

links = getLinks('/wiki/py')


