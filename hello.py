 def app (environ, start_response):
  status = '200 OK'
  headers = [('Content-type','text/plain')]
  start_response(status, response_headers)
  resp = environ['QUERY_STRING'].split("&")
  resp = [item+"\r\n" for item in resp]
  return resp
