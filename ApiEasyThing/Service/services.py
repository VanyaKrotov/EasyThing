def getWorkScheduleDateFromString(data):
    if not data:
        return None

    resultArray = data.split('-')

    return {
        'before': resultArray[0],
        'after': resultArray[1]
    }