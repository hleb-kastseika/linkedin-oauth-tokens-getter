import oauth2 as oauth
import urllib

consumer_key = '' #from Linkedin site
consumer_secret = '' #from Linkedin site
consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
resp, content = client.request(request_token_url, "POST")
if resp['status'] != '200' :
    raise Exception('Invalid response %s.' % resp['status'])
content_utf8 = str(content,'utf-8')
request_token = dict(urllib.parse.parse_qsl(content_utf8))
authorize_url = request_token['xoauth_request_auth_url']

print('Go to the following link in your browser:', "\n")
print(authorize_url + '?oauth_token=' + request_token['oauth_token'])

accepted='n'
while accepted.lower() == 'n' :
    accepted = input('Have you authorized me? (y/n)')
oauth_verifier = input('What is the PIN?')

access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)
resp, content = client.request(access_token_url, 'POST')
content8 = str(content,'utf-8')
access_token = dict(urllib.parse.parse_qsl(content8))

print('Access Token:', "\n")
print('- oauth_token        = ' + access_token['oauth_token']+'\n')
print('- oauth_token_secret = ' + access_token['oauth_token_secret'])
print('You may now access protected resources using the access tokens above.')
