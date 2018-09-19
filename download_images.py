import urllib2
from time import sleep
import random

with open('image_links.txt', 'r') as image_links:
    urls = image_links.read().split(",")

processed = []
urlsCount = len(urls)
processedCount = 0;

for url in urls:

	filename = url.split('/')[-1];
	filedata = urllib2.urlopen(url);
	datatowrite = filedata.read();

	if(filename in processed):
		filename = str(random.randint(1,99999)) + "_" + filename;
		print("Duplicate filename. Changing to " + filename);
	else:
		processed.append(filename);

	with open('/home/thijs/Projects/imageshack-scraper/images/' + filename, 'wb') as f:  
	    f.write(datatowrite)

	processedCount += 1;
	print("Downloaded " + filename + " (" + str(processedCount) + " / " + str(urlsCount) + ")");
	sleep(1)

print("Downloaded all images! Check out your /images folder.")