from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import os
class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
        print(self.path)

        if(self.path=='/do_3d_reconstruction'):
            print("run 3d reconstruction")
            os.system('./generate_and_copy_file_to_django_dir.sh')


def run(server_class=HTTPServer, handler_class=Server, port=6060):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
