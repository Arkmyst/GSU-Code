def extractQuotes(q1):
    test = q1.split('"')
    
    subqoute = test[1]

    inner = subqoute.split('"')

    return inner