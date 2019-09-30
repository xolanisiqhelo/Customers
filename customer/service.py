from xml.dom import minidom


def get_code_reference():
    url = "http://197.97.154.196/live/logic/courier_demo"
    string = ('sample.xml')
    print(string)
    myTree = minidom.parse(string)

    statusCode = myTree.getElementsByTagName('CustomerCode')
    a = []
    for x in statusCode:
        try_list = x.firstChild.data
        print(try_list)
        a.append(try_list)
    out = a
    print(out)


class QueryExternalAPI(object):
    get_code_reference()
