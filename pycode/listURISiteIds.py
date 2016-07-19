import cx
import json

def listURLSiteIDs():
    print 'SiteGroupName;SiteGroupId;SiteName;SiteId;SiteURL;DMPEnabled;Sentiment;Timezone'
    listSiteGroups = json.loads(cx.execute(cx.getUrl('/site/group'),'' , cx.username, cx.secret)[2])
    for siteGroup in listSiteGroups['siteGroups']:
        sites = siteGroup['siteIds']
        for siteid in sites:
            siteDefinition = json.loads(cx.execute(cx.getUrl('/site'), '{"siteId":"' + siteid + '"}', cx.username, cx.secret)[2])
            details = siteDefinition['sites']
            for  site in details:
                print siteGroup['name'] + ';"' + str(siteGroup['id']) + '";' + site['name'] + ';"' + str(site['id'])+ '";' + site['url'] + ';' + str(site['dmp']) + ';' + str(site['sentimentDetection']) + ';' + site['timeZone']

if __name__ == "__main__":
    listURLSiteIDs()
