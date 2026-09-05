import urllib.request, re
html = urllib.request.urlopen('https://razorpay-buidathon.vercel.app/').read().decode('utf-8')
js_file = re.search(r'/assets/index-[^\"]+\.js', html).group(0)
js_content = urllib.request.urlopen('https://razorpay-buidathon.vercel.app' + js_file).read().decode('utf-8')
urls = re.findall(r'\"https?://[^\"]+\"', js_content)
for u in urls:
    if 'railway' in u.lower():
        print('Found URL:', u)
