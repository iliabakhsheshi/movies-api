import requests as requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)


@app.route('/<string:movie_id_id>',methods=["POST","GET"])
def movies_api(movie_id):
    import json
    # Convert to str
    movie_id = str(movie_id)
    # Create the link for request
    url_date = '''https://www.imdb.com/title/{}'''.format(movie_id)
    source = requests.get(url_date)
    soup = BeautifulSoup(source.content, "html.parser")
    # Find information in imdb site
    html_code = soup.find('script', type="application/ld+json")
    html_code = str(html_code)
    html_code = html_code.replace('<script type="application/ld+json">', "")
    html_code = html_code.replace('</script>', "")
    # Convert to json
    json_file = json.loads(html_code)
    # Return json
    return json_file


if __name__ == '__main__':
    app.run()
