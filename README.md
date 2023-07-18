# PaperBack

PaperBack is an online book store for those who enjoy reading physical books. 

The website can be accessed [here](https://paperback-pp5-4d817902330a.herokuapp.com/).

![Mockup](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/mockup.PNG)

## Features

### Existing features

* Navigation Bar 
    * Includes direct links to all parts of the website, allowing the user to easily navigate between them.
        1. All users can see the folowing links in the navbar: Account and Cart (in top part of the navbar), Home, All Books, Genres, Newsletter and Contact Us (in bottom part of the navbar).

           ![Navigation](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/navbar.PNG) 
        
        2. All users can see the search bar, allowing them to search for any book.

           ![Search-bar](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/search-bar.PNG) 

        3. When logged OUT, the user can see the following links when clicking on the Account dropdown: Register, Login.

           ![Navigation Logged Out](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/logged-out.PNG)

        4. When logged IN, the user can see the following links when clicking on the Account dropdown: Management, Profile, Logout.

           ![Navigation Logged In](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/logged-in.PNG)

        5. On smaller devices the menu links scale down to a toggler, allowing for a cleaner design.

           ![Navigation Responsive](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/mobile-nav-shots.jpg)
      
* Landing page image with overlaying jumbotron
    * The index.html page (Home) includes a background picture of books, with a button leading directly toe the shop where users can view all available books. 
    
      ![Jumbotron](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/landing-page.PNG)

* Welcome to Bookworm Paradise section
    * A small section welcoming users to the store. 

      ![Welcome](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/welcome.PNG)

* Newsletter section
    * A section containing the newsletter subscription form, where users can enter their email which will then be saved in MailChimp database. In a real life scenarion, this could then be used to create a mailing list to send out newsletters.  

      ![Newsletter](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/newsletter.PNG)

* Interactive footer across all pages
    * It consists of clickable icons linking the user to a choice of social media platforms (Facebook, Twitter, Instagram). All links open in new tabs so the user does not have to leave the Bookworm Paradise page.

      ![Footer](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/footer.PNG)

* All Books page
    * This page list all books available to purchase on the site, with clickable book ocvers that lead to the chosen book's detail page when clicked. It states how many books are available in the shop in total and has a 'Sort by...' select box where users can sort books by title, author, genre, price and rating.  

      ![All Books](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/all-books.PNG) 

    * The books on this page can also be sorted into Genres by clicking on the Genres link in the navbar. Once a genre is chosen, the page will display only the books in the chosen genre and update their number. 

* Book detail page
    * Once a user selects a book and clicks on its cover, they will be taken to the book's detail page containing all the information about it, such as price, description, number of pages, etc. If a user is an admin / shop owner, they will also be able to edit or delete a book on this page, using the 'Edit' and 'Delete' buttons located above the price. 
    
      ![Book details](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/book-detail.PNG) 

* Book detail page - review section
    * At the bottom of each book's detail page, users can find a section where they can read existing reviews or add their own. All users can view existing reviews but only logged in users can add them. When it comes to editing or deleting an existing review, only the review's author can do this. A user will see the an 'Edit' and 'Delete' buttons under a review only if they are the review's author.
    
      ![Reviews](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/reviews.JPG) 

* Contact page
    * The contact.html page consists of a contact form through which a user can ask the shop owner a question. When submitted, the form creates a message instance in the database so the owner can access it and contact the user. 
    
      ![Contact](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/contact-form.PNG)

* Cart page
    * When a user chooses a book and clicks on the 'Cart' link, they will be redirected to the Cart page where they will be able to see the info for the product they've chosen.  
    
      ![Cart](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/cart.PNG)

* Checkout page
    * If they decide they are happy with their choice, they can then click on the 'Checkout' button which will in turn take them to the page where they can fill in their personal info and card details to pay for the book.
    
      ![Checkout](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/checkout.PNG)

* Checkout success page
    * Once the user places their order, they will be greeted with a checkout success page, showing them their order details. 
        
      ![Success](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/thank-you.PNG)

* Sign Up page
    * Allows the user to register for an account so they can save their details and order history.
        
      ![Sign Up](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/sign-up.PNG)

* Sign In / Login page
    * Allows the user to log in to an existing account in order to manage reviews and view their order history.
        
      ![Sign In](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/login.PNG)

* Sign out / Logout confirmation page
    * A template that renders after the user chooses to log out, giving them a chance to confirm in case they clicked the link by mistake.       
    
      ![Sign Out](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/logout.PNG)

*  Custom 404 page
    * A custom 404 page has been made to make it easy for the user to come back to home page after they tried to move to a non-existent page.

      ![404](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/404.PNG)

* A favicon
    * A favicon has been added to make it easier for users to find the Taste of Poland page if multiple tabs are open. 
    
      ![Favicon](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/favicon.PNG)

* A Facebook business page 
    * A business page has been created for marketing reasons, to further advertise the shop, post news and communicate with customers.  favicon has been added to make it easier for users to find the Taste of Poland page if multiple tabs are open.
    * The page can be accessed [here](https://www.facebook.com/Bookworm-Paradise-106344228834492/?notif_id=1658868269617980&notif_t=page_invite_accept&ref=notif).  
    
      ![Facebook 1](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/fb1.JPG)

      ![Facebook 2](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/fb2.JPG)


## User Experience Design

Bookworm Paradise is a responsive website of a non-existent online bookshop. 

The aim of the website is: 
- to give users an opportunity to purchase a book without an unnecessary hassle and going through complicated processes;
- to give users the possibility of browsing the available books by genres so that they can easily find what they are interested in;
- to give users the possibility of registering for an account in order to be able to save their delivery details and order history;
- to give users the possibility of registering for an account in order to be able to leave a book review (and edit or delete it if necessary);
- to give the site owners / authorised staff the possibility of viewing the orders and reviews users made so they can be modified or deleted if needed;
- to give users the possibility of accessing the website on any device;
- to give users the means necessary for them to be able to contact the shop owner.

### User Stories

User stories for this project can be viewed on [Trello](https://trello.com/b/S14lxcQ0/bookworms-paradise).

![UX Epic](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/ux-epic.PNG)

1. As a user, I want the main purpose of the website to be clear so that upon entering I immediately know what it's purpose is.
    * Acceptance Criteria:
        - Bookshop's logo and information displayed on the main page with clear information on what the site's purpose is.
    * Implementation:
        - The Home page will contain the main website title of "Bookworm's Paradise", situated in the navbar section.
        - It will also contain information about the site's general purpose and about the shop itself, to make what the site is intended for immediately clear to the user.

2. As a user, I want to be able to easily navigate between the different parts / pages of the website so that I can find content quickly and easily on any device.
    * Acceptance Criteria:
        - Navigation menu to allow users to navigate the site with ease.
        - Collapsible mobile menu to allow users to navigate the site from a mobile device. 
        - All navigation links should navigate to the correct pages.
        - The 'Profile' dropdown option should only appear for signed in users.
    * Implementation:
        - A navigation menu will be created to allow users to navigate through the site. It will be collapsible on a mobile device, and positioned at the top left of the logo element.
        - When a user is not logged in, the 'Account' dropdown will only show the 'Register' and 'Login' links. 
        - When a user is logged in the 'Account' dropdown will show 'Profile' and 'Logout' options. 

3. As a user, I want to be able to easily find links to any social media channels that the bookshop might be running.
    * Acceptance Criteria:
        - Social media links included to allow users to navigate to linked accounts with ease.
        - All links should navigate to the correct pages.
    * Implementation:
        - Social media links in the form of FontAwesome icons will be added to the footer and appear on each page.

4. As a user, I want to search for a book using its title, author or description, so I can find a specific book I'm interested in.
    * Acceptance Criteria:
        - A search bar that takes different criteria and keywords.
    * Implementation:
        - A search bar will be added to the navbar, allowing the users to search a book by its author, title, or keywords present in its synopsis.

5. As a user, I want to see all results of my search so I can see straight away whether the book I'm looking for is available on the site.
    * Acceptance Criteria:
        - A page displaying search results.
    * Implementation:
        - A page displaying search results will be created, allowing the user to see every book that the search produced.

6. As a user, I want to see all results of my search so I can see straight away whether the book I'm looking for is available on the site.
    * Acceptance Criteria:
        - A page displaying search results.
    * Implementation:
        - A page displaying search results will be created, allowing the user to see every book that the search produced.

7. As a user, I want to be able to contact the shop in case I have any questions regarding the products or an order I made, or if I encounter any issues with the website.
    * Acceptance Criteria:
        - A 'Contact' page which includes a form allowing users to send the shop owner a message.
    * Implementation:
        - A 'Contact' page will be created and it will include a form through which a user can send a message to the shop owner. It will consist of an obligatory email field so the shop owner is able to reply to the query.

8. As a user, I want to be able to sort the books by price, rating, author, etc., so that I can find the best option for myself.
    * Acceptance Criteria:
        - Sorting functionality to be added to the 'All Books' page, allowing users to sort the books by title, author, price, rating and genre.
    * Implementation:
        - A select input will be added to the aforementioned page, allowing users to modify the order in which the books appear.

9. As a user, I want to be able to view all available books on one page so that I can see everything that the shop has on offer in one place.
    * Acceptance Criteria:
        - A page with all the books listed, so that users can see everything that is being offered so they don't have to settle on a genre.
    * Implementation:
        - The 'All Books' page will consist of a list of all books that are available in the shop so users will be able to see all of them in one place.

10. As a user, I want to be able to view detailed information about the product (book), including photos.
    * Acceptance Criteria:
        - A book detail page for each book that will include all the information about the book, such as its title, author, publisher, the number of pages, the type of binding, etc.
    * Implementation:
        - A detail page will be created for each book, containing all the aforementioned information in a clear and concise manner.

11. As a user, I want to see the reviews other people left, so that I can decide whether it's a good idea to purchase a book or not.
    * Acceptance criteria:
        - A section displaying existing reviews will be added to each book's detail page.
    * Implementation:
        - A section displaying existing reviews will be added to each book's detail page for everyone to see and read, even the users that did not log in.

12. As a user, I want to add reviews to the books I've purchased and/or read, so I can share my opinion on the book or shopping experience.
    * Acceptance criteria:
        - A custom review form allowing logged in users to add a review to each book.
    * Implementation:
        - A review form will be added to the bottom of each book's detail page, allowing logged in users to leave a review of the book.

13. As a user, I want to be able to edit reviews that I added, so that I can add missing information or edit the existing one.
    * Acceptance criteria:
        - An edit button will be added to each review.
    * Implementation:
        - An edit button will be added to each review but will only be visible to each review's logged in author, allowing them to modify it and save changes.

14. As a user, I want to be able to delete reviews that I added, if I change my mind and do not want to share them anymore.
    * Acceptance criteria:
        - A delete button will be added to each review.
    * Implementation:
        - A delete button will be added to each review but will only be visible to each review's logged in author, allowing them to delete the review.

![SE Epic](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/se-epic.PNG)

15. As a user, I want to be able to easily view the total for the books in my cart (without navigating to it) so that I can avoid spending too much.
    * Acceptance criteria:
        - Cart icon displaying the cumulative price of selected books visible on each store page.
    * Implementation:
        - An amount field will be added under the cart icon and it will update every time an item is added to the cart, showing accurate amount to be paid on checkout

16. As I user, I want to easily select the quantity of a chosen book when purchasing it, so I can avoid choosing the wrong amount or book.
    * Acceptance Criteria:
        - A quantity selection box to be included on each book's detail page.
    * Implementation:
        - A quantity selection box will be added to the book detail page for each book, where users will be able to input the quantity they would like to purchase.

17. As a user, I want to view the contents of my cart, so that I can see which books I've chosen and identify the total cost of my order.
    * Acceptance Criteria:
        - A custom cart page, showing the chosen items, their quantity and cost.
    * Implementation:
        - A cart page will be created, showcasing the items that the user has chosen and their price, as well as the delivery costs and the grand total for the order.

18. As I user, I want to easily change the quantity of a chosen book in the cart so that I can make changes to my order before checking out.
    * Acceptance Criteria:
        - A quantity selection box to be included next to the book already in the cart.
        - Edit and delete functionality included.
    * Implementation:
        - A quantity selection box will be included next to the book already in the cart, with buttons allowing users to edit the quantity or delete the book from cart completely.

19. As a user, I want to be able to enter my payment information easily, so that I can check out promptly and hassle-free.
    * Acceptance criteria:
        - Form allowing the user to enter their card details in a quick and efficient manner.
    * Implementation:
        - The checkout page will consist of a Stripe form input, allowing the user to enter their card details and pay for their order.

20. As a user, I want to see an order confirmation after checking out, so I can see that all the details are correct.
    * Acceptance criteria:
        - A page informing the user that they checked out successfully and displaying their order information.
    * Implementation:
        - A page that is generated after an order has been placed will be added, displaying the order and delivery information to the user.

21. As a user, I want to see my past orders so that I can keep records of my purchases.
    * Acceptance criteria:
        - A page displaying the user's past orders in the profile section.
    * Implementation:
        - An order history section will be created and added to the user's profile page.

![UP Epic](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/up-epic.PNG)

22. As a user, I want to be able to register for an account so I can view my profile.
    * Acceptance Criteria:
        - A custom registration form / page allowing the users to register for an account.
    * Implementation:
        - A reservation form / page will be created using the allauth library, allowing users to register for an account.

23. As a user, I want to be able to log into my account to be able to access my account information and view my order history.
    * Acceptance Criteria:
        - A login form allowing the users to login to the website.
    * Implementation:
        - A login form will be created using the allauth library, allowing users to login to an existing account.

24. As a user, I want to be able to reset my password if I forget it, so that I can access my account.
    * Acceptance Criteria:
        - A custom password reset form allowing the users to input their email so they can be sent a password reset link.
    * Implementation:
        - A login form will be created using the allauth library, allowing users to reset their password.

25. As a user, I want to have my own profile so I can save and view my personal information and order details.
    * Acceptance Criteria:
        - A personalised profile page for each authorised user, allowing them to view and manage their info.
    * Implementation:
        - A profile page will be created, containing user's personal details, such as delivery address, and their order history.

![AP Epic](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/ap-epic.PNG)

26. As a site admin, I want to be able to add, edit and delete books from my shop.
    * Acceptance Criteria:
        - An 'Admin' page displaying all books currently in stock, where the shop's owner or authorised staff are able to view, modify and delete them.
    * Implementation:
        - A Django built-in admin panel will be utilised to create a page where staff authorised as Django 'superusers' can view books in stock, as well modify and them.

27. As a site admin, I want to be able to view, edit and delete users' orders.
    * Acceptance Criteria:
        - An 'Admin' page displaying all orders placed by users, where the shop's owner or authorised staff are able to view, modify and delete them.
    * Implementation:
        - A Django built in admin panel will be utilised to create a page where staff authorised as Django 'superusers' can view the existing orders, as well as modify and delete them if necessary.


### Business model

* Bookworm Paradise is based on a B2C (Business to Consumer) as it sells its books directly to the customer.
* As this is the case, it needs to maintain good relationship with its customers in order to build a customer base and thrive.
* A Facebook page has been created as it allows the shop owners to reach a wide range of customers and communicate with them regularly. 


### Entity Relationship Diagram

![ERD](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/erd.PNG)

### Wireframes

* Home

    ![WireframeHome](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/wireframe1.PNG)

* All Books

    ![WireframeBooks](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/wireframe2.PNG)

* Book details

    ![WireframeDetails](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/wireframe3.PNG)

* Contact Us

    ![WireframeContact](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/wireframe4.PNG)


## Technologies

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/) was the framework used to build this website.
* [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) was used to create and style the front end of the website.
* [Font Awesome](https://fontawesome.com/) icons have been used for the social media links in the Footer and links in the navbar.     
* [Google Fonts](https://fonts.google.com/) have been used to import fonts. 
* [Favicon](https://favicon.io/) was used to create the favicon for the website.
* [Techsini](http://techsini.com/multi-mockup/index.php) mockup generator was used to create the mockup image for the README.md file. 
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) were used to inspect elements of the website and test different styles. 
* [GitHub](https://github.com/) has been used to store the code, images, and other contents of the website.
* [AWS](https://aws.amazon.com/) was used to store static and media files in deployed stage. 
* [Stripe](https://stripe.com/gb) was used to set up the payment system for the shop.
* [Heroku](https://dashboard.heroku.com/apps) was used to deploy the game to the web.
* [Git](https://git-scm.com/) was used to track changes made to the project and to commit and push code to the repository.
* [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org) was used to test the website's accessibility.
* [Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools) was used to run an audit of the website. 


## Testing

### Manual testing
| Test Case # | Description                                                                                                                                                               | Steps                                                                                                                                                                                                                                            | Expected                                                                                                                                                                                                                                                                                         | Actual      | Pass/Fail |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | --------- |
| 1           | Checkout Form Validation                                                                                                                 | 1\. Incorrectly fill in checkout form and try to submit the form. <br>2\. Correctly fill in form and submit.                                                                                                                                                                                       | 1. Form doesn't allow submission.<br>2\. Feedback is given to user to let them know what they need to change.<br>3\. When form is filled in correctly, the form successfully submits and user is taken to the chekout success page.                                                   | As expected | Pass      |
| 2           | Test inccorrect answer feedback functioning correctly                                                                                                                     | 1\. Start game.<br>2\. Answer question incorrectly.                                                                                                                                                                                              | 1\. Red background color added to input field and text feedback.<br>2\. Text feedback appears saying that we were incorrect.<br>3\. Input field, dropdown arrow and check answer button disabled.<br>4\. Focus taken away from the input field.                                                  | As expected | Pass      |
| 3           | Test invalid answer feedback functioning correctly                                                                                                                        | 1\. Start game.<br>2\. Answer question invalidly (not exactly matching a dropdown list option).                                                                                                                                                  | 1.Yellow background color added to input field and text feedback.<br>2\. Text feedback appears saying that we had invalid guess.<br>3\. Check answer button disabled.<br>4\. All other fields/buttons remained active.<br>5\. Input field emptied.<br>6\. Focus taken away from the input field. | As expected | Pass      |
| 4           | Test is all countries appeared in the quiz and not double ups.                                                                                                            | 1\. Start game.<br>2\. Answer every question.<br>3\. console.log the country object half way through and before last question of the quiz.                                                                                                       | 1\. Each country that we've already answered is being removed from the countries object.<br>2\. By last question, the console.log should should just one option for the last renaming country.                                                                                                   | As expected | Pass      |
| 5           | Test score and question number were being updated correctly.                                                                                                              | 1\. Start game.<br>2\. Play full quiz,during which I answering 3 random questions correctly.                                                                                                                                                     | 1\. My score at the end should be 3.<br>2\. The question number at the end should be 50/50.                                                                                                                                                                                                      | As expected | Pass      |
| 6           | Test Jerusalem didn't appear twice in the dropdown options list, and that the one option was deemed correct for both Israel and Palestine (More details in bugs section). | 1\. Start game.<br>2\. Click dropdown arrow to see all options. If we see only one instance of Jerusalem, move on to step 3.<br>3\. Skip ahead until we see both Israel and Palestine. For both, select the sole Jerusalem option as the answer. | 1\. Jerusalem only appears once in the dropdown list.<br>2\. When its selected as the answer for both Israel and Palestine, we get the correct answer feedback, as mentioned in Test Case #1.                                                                                                    | As expected | Pass      |
| 7           | Test modal functioning correctly on both home page and capitals of Asia quiz page.                                                                                        | 1\. Load home page.<br>2\. Click how to play button. Close modal if it opens.<br>3\. Click on question mark in the nav bar. Close modal if it opens.<br>1\. Start game.<br>2\. Click on question mark in the nav bar. Close modal if it opens.   | 1\. Modal opens when either the how to button or the question mark is clicked on both pages.<br>2\. Modal can be closed by clicking on the gray out background or the X button at the top right of the modal.                                                                                    | As expected | Pass      |
| 8           | Test end of quiz functionality.                                                                                                                                           | 1\. Start game.<br>2\. Click next until you reach the end.<br>3\. Click replay button.                                                                                                                                                           | 1.Pink background color added to input field and text feedback.<br>2\. Input field, dropdown arrow, check answer button and next button disabled.<br>3\. Replay button appears. When clicked, it reloads the page and the quiz start again.                                                      | As expected | Pass      |
        
### Automated testing

All tests in tests.py files were run successfuly.

![AutoTest](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/auto-testing.PNG)


### Validator testing

* HTML - when the code was passed through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm-paradise.herokuapp.com%2F) 
    * When I passed my code through the W3C validator, two errors appeared. One of them stated that there was a stray 'label' tag somewhere in the code, and the other stated that there's a missing closing 'div' tag. I have located both of these in the main-nav.html file and corrected them.

    * After correcting the above, I run the validator again and this time no errors were found:

    ![W3C result](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/w3c-validator.PNG)

* CSS - no errors were found when code was passed through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator)

    ![CSS](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/css-validator.PNG)


* JavaScript - when running the code through [JSHint linter](https://jshint.com/) I received the following error message referring to the two 'html' variables: "'template literal syntax' is only available in ES6 (use 'esversion: 6').". I copied /*jshint esversion: 6 */ into the linter window to override this. After I did this, no more errors appeared.

    ![jShint](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/jshint.PNG)


* Python - when running the code through [PEP8 linter](http://pep8online.com/) I received a few 'line too long' errors referring to the automatically generated code in settings.py. As the code was auto-generated and there was not an easy fix to shorten the lines, I have left this error in. There were no errors in any files that have been coded and customised by me.  


* Accessibility - when using the [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org) to test the site's accessibility, I have encountered the following errors and/or warnings:
    * There were missing labels on some form inputs as the inputs had placeholders instead. I have added the labels and used the .visually-hidden class to hide them (I found info [here](https://www.a11yproject.com/posts/how-to-hide-content/#:~:text=visually%2Dhidden%20class%20is%20applied,focus%20indicator%20had%20gone%20to.)) 
    * Aria-labels were missing on some content - I have added all of them.
    * No further errors have been found after I applied the above fixes and passed the site through the validator again.
    
    ![Wave](https://github.com/OlgaJ1989/bookworm-paradise/blob/main/docs/wave.PNG)

### Unfixed bugs

No other bugs found.

## Deployment

The below steps were followed to deploy this project to Heroku:
1. Go to [Heroku](https://dashboard.heroku.com/apps) and click 'New' to create a new app.
2. After choosing the app name and setting the region, press 'Create app'.
3. Go to 'Resources' to add a database and scroll down to 'Add-ons'. Search for 'Postgres' and choose 'Heroku Postgres' from available options.
4. Go to 'Settings' and navigate to 'Config Vars'. As the Postgres database has been connected, the DATABASE_URL is already there. Add the remaining config vars: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET, USE_AWS (the values for these variables depend on your own personal set up and will not be added here for security reasons). 
5. Leave 'Settings' and go to 'Deploy'. Scroll down and set 'Deployment Method' to GitHub. Once GitHub is chosen, find your repository and connect it to Heroku.
6. Scroll down to Manual Deploy, make sure the 'main' branch is selected and click 'Deploy Branch'.
7. The deployed app can be found [here](https://paperback-pp5-4d817902330a.herokuapp.com/).

## Credits

### Content & Media

The information about each book and author, and images related to the books, have been taken from: 
* [Amazon](https://www.amazon.co.uk/)
* [Britannica](https://www.britannica.com//)
* [Wikipedia](https://www.wikipedia.org/)

### Acknowledgements

I'd like to thank my mentor Daisy McGirr for her guidance and great advice throughout this project. 