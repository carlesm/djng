# Create your views here.
from django.http import HttpResponse

def mainpage(request): 
    output = '''
        <html>
        <head><title>%s</title></head>
        <body>
        <h1>%s</h1><p>%s</p>
        </body>
        </html>
        ''' % ( 'Sobres aPP',
        'Welcome to the Sobres aPPlication',
        'Managing non legal funding since 2013')
    return HttpResponse(output)

