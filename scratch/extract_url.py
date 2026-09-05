import urllib.request, re
html = urllib.request.urlopen('https://razorpay-buidathon.vercel.app/').read().decode('utf-8')
js_file = re.search(r'/assets/index-[^\"]+\.js', html).group(0)
js_content = urllib.request.urlopen('https://razorpay-buidathon.vercel.app' + js_file).read().decode('utf-8')
urls = re.findall(r'https://[^\"]+railway\.app/?', js_content)
print('Found URLs:', urls)
