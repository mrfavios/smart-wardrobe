<h1>Smart Wardrobe - Outfit Management System</h1>

This is a Python and Flask-based project for managing outfits in a smart wardrobe. The project allows users to create outfits using pre-saved items of clothing, such as pants, shirts, and shoes.

<h2>Getting Started</h2>

To get started, clone the project to your local machine using the following command:

<code>git clone https://github.com/mrfavios/smart-wardrobe.git</code>

Once you have cloned the project, navigate to the project directory and install the necessary packages using the following commands:

    <code>pip install Flask</code>
    <code>pip install json</code>
    <code>pip install socket</code>

Next, you will need to save images of your clothing items to the appropriate folders in the static/img directory. The images should be saved to the following folders:

    static/img/pants
    static/img/shirts
    static/img/shoes

The project comes with pre-saved outfits, which can be found in the outfit.json file.

To run the project, open a terminal window and navigate to the project directory. Then, run the following command:

python app.py

This will start the Flask application and you can access the smart wardrobe system by opening your web browser and navigating to http://(your local ip):5000.

<h2>How it Works</h2>

The smart wardrobe system allows users to view their clothing items and create outfits by selecting items from each category. Users can also save outfits for future reference.

The project uses Python and Flask for the backend, and HTML, CSS, and JavaScript for the frontend.

<h2>Contributing</h2>

If you would like to contribute to the project, please create a pull request with your changes.
