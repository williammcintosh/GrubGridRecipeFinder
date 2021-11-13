import numpy as np
import pandas as pd
from flask import Flask
from flask import request
from flask import json
from googleapiclient.discovery import build


app = Flask(__name__)

@app.route('/grabimage/<string:search_term>')
def get_image(search_term):
    api_key = "mykey"
    resource = build("customsearch", 'v1', developerKey=api_key).cse()
    result = resource.list(q=search_term, cx="0a2fb8613582786f9",searchType='image').execute()
    return str(result['items'][0]['link'])

@app.route('/by_ingredient/<string:ingredient_list>')
def by_ingredient(ingredient_list):
    ing = [str(idx) for idx in ingredient_list.split(',')]
    recipes_df = pd.read_csv("cleanedup_RAW_recipes.csv")

    results_one = recipes_df.loc[recipes_df['ingredients'].str.contains(ing[0], case=False)]
    results_two = results_one.loc[results_one['ingredients'].str.contains(ing[1], case=False)]

    result = results_two.to_json(orient="records")
    parsed = json.loads(result)

    maximum = min(int(ing[2]), len(parsed))
    recipes = ""

    for i in range(0,maximum):
        recipe_name = parsed[i]['name']
        image_link = (
            """
            <img src="
            """
            + get_image(recipe_name) +
            """
            " alt="burger" width="300">
            """
        )
        recipes += (
            image_link
            + """
            <br><h1>
            """
            + recipe_name
            + """
            </h1><h3>Ingredients</h3>
            """
            + json.dumps(parsed[i]['ingredients'])
            + """
            </h1><br><h3>Steps</h3>
            """
            + json.dumps(parsed[i]['steps'])
            + """
            <br><br><br>
            """
        )
    return recipes
        

    # Makes all json objects into a string
    #return json.dumps(parsed, indent=4)

@app.route("/")
#def index():
def home():
    args = request.args.getlist("param")
    if len(args) > 2 and str(args[2]) != "":
        print(len(args))
        print(args[2])
        recipes = (
            "<br> <big>Resulting Recipes with "
            + args[0]
            + " and "
            + args[1]
            + ": </big><br><br><br>"
            + by_ingredient(str(args[0]+","+args[1])+","+str(args[2]))
        )
    else:
        recipes = "Please fill out all three fields"
    return (
        """
        <form action="" method="get">
                <br><big>Enter two ingredients:</big><br><br>
                Ingredient One:<br>
                    <input type="text" name="param" value="potato" /><br>
                Ingredient Two:<br>
                    <input type="text" name="param" value="broccoli" /><br>
                Max Results::<br>
                    <input type="number" id="quantity" name="param" value="5" min="1" max="100" /><br><br>
                <input type="submit" value="SUBMIT">
        </form>
        """
        + recipes
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
