# 🧀🧀🧀 CheeseShop Inventory 🧀🧀🧀
A fullstack webapp tracking and managing cheese products' details, stock and providers. It was built using OOP and modelled on an MVC pattern.
<br />

This was my first app! 😊
<br />

**Tech Stack:** Python3, HTML, CSS, Flask and PostgreSQL


<img width="1399" alt="Screenshot 2022-06-11 at 20 09 08" src="https://user-images.githubusercontent.com/101068957/173203760-1e6d7ea6-9dfe-4256-b460-3c579bf5f0ba.png">

## Installs
1. Make sure you have Python3, Flask, PostgreSQL and psycopg2 all installed.
2. Open the command line and navigate to the folder you want to store the app in.
3. Copy-paste the below in your command line and press Return:

        git clone git@github.com:Vallalika/Cheese_shop_inventory.git
        
    *The app folder is now created and should be visible.*

## Database setup
1. Go to the **Cheese_shop_inventory** folder, then to the **app** folder with the command line.
2. Type the below to create the cheese_shop database and populate it with data.
        
        createdb cheese_shop
        
        psql -d cheese_shop -f db/cheese_shop.sql
        
        python3 db_load.py
## Run
1. Copy-paste the below in the command line, still in the app folder.
        
        flask run
     *That should be Flask running now*
     
2. Open Chrome and copy-paste the below in the address bar.

        http://127.0.0.1:4999/

**The CheeseShop Inventory app should now fully be running in Chrome!**
