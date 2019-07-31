### Y2 2019 Summer: Basic Flask Lab

Welcome to the Intro to Flask lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

Throughout this lab, you should be editing `app.py`.

### Part 1: First web page!

In `app.py` edit the `home_page` function to return a string of your favorite food.

Open a terminal and run `python app.py`. If there are no errors, the terminal will say: Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Open chrome and enter the URL: `http://127.0.0.1:5000/` and make sure it prints your favorite food.

### Part 2: Adding a Template!

Remember that the folder `templates` is where we store all the html files.
Right now there is only one html file: `index.html`.
Open this file (in Sublime3) and edit it.

This template should have
- A heading, h1 tag, with your favorite food
- A paragraph about why it's the best food

Now, use the `render_template` function in `app.py` to see your
HTML page in the browser!

### Part 3: Adding CSS

The `static` folder is where we keep CSS and JS files. 
Right now there is just one file in the `static` folder: `style.css`.

Edit the file  `style.css` to make the background color in
your website green. 

Then, import this file in your HTML template. (if you don't remember how, look at the hints below)
Run the webserver again by running `python app.py` in the terminal, and check that the background is green.

If you have extra time, build a color scheme for your website.

### Part 4: Using Loops and Conditionals!

- First, add a for loop into your template, to print a list
of your favorite foods (sometimes you can't choose just one). This list should be defined
in your Python file `app.py` inside the `home_page` function.

- Define a variable `opposite_day` in `app.py`. Use an if-statement, in the html file and
if `opposite_day` is true then the website should show your least favorite foods.

### Part 5: Hints
To link a stylesheet, in the html file, add the line:
`<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">`

### Part 6: Extras

If you finish any of the previous parts early, you can work
on some extra tasks, including:

Part 2 Extras:
- Organize your website using divs in `index.html`
- Adding images to your website
- Finding and importing more complex templates from W3

Part 3 Extras:
- Add a header to your website, and make sure to use margins and padding
to separate the header from the content on the website
- Adding a sidebar to your website, that doesn't move when you scroll

Part 4 Extras:
- Add a table to the website, with pictures and descriptions about your favorite dishes.
- Adding more complex if-statements into your website - for instance, checking
how many foods the user wants to see. This should determine the length of the list you show.
- Instead of specifying exactly how many players
the user wants to see, the template should accept a variable `users_favorite_food`.
The website should print all the foods, until we print their favorite food. If this
is the first food, we only need to print one food. If their favorite isn't
in the list of your foods, then the entire list is printed.


