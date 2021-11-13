# GrubGridRecipeFinder
This project uses a Kaggle Dataset to parse a pandas dataframe and search for matching results.

[Link to the site](https://grubgrid-get-recipes.herokuapp.com/)

[Link to download my cleaned up .csv file](https://drive.google.com/uc?export=download&id=1tAjPlEKgceLlm2FWWlUd6Nw3MBThliW3)

### Purpose

I realized that meals are really divided up into two groups, “carbs” and “veggies” (later which will make a grid). The other stuff as far as meat, or not, glutens or not, those are all dietary needs.

All other recipe apps are either too many options (like searching on Google) or are too rigid (like pantry inventory management). So, having the flexibility of just inserting two ingredients is a nice balance. Either these are ingredients you want to buy, or currently have. It adds a good balance between flexibility and construct.

### Approach

I downloadeded the csv file [from Kaggle](https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions?select=PP_users.csv), deployed a heroku app using python and flask for the api endpoints. I also used Google’s programmable search engine to display the images. I was able to manipulate the csv using pandas and numpy which are python libraries.

### Future Goals

My next steps are adding a login feature, and then saving favorite recipes. Then, I can use Machine Learning (my ultimate goal) to recommend which recipes you’d want.

Also a friend of mine will be working on the front end.
