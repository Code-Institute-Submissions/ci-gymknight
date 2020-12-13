# GymKnight - Performance. Elevated.

![Gymknight logo](static/img/gk-logo-sm.png "Bloggy logo Logo")

GymKnight is an online webshop for fitness enthusiasts to purchase premium clothing products as well as home and training accessories.

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Strategy**](#strategy)
    - [**Scope**](#scope)
    - [**Structure**](#structure)
    - [**Skeleton**](#skeleton)
    - [**Surface**](#surface)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

 
## UX
 
### User stories

📌 As a user I want to access the website and browse products on offer

📌 As a user I want to be able to see product details, image and available sizes

📌 As a user I want to be able to add desired item to my cart

📌 As a user I want to be able to purchase the desired product(s) and get them shipped to my address

📌 As a user I want to be able to pay using my debit or credit card

📌 As a user I want to be able to register for an account

📌 As a user I want to save entered details for future purchases

📌 As a user I want to be able to see my previous purchases

📌 As a store owner I want to be able to add, edit and remove products

### Strategy

The main design goal is to provide a modern and sleek UI that presents products in an organised way (using categories) and allow users seamless start to finish experience.

### Scope

GymKnight is an online webshop for fitness enthusiasts to purchase premium clothing products as well as home and training accessories.

### Structure

Index page is simple and contains a call a jumbotron that shows users new gear that's available in the webshop & a call to action button to go to the products page.
Underneath that users can see the reasons why to choose GymKnight - premium materials, free shipping over certain order amount and because it's an Irish brand.

User is able to view the products based on the category - Mens, Ladies, Accessories, Homeware & Living and by viewing all products. 

Products page features card layout of all available products in the specified category. The cards feature image of the product, their description, category they belong to & their rating.

By clicking on the product user is able to see all the same details as well as product price, and is able to select the size and quantity to be added to their cart.

Shopping cart page displays product SKU, Product info (including name, description, size and quantity) as well as unit price and the subtotal. Bottom three rows display current total, delivery charge (if applicable) and the grand total for the order. From here, users are able to proceed to checkout or go back and continue shopping.

Checkout page displays user's oder summary, total, delivery and grand total amounts in a table. On the right hand side (desktop layout) user are asked for their personal, delivery and credit/debit card details. 

Once the order is successfully paid for, the user is presented with a confirmation screen which displays the entered information about delivery and products ordered.

User account page (accessible for registered users only) displays saved user delivery information which they're able to edit as well as their order history. 

### Skeleton

Balsamiq Wireframes has been used to develop wireframes for this website.

Wireframes are available under links below and are stored within _wireframes_ folder inside _docs_ folder.

[Home page wireframe](/docs/wireframes/home-page.png)

[Merch/products wireframe](/docs/wireframes/merch-page.png)

[Shopping cart wireframe](/docs/wireframes/shopping-cart.png)

[Single item page wireframe](/docs/wireframes/single-item.png)

[User profile page wireframe](/docs/wireframes/user-profile.png)

### Surface


| Colour name       | Colour RGB Code    
| -------------     |:-------------:| 
| Bittersweet       |#FF715B
| White             |#FFFFF

Font used on the website is [Montserrat from Google Fonts](https://fonts.google.com/specimen/Montserrat)

## Features

### Existing Features

🟢 **Home page**

Users are able to navigate using top navigation menu, access current products, their account and shopping card. Users can also view the reasons why choose GymKnight.

🟢 **Browse products on offer**

User is able to view the products based on the category - Mens, Ladies, Accessories, Homeware & Living and by viewing all products. 

🟢 **View product details**

Users are able to view product details by clicking on the product name. Details include name, price, description, rating, sizes available and an option to add the item to cart

🟢 **Add items to cart**

Once the user selects the size they wish to add, they can add the product by simply clicking add to cart on the product details view.

🟢 **View cart**

By clicking on the cart icon on the upper right of the screen (desktop layout), users are able to navigate to their cart and see current items in their cart.
Users are also able to update quantity and remove the product from the cart entirely.

🟢 **Proceed with order and payment**

Once in their cart, user can click on 'Secure Checkout' button which will navigate them to the checkout view where they're required to enter personal and delivery details as well as their card details.

🟢 **Create an account**

By clicking on Account in the main menu, users are able to register for an user account which will be used to save future orders into their history as well as delivery details.

🟢 **Edit saved personal and shipping details**

By clicking on "Edit profile" user can edit their delivery details with new information.

🟢 **View order history**

Beside their details users are able to view their past orders in chronological order and they can also view the contents of the orders themselves.
### Features Left to Implement

🔴 **Wishlist**

It would be great to implement a wishlist feature like those Amazon and the likes have for saving interesting products for later.
## Technologies Used

1. HTML5
2. CSS3
3. [Google Fonts](https://fonts.google.com/)
4. JavaScript
5. Python 
6. [Django 3.1](https://docs.djangoproject.com/en/3.1/)
7. AWS S3
8. Heroku for Deployment

## Testing

Please refer to [TESTING.md](./docs/TESTING.md) for testing documentation

## Deployment

To deploy this app on your own, you can clone this repository or download it and upload again to your own repository via CLI.

(Creation of AWS account, setting up Stripe, setting up S3 bucket and the rest has been omitted in interest of keeping this as a summary. Expert knowledge in the deployment of Django apps is assumed)

1. Create a Heroku account if you don't have one already.
2. Create a new app
3. Navigate to _Settings_ tab for your app and click on _Reveal Config Vars_
4. Populate config vars with the following details: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET, USE_AWS (this should be set to True for production).
5. Create an _env.py_ file in and IDE you wish to use (VSCode, Atom), populate the above variables using your AWS/Stripe details and add your _env.py_ file to _.gitignore_ file **(this is very important)**
6. Create a _requirements.txt_ file by typing `pip3 freeze > requirements.txt` in the command line of your IDE
7. Create a Procfile in the root of your project and copy-paste the following `gymknight.wsgi:application app.py`
8. Commit all and push to remote origin on GitHub
9. Under _Deployment_ tab in your Heroku app, connect your GitHub account and select desired repo you wish to deploy.

Heroku CLI can also be used to push files directly to Heroku via the command line.

## Credits

CodeInstitute's Boutique Ado tutorial was followed in the making of this project.

### Content

All the textual has been created by myself.
### Media

Product images have been generated using [Printify](https://printify.com)

Stock images have been sourced from [Pexels](https://www.pexels.com/)