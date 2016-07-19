import cx
import csv


def writetofile(sitename, siteurl, siteid):
    print '"' +  siteurl + '":' +  siteid.split(':')[1]

def createsite(sitename, siteurl):
    # ATLANTIC 1139578605085513194
    # QUEBEC 1139578605085513192
    localsitegroup = '{"siteGroupId":"1139578605085513194",'  #change this when switching SiteGroups
    name = '"name":"' +  sitename + '",'
    uri = '"url":"' +  siteurl + '",'
    country = '"country":"Canada",'
    timezone = '"timeZone":"America/Atlantic"}'  #change this when switching SiteGroups
    param = localsitegroup +  name + uri + country + timezone
    createloc = cx.getUrl('/site/create')
    response = cx.execute(createloc ,param,cx.username,cx.secret)

    writetofile(sitename, siteurl, response[2])

if __name__ == "__main__":
    with open('/Users/tweediej/Desktop/atl.csv','rU') as f:  #change this with your path
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            createsite(row[0].split(';')[0], row[0].split(';')[2])

