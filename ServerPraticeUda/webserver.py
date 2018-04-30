from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '<html><body>'

                output += '''<form method='POST'
                        enctype='multipart/form-data' action='/hello'>
                        <h2>Waht would you likel me to say?</h2>
                        <input name='message' type="text" >
                        <input type="submit" value="Submit"></form>'''
                output += '</body></html>'
                
                self.wfile.write(output)
                print (output)
                return

            if self.path.endswith('/hola'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                message = ''
                message += '<html><body>'
                
                output += '''<form method='POST'> 
                        enctype='multipart/form-data' action='/hello'>
                        <h2>Waht would you likel me to say?</h2>
                        <input name='message' type="text" >
                        <input type="submit" value="Submit"></form>'''

        except IOError:
            self.send_error(404, 'file not found %s'%self.path)


    def do_POST(self):

        try:
            print('something went wrong')
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            print('From this line , something went wrong') 
            ctype, pdict = cgi.parse_header(
                            self.headers.getheader('content-type'))
            print('1')
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            print('2')
            output = ''
            output += '<html><body>'
            output += '<h2> Okay.how about this:</h2>'
            output += '<h1 %s</h1>' %messagecontent[0]
            output += '''<form method='POST' 
                            enctype='multipart/form-data' action='/hello'>
                        <h2>Waht would you likel me to say?</h2>
                        <input name='message' type="text" >
                        <input type="submit" value="Submit"></form>'''

            output += '</body></html>'

            self.wfile.write(output)  # if you forget to write this code 
            print output              # you will get nothing after POST..      
        except:
                pass

def main():

    try: 
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "web sever runing on port{}".format(port)
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C enterd, stopping web server.."

if __name__ == '__main__':


    main()
