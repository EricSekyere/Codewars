'''
A method that does the following:
Removes any duplicate query string parameters from the url
Removes any query string parameters specified within the 2nd argument (optional array)

Examples:
stripUrlParams('www.codewars.com?a=1&b=2&a=2') // returns 'www.codewars.com?a=1&b=2'
stripUrlParams('www.codewars.com?a=1&b=2&a=2', ['b']) // returns 'www.codewars.com?a=1'
stripUrlParams('www.codewars.com', ['b']) // returns 'www.codewars.com'

'''

def strip_url_params(url, params_to_strip=[]):
    #extract params
    params = url[url.find("?")+1:]
    sorted_params, sorted_params_2 = [], []
    paramsArr = params.split("&")

    for param in paramsArr:
      if (param[:param.find("=")]) not in sorted_params_2:
        sorted_params_2.append(param[:param.find("=")])
        sorted_params.append(param)

    for index, arg in enumerate(sorted_params):
        if arg[:arg.find("=")] in params_to_strip:
            sorted_params[index] = ""
    return(url if not paramsArr else url[:url.find("?")+1] + "&".join([x for x in sorted_params if x]))
