import urllib2
outfile=open("source.html","w")
outfile.write(urllib2.urlopen("http://haozi.freetzi.com").read())
outfile.close()
