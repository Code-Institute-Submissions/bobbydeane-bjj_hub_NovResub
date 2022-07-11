# BJJ Hub

BJJ Hub is a e-commerce store that supplies Brazilian Jiu Jitsu apparel and goods. The site is built using the Django Framework in python and is heavily beased on Code Institute Boutique Ado project.

![Site Preview](https://bjjhubproject.s3.amazonaws.com/media/RESPONSIVE.png)


Live app link can be found [here](https://bjj-hub-project.herokuapp.com/)

# Target Audience

This site is targeted to the Brazilian Jiu Jitsu community. People who want to wear well known, stylish and durable gear when training and competing in BJJ and Grappling.
The site is also to MMA fans and BJJ newcomers who need the right gear when starting out in their BJJ journey.

# Marketing

The user can keep up with deals and sales by signing up to the site mailing list and by following the [Facebook page](https://www.facebook.com/BJJ-Hub-107733918670528). The facebook will also post BJJ news, videos and competition info.

![Site Preview](https://bjjhubproject.s3.amazonaws.com/media/BJJ_hub_facebook.jpg)

# Search Engine Optimisation

Generated sitemap.xml and robots.txt files to improve the quality and quantity of website traffic. I have come up with a selection of keywords which would be important to the customers and added them in the meta.

![Keywords](https://bjjhubproject.s3.amazonaws.com/media/SEO1+google+search.jpg)

![SEO](https://bjjhubproject.s3.amazonaws.com/media/SEO1+google+search1.jpg)



# User Experience

***


## User Stories
1 User
### 1.1 As a User I can View product details so that identify price, description and image
### 1.2 As a user I can Easily view the total of my purchases at any time so that keep track of spending
### 1.3 As a User I can register for an account so that view my profile details and edit my acc
### 1.4 As a User I can easily log in and out so that access my account info
### 1.5 As a user I can recover my password so that recover access to my account
### 1.6 As a user I can receive an email confirmation after registering so that verify my acc…
   

2 Shopper
### 2.1 As a shopper I can sort the lsit of available products so that easily id the best rated product
### 2.2 As a shopper I can sort a specific category of products so that find the best priced products
### 2.3 As a shopper I can sort multiple categories of products simultaneously so that find th best suited product across categories such as "fight wear
### 2.4 As a shopper I can sort multiple categories of products simultaneously ** so that find th best suited product across categories such as "fight wear"
### 2.5 As a shopper I can easily see what ive search for and the number of results so that I can decide what product is available
### 2.6 As a Shopper I can Easily select a size and quantity of product so that Ensuring I don't select the wrong size product
### 2.7 As a shopper I can view items inmy bag to be purchased so that identify the cost of my purchase and all the items i will receive
### 2.8 As a Shopper* I can Adjust the quantity of individual items in my bag so that make changes to my bag
### 2.9 As a shopper* I can Easily enter my payment information so that I can check out quickly
### 2.10 As a shopper I can feel my shopping details are secure so that be confident in providing my info
### 2.11 As a Shopper I can view an order confirmation after checkout so that verify i haven't made any mistakes
### 2.12 As a Shopper I can Receive email confirmation after checking out so that I can keep the confirmation of what ive purchased.
### 2.13 As a shopper I can edit and delete my reviews so that update my review or remove it
### 2.14 As a shopper I can leave site feedback so that received benefit

 3 Storeowner
### 3.1 As a Store owner I can Add a product so that Add new items to my store
### 3.2 As a store owner I can edit a product so that change product prices, descriptions etc
### 3.3 As a store owner I can Delete a product so that remove items that are no longer for sale
### 3.4 As a Store owner I can read user feedback so that make positive changes to the site

## 1. Strategy

 - ### Project Goal
 Create a site that allows users to get support and motivation to quit Caffeine through the site community and Blog Posts.
 Creat a site that allows users to browse and shop for BJJ apparel.

## 2. Scope
- Simple, functional E-commerce site
- explicit content
- Site is easily Navigated
- Appealing on Mobile devices.

# Functional Scope

***


### BJJ Hub Diagram Entity Relationship

![DER](https://bjjhubproject.s3.amazonaws.com/media/flowchart1.jpg)

### Agile Methodology

All development and functioanlity of this project were managed using [Github](https://github.com/bobbydeane/bjj_hub/issues/26).

## 3. Structure

- The site has a simple layout to ensure intuitive navigation.
- Forms are straightfoward an easy to understand
- Edit, update and delete forms are easy to use
- The bag has recognisable UX friendly functionality and layout (Bag taken from boutique ado project)
- The site uses all auth django user sign ups, log in, log outs to deliver tried and tested UX formats and design.



## 4. Surface

The site follows the Code Institute Boutique Ado site style and layout. The Products and Product details pages kept the Boutique style and used similar bootstrap.

# Existing Features

***

Product select dropdowns on the home landing page that are clear.
Bag and user account log for easy access to other aspects of the site.
The Logged in User can view their profile and update their account details and also leave feedback.
The store owner has access to front end product admin and user feedback display.

![Home](https://bjjhubproject.s3.amazonaws.com/media/homepage.jpg)

The Home page shows a striking backround image and contains a link to the products page.

![Products](https://bjjhubproject.s3.amazonaws.com/media/products.jpg)

User can view all store products and filter via category and other metrics like price,

![Product Detail](https://bjjhubproject.s3.amazonaws.com/media/products_detail.jpg)

The Product Detail page shows the product image and key info like price, description and sizes. The user can add items to their basket from this page

![Bag Preview](https://bjjhubproject.s3.amazonaws.com/media/bag_preview.jpg)

Once an item is added to the bag, the bag contents are shows in the top right of the screen. Like the Boutique Ado store.


![Bag](https://bjjhubproject.s3.amazonaws.com/media/bag.jpg)

The Bag shows the bag contents summary and allows for the user to Update or delete the bag contents.


# Future Features
***
I would like to 
    1. Allow users to reply to reivews.
    2. Add a link to BJJ competition sites.
    3. Add product ratings.
    4. Add video content area to site.
    5. Monthly sub to receive BBJ video tutorials

# Languages Used
***
Python 3.0
HTML
CSS
JS
Django Frameworks


# Frameworks, Libraries & Programmes Used
***
- GitHub: GitHub is used to store the project's code after being pushed from Git.
- Django: Framework used to add structure to the platform.
- Gitpod: was used as a CLI/Code editor.
- Lucidchart: used to create Database schema diagram and flow chart diagram.
- Font Awesome: Used to add icons to the Blog posts.
- google fonts: Used for fonts throughout the site.
- PostgresSQL
- Markdown
- Amazon AWS: used ot host static and media files

# Testing and Code validation
***

## Automated Tests
***
Automated tests were carried out using Djangos testing functionality.
The tests looked at the Python files in the App to validate the code. The Coverage repost can be found int he htmlcov folder in the app.
![Tests](https://bjjhubproject.s3.amazonaws.com/media/checkout_coverage.jpg)

Other Functionality tests  were carried out by the User:
    -test that forms display as expected
    -form submission reacts with Models as expected
    - Test that unathorised user cannot edit/delete a post.
    
Html Tests using - https://validator.w3.org/nu/
CSS testing - https://jigsaw.w3.org/css-validator/
Python Testing - http://www.pep8online.com/

# Credits
***

## Media
***
 - All Images were found on Google images. Produst images taken from Scramble Ireland store site.

## Work based on other Code
***
[Boutique Ado](https://github.com/bobbydeane/Boutique-Ado) was the inspiration for the site. The layout, CSS, bootstrap and general functionality of BJJ Hud relied heavily on the excellent Boutique Ado created by Code Institute.

[Codemy](https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw) was used as a guide to develop CRUD functionality for Blog Posts
Stack Overflow was valuable in troubleshoiting many issues.

[Bootstrap Templates](https://getbootstrap.com/docs/4.0/examples/blog/) and documentation was used for the HTML and styling of the majority of the site.

[Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used for many of the forms on the site.

[Summernote](https://github.com/summernote/django-summernote) was used to style the admin site and forms 

## Acknowledgements
***

- Codemy for getting me through some tricky code implementation
- Code Institute Slack Community for the support and time
- Stackoverflow for the lifeline when i'm struggling
- Code Institute tutor support for the help and patience

I would also like to thank:
- Code Institute for this opporuntity.
- Caragh & Ban.
