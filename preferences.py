def getAssetsUrl():
    return r'https://api.polyhaven.com/assets?t=hdris&c=outdoor'

def getAssetDetailUrl(img, size):
    return r'https://cdn.polyhaven.com/asset_img/primary/' + img + '.png?height=' + str(size)