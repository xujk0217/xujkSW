from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html_content = """<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]>      <html class="no-js"> <!--<![endif]-->
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>xujk's personal web </title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href=""> 
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        
    </head>
    <body>
        <header>
            <h1>xujk's personal web</h1>
        </header>
        
        <div class="container">
            <section id="about" class="section">
                <h2>關於我</h2>
                <p>你好，我是xujk，這是我的個人網站。現在還在架鷹架還有找磚頭，只提供聯絡資訊。</p>
            </section>
        
        
            <section id="contact" class="section">
                <h2>聯絡我</h2>
                <p>email: kevin16021777@gmail.com </p>
                <p>phone number: +886 970332450</p>
            </section>
        </div>
        
        <footer>
            <p>&copy; xujk 2024</p>
        </footer>
        <script src="" async defer></script>
    </body>
</html>"""
        
        self.wfile.write(html_content.encode()) 