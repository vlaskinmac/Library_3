from livereload import Server

from render_website import rebuild


if __name__ == "__main__":
    rebuild()
    server = Server()
    server.watch('Library_3/*.html', rebuild)
    server.serve(root='.')