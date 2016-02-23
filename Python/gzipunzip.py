import gzip

zipfile = raw_input('file to be unzipped: ')
zipfilename = zipfile.split('.')
output = gzip.open(zipfile,'rb')
outfile = open(zipfilename[0]+"."+zipfilename[1],'wb')
content = output.read()
outfile.write(content)

print outfile.read()
print content

output.close()
outfile.close()
