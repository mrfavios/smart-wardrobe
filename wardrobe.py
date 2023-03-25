from flask import Flask, render_template, request, redirect, url_for
import os
import json
import socket

app = Flask(__name__)

def get_images():
    shirts = os.listdir("static/img/shirts")
    pants = os.listdir("static/img/pants")
    shoes = os.listdir("static/img/shoes")
    return shirts, pants, shoes

def get_image_by_index(category, index):
    images = os.listdir("static/img/" + category)
    if index < 0:
        index = len(images) - 1
    elif index >= len(images):
        index = 0
    image_name = images[index]
    return image_name
    
@app.route("/")
def index():

    shirts, pants, shoes = get_images()
    
    shirt_index = int(request.args.get("shirt_index", 0))
    pant_index = int(request.args.get("pant_index", 0))
    shoe_index = int(request.args.get("shoe_index", 0))
    
    shirt_image = get_image_by_index("shirts", shirt_index)
    pant_image = get_image_by_index("pants", pant_index)
    shoe_image = get_image_by_index("shoes", shoe_index)
    
    return render_template("index.html", shirts=shirts, pants=pants, shoes=shoes, shirt_image=shirt_image, pant_image=pant_image, shoe_image=shoe_image, shirt_index=shirt_index, pant_index=pant_index, shoe_index=shoe_index)

@app.route("/save_outfit/<shirt>/<pant>/<shoe>/<season>")
def save_outfit(shirt, pant, shoe, season):
    data = {"shirt": shirt, "pant": pant, "shoe": shoe, "season": season}
    
    with open("outfit.json", "r") as f:
        outfits = json.load(f)

    outfits.append(data)

    with open("outfit.json", "w") as f:
        json.dump(outfits, f, indent=4)

    return redirect(url_for("outfit_saved"))

def get_outfits():
    outfits_a = []
    outfits_b = []

    with open("outfit.json", "r") as f:
        outfits = json.load(f)

    for outfit in outfits:
        shirt = outfit["shirt"]
        pant = outfit["pant"]
        shoe = outfit["shoe"]
        season = outfit["season"]

        if season == "s":
            outfits_a.append({"shirt": shirt, "pant": pant, "shoe": shoe})
        else:
            outfits_b.append({"shirt": shirt, "pant": pant, "shoe": shoe})

    return outfits_a, outfits_b

@app.route("/outfit_saved")
def outfit_saved():
    outfits_a, outfits_b = get_outfits()
    return render_template("outfit_saved.html", outfitsa=outfits_a, outfitsb=outfits_b)

@app.route("/delete_outfit/<shirt>/<pant>/<shoe>/<season>")
def delete_outfit(shirt, pant, shoe, season):
    with open('outfit.json', 'r') as f:
        outfits = json.load(f)
    
    for outfit in outfits:
        if outfit['shirt'] == shirt and outfit['pant'] == pant \
        and outfit['shoe'] == shoe and outfit['season'] == season:
            outfits.remove(outfit)
            break
    
    with open('outfit.json', 'w') as f:
        json.dump(outfits, f)
        
    outfits_a, outfits_b = get_outfits()
    return render_template("outfit_saved.html", outfitsa=outfits_a, outfitsb=outfits_b)
    
if __name__ == "__main__":

	ip = socket.gethostbyname(socket.gethostname())
	app.run(host=ip)
