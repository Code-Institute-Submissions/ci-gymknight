# GymKnight - Performance. Elevated.

![Gymknight logo](../static/img/gk-logo-sm.png "Bloggy logo Logo")

## Testing

## Table of Contents
1. [**Manual Testing**](#manual-testing)
    - [**Home page**](#🛠-home-page)
    - [**Viewing products**](#🛠-viewing-products)
    - [**Search**](#🛠-search)
    - [**Viewing single product details**](#🛠-viewing-single-product-page)
    - [**Sort by**](#🛠-sort-by)
    - [**Adding an item to cart**](#🛠-adding-an-item-to-cart)
    - [**Viewing shopping cart**](#🛠-viewing-shopping-cart)
    - [**Updating quantity of the item in cart**](#🛠-updating-quantity-of-the-item-in-cart)
    - [**Removing item from cart**](#🛠-removing-item-from-cart)
    - [**Checkout**](#🛠-checkout)
    - [**Successful order**](#🛠-successful-order)
    - [**Creating an user account**](#🛠-creating-an-user-account)
    - [**Logging in**](#🛠-logging-in)
    - [**Viewing order history**](#🛠-viewing-order-history)
    - [**Adding products**](#🛠-adding-products)
    - [**Editing a product**](#🛠-editing-a-product)
    - [**Deleting a product**](#🛠-deleting-product)
2. [**Devices and tools used**](#devices-and-tools-used)

## Manual testing

### 🛠 Home page

Upon loading the user is presented with current offers - in the current case "Winter Gear Has Landed". By clicking the CTA button user is brought to the All products view.
No issues to report - all works as expected.
### 🛠 Viewing products

Users are able to view product by clicking on Merchandise and selecting which category they wish to view or if they wish to view all products.
View is filtered based on the category and only products in that category display to the user. No issues to report - all works as expected.

### 🛠 Search

Users are able to search for products based on the product name or description. The view is refreshed and product filtered based on the users query.
No issues to report - all works as expected.
### 🛠 Viewing single product details

By clicking on the product name, users are able to view details of a single product:

1. Product name
2. Product price
3. Rating
4. Description

Users can also select the size if they wish to add the item to their cart and change the quantity to be added. No issues to report - all works as expected.

### 🛠 Sort by

1. Name (A-Z)
2. Name (Z-A)
3. Price (Low-High)
4. Price (High-Low)
5. Rating

The view then refreshes and sorts products by selected parameter, ascending or descending. No issues to report - all works as expected.

### 🛠 Adding an item to cart

By specifying the quantity and selecting a size (if applicable) and clicking the Add to Cart button, product is added to cart and the Cart in the top right hand corner updates to orange colour and value of current cart is displayed. No issues to report - all works as expected.

### 🛠 Viewing shopping cart

By clicking on the cart in the top right hand corner users are able to view their current cart. The cart will display all items in their cart, details of the products including name, size, unit price, subtotal, delivery costs and grand total. No issues to report - all works as expected.

### 🛠 Updating quantity of the item in cart

Users have 2 ways to update the quantity of the product in their cart. First is to add the same size and type product to cart which will update the quantity (same type but different size will result in 2 different sizes in the cart as 2 separate items). Second is by typing in the desired number in the quantity field in the shopping cart and clicking Update Cart. No issues to report - all works as expected.

### 🛠 Removing item from cart

Item can be removed from cart by clicking 'Remove item' in the shopping cart view. The item will disappear from the page. No issues to report - all works as expected.

### 🛠 Checkout

Once there is a product in the cart users can proceed to checkout. The view present user with their order summary and provides a form for users personal and shipping details. All fields but Address Line 2 & Postcode are required and form will throw an error if any of them are omitted. 

By ticking the "Save details" checkbox, user can choose to save the delivery details to their profile for future orders. This checkbox only shows for registered and logged in users.

To test a successful payment Stripes internal testing card number 4242424242424242 should be used along with any future date as expiry date and any 3 digit CVV number and any 5 digit postcode. 

Unsuccessful payments are handled via Stripe directly and users will be presented with an error in an event of card being declined. 

### 🛠 Successful order

Once the user has completed the payment sucessfully, the order summary will be displayed with all details regarding the order, users personal and delivery details.

### 🛠 Creating an user account

Users can register for an account by navigating to Account - Register using the main navigation menu.

All fields of the form are required and an error is thrown if the user misses or incorrectly fills a field (ie. email)

All authentification is handled through django-allauth.

### 🛠 Logging in

Users can register for an account by navigating to Account - Log in using the main navigation menu and supplying correct username and password.

### 🛠 Viewing order history

Order history will be displayed if user has completed any orders in the past (otherwise an empty table is shown). Order details include oder number, date, contents and price.

### 🛠 Adding products

This is a superuser feature only. If the user is logged in as superuser they can add a product using the website (rather than Django Admin) by supplying all relevant product details. Only non-required field is the image field.
If no image is supplied, default image will be assigned to the product.

### 🛠 Editing a product

This is a superuser feature only. If the user is logged in as superuser they can edit a product using the website by clicking on 'Edit' in the main products view or on product details page. 
If no image is supplied or if image is removed (cleared), default image will be assigned to the product.

### 🛠 Deleting a product

This is a superuser feature only. If the user is logged in as superuser they can delete a product using the website by clicking on 'Delete' in the main products view or on product details page.

## Devices and tools used

App has been tested on the following devices/browsers and no known issues could be reported:

1. Macbook Pro 13" (macOS 11 Big Sur)
    * Google Chrome (v87)
    * Safari (v14.01)
    * Firefox (v83)
    * Opera (v73)
2. Desktop PC (Windows 10)
    * Google Chrome (v87)
    * Edge (v87)
    * Firefox (v83)
3. iPhone 11 Pro Max (iOS 14.2)
    * Safari 
4. iPhone XR (iOS 14.2)
    * Safari

Python code has been checked using [PEP8 Compliance checker](http://pep8online.com/)

CSS has been validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator)

HTML has been checked (validation will always fail due to Django/Jinja templating language being used) using [W3C Markup Validator](https://validator.w3.org/)
 
