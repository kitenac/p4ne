from flask import Flask, render_template, render_template_string
import sys
from backend import get_Info

# Создаём веб веб сервер и говорим откуда брать html и прочее
app = Flask(__name__, template_folder='templates')

# Demo frontend: - тут по html файлу с jinja-выражением рендер идёт
@app.route('/')
@app.route('/index')
def index():
    payload = f''' payload_index '''
    return render_template('index.html', payload=payload, urls=urls, lab_urls=lab_urls)

# Можно параметры урла доставать автоматом - тут - <name>
@app.route('/page2/<name>')
def page2(name):
    return f'параметр урла: {name}'

# Lab2.2 Frontend: - тут по <строке> с jinja выражением рендер
jinja_html = '''
    {{Title}}: <br>
    {% for x in List %}
            <a href="configs/{{x}}">{{x}}</a>
            </br>
        {% endfor %}
    '''
@app.route('/configs')
def configs():
    return render_template_string(jinja_html, List=Info.keys(), Title='Список устройств с конфигами')

@app.route('/configs/<host_name>')
def hosts_ips(host_name):
    return render_template_string(jinja_html, List=Info[host_name], Title=f'Список IP для {host_name}')

@app.route('/configs/<host_name>/<IP>/<mask>')
def ip_NET_page(host_name, IP, mask):
    return f'You`ve crawled too deep - <a href="/{host_name}"> go back :)</a>'

@app.route('/configs/<host_name>/<IP>')
def ip_page(host_name, IP):
    return f'You`ve crawled too deep - <a href="/{host_name}"> go back :)</a>'

if __name__ == '__main__':
    lab_urls = ['/', '/configs', '/configs/hostname']
    urls = ['/page2/Name', *lab_urls]
    Info = get_Info()
    app.run(debug=True)


