from livereload import Server

from render_website import rebuild

rebuild()

server = Server()
server.watch('Library_3/*.html', rebuild)
server.serve(root='.')