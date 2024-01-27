# Flask Boilerplate
Your simple, yet opinionated, boilerplate for Flask projects.

## Why?
I've been using Flask for a while now, and I've found myself repeating the same steps over and over again when starting a new project. In order to save myself (and you) some time, I decided to create this boilerplate.

## Features
- User authentication (login, logout, register)
- 'Sane' defaults for Flask configuration
- A understandable project file structure
- A simple SQLite database (you can, of course, replace this with any other database that SQLAlchemy supports)
- Jinja2 templates with Flowbite (Tailwind) CSS (CDN version)
- A CLI for managing aspects of your project (use `kettle --help` to see the available commands)*

**In order to use `kettle`, you will need to install it with `pip install --editable cli` from the root directory of the project.*

## Get started

*I'm assuming you have Python 3.11+ installed on your machine and that you are comfortable with using the command line on your machine.*

1. Clone this repository and `cd` into it
2. Create a virtual environment with `python3 -m venv venv` (or `python -m venv venv` if you're on Windows) and activate it with `source venv/bin/activate` (or `venv\Scripts\activate.bat` if you're on Windows)
3. Install the dependencies with `pip install -r requirements.txt`
4. Run the application with `flask run` (or `python -m flask run` if you're on Windows) - you can also append `--debug` to enable debug mode
5. Open your browser and go to `http://localhost:5000`

And voilà, you're ready to open this project in your favorite editor and start working on your next big thing!

## Contributing
If you have any suggestions or improvements, then feel free to open an issue or a pull request. I'll be happy to take a look at it!

## Thanks

### Icons
The boiler, gears and download icon (as seen on the front page) are sourced from [Icons8](https://icons8.com/).

### CSS/UI
The CSS and UI is sourced from [Flowbite](https://flowbite.com/), which is a library of components and layouts for [Tailwind CSS](https://tailwindcss.com/).

### User profile avatars
The user profile avatars are sourced from [UI Avatars](https://ui-avatars.com/).

### Libraries
- [Flask](https://flask.palletsprojects.com/en/)
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

*See the `requirements.txt` for the full list of libraries that is used.*

## License/Legal/"Don't sue me, thanks" section
The boilerplate is not licensed, however, the libraries used are. Please check the respective licenses for each library.

Disclaimer: Flask is a trademark of [Pallets](https://palletsprojects.com/), and is not affiliated with this project in any way.