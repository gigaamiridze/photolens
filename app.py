from flask import Flask, render_template

app = Flask(__name__)

# Main pages
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Media page and its sub-pages
@app.route('/project-categories/media')
def media():
    return render_template('media.html')

@app.route('/project/back-to-school')
def back_to_school():
    return render_template('back-to-school.html')

@app.route('/project/gaming-contest')
def gaming_contest():
    return render_template('gaming-contest.html')

# Events page and its sub-pages
@app.route('/project-categories/events')
def events():
    return render_template('events.html')

@app.route('/project/rooftop-concert')
def rooftop_concert():
    return render_template('rooftop-concert.html')

# Portraits page and its sub-pages
@app.route('/project-categories/portraits')
def portraits():
    return render_template('portraits.html')

@app.route('/project/jim-tina-couple')
def jim_tina():
    return render_template('jim-tina.html')

@app.route('/project/mia-whitney')
def mia_whitney():
    return render_template('mia-whitney.html')

# Landscape page and its sub-pages
@app.route('/project-categories/landscape')
def landscape():
    return render_template('landscape.html')

@app.route('/project/flash-waves')
def flash_waves():
    return render_template('flash-waves.html')

@app.route('/project/l-a-birds-view')
def birds_view():
    return render_template('birds-view.html')

# category pages from shop page
@app.route('/category/people')
def people():
    return render_template('people.html')

@app.route('/category/brand')
def brand():
    return render_template('brand.html')

@app.route('/category/landscape')
def shop_landscape():
    return render_template('shop-landscape.html')

# product pages from shop page
@app.route('/product/ying-yang')
def ying_yang():
    return render_template('ying-yang.html')

@app.route('/product/tesla')
def tesla():
    return render_template('tesla.html')

@app.route('/product/unconcept')
def unconcept():
    return render_template('unconcept.html')

@app.route('/product/kirkjufell')
def kirkjufell():
    return render_template('kirkjufell.html')

if __name__ == '__main__':
    app.run(debug=True, port=7777)