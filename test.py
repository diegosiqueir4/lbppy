import lbppy

resource = lbppy.Resource.find("http://scta.info/resource/lectio1/critical/transcription")

# call for file part with specified kwargs
#text = resource.file(**{"path": "doc", "partid": "l1-cpspfs"})
html = resource.file().transform("https://raw.githubusercontent.com/lombardpress/lombardpress-web/develop/xslt/1.0.0/critical/main_view.xsl")
print(html)
