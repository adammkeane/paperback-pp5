# PaperBack - "We're bring paper back."

PaperBack is an online book store that specialises in physical books. The target audience for the website would be people who like to read and who prefer reading physical books. The aim of the site is to provide users with an easy and intuitive way to browse and buy books. Additional features, such a contact forms and profiles, can help make this experience more enjoyable.

[Click here to view website.](https://paperback-pp5-4d817902330a.herokuapp.com/)

![Mockup](docs/mockup.PNG)

# Components / Features / Pages

## 1 - Home Page

``USER STORY: Home Page``

![Home Page](docs/home.JPG) <br>

**Contains**:

- Intro section - welcomes user to the site, tells them what the site does, and links to our selection of books.

- Latest additions - displays the 3 most recent additions to the shop.

## 2 - Nav Bar

``USER STORY: Nav Bar/Bootstrap Install``

Repsonsively houses easy-to-reach, useful links for the user.

- Desktop <br>
  ![Nav Bar Desktop](docs/navbar.JPG)

- Mobile (closed) <br>
  ![Nav Bar Mobile (closed)](docs/navbar2.JPG)

- Mobile (open) <br>
  ![Nav Bar Mobile (open)](docs/navbar3.JPG)

- Mobile (open & account dropdown) <br>
  ![Nav Bar Mobile (open & account dropdown)](docs/navbar4.JPG)

**Contains**:

- Search bar - allows user to easily search letters/words found in the book titles, book descriptions, and author names.

- Account dropdown - gives user access to sign in, sign out, registration and profile pages.

- Shopping bag link - keeps track of user's shopping bag total for the current session, and acts as link to get to the shopping bag page.

- Banner - allows users to quickly navigate to home, books, and contact form pages.

## 3 - Footer

``USER STORY: Footer / Mailchimp Newsletter``

![Footer](docs/footer.JPG) <br>

**Contains**:

- Social media links - Facebook links to a facebook page created for the ecommerce site. Youtube just links to youtube homepage for now. Both links contain the noopener and nofollow rel attributes.

- Mailchimp newsletter sign up form - user can enter email to be added a newsletter mailing list.

## 4 - Books Page

``USER STORY: View Books``

![Books Page](docs/books.JPG) <br>

**Contains**:

- Book count & sorting - tells user the total number of books on display, and allows user to sort the books in terms of name, price and average review rating (both ascending and descending)

- Book info - basic book info is given, including the cover image, title, price and review info. Both the cover image and title act as links to take you to the book detail page.

## 5 - Book Detail Page

``USER STORY: View Books``
``USER STORY: View Book Reviews``

- Detail 1 <br>
  ![Book Detail 1](docs/book-detail1.JPG)

- Detail 2 <br>
  ![Detail 2](docs/book-detail2.JPG)

- Reviews <br>
  ![Reviews](docs/reviews1.JPG)

**Contains**:

- Book detail - includes cover image, title, author, review score/number of reviews in parenthesis and price. The author is a link the author page.

- Add to bag - user can select the option (if there is one), select the quantity they want, and add their deserved option combo quantity to shopping bag.

- Reviews - user can see how other users have reviewed the book in more detail. They can also add a review of their own if they are signed in.

## 6 - Add Review Page

``USER STORY: Create Book Reviews``

![Add Review Page](docs/reviews2.JPG) <br>

**Contains**:

- Add review form - only required field is the rating field, if user is short on words/time. Once submitted, user is taken back to book detail page, where they can see their review added to the review section.

## 7 - Shopping Bag Page

``USER STORY: Shopping Bag``

- Desktop <br>
  ![Shopping Bag Page Desktop](docs/bag1.JPG)

- Mobile <br>
  ![Shopping Bag Page Desktop](docs/bag2.JPG)

**Contains**:

- Bag Summary - user can double check book options, quantity, and price before goign to checkout.

- Update & remove item - allows user to change the quanity of a book or remove a book from the bag entirely.

- Back to top arrow - mobile display has a handy arrow to allow user to quickly jump back to top of the page.

## 8 - Checkout Page

``USER STORY: Checkout Page / Stripe``

![Checkout Page](docs/checkout.JPG) 

**Contains**:

- checkout form - user can enter in their shipping and contact details.

- stripe card element - user can process their payment through a trustworthy company.

- save delivery info checkbox - allows signed in user to save their delivery info to their profile, to speed up future purchases.

- another order and price summary - for user clarity and peace of mind.

## 9 - Checkout Success / Order Summary Page

``USER STORY: Checkout Page / Stripe``

![Checkout Success](docs/order-confirmation.JPG) <br>

**Contains**:

- Order summary - user can see all relevant info regarding their order. This page can also be revisted through the user's profile order history section (if the user has registered for an account). It also lets user know a confirmation should be in their email inbox.

## 10 - Add Book Page (superuser)

``USER STORY: Add Book``

![Add Book Page](docs/add-book.JPG) <br>

**Contains**:

- Add book form - contains inputs for name, description, if the book has options, price, image url, and image. Only name, description and price fields are mandatory. Once submitted, user is taken to book detail page where they can view the book they just added to the store.

## 11 - Edit / Delete Book (superuser)

``USER STORY: Edit Books``
``USER STORY: Delete Books``

![Edit / Delete Book Page](docs/edit-delete-books.JPG) <br>

**Contains**:

- Edit book button / form - button visible under book on books page, book detail page and author page. User is taken to an edit book form (identical to add book form styling). User can change book details. Once submitted, user is taken to book detail page where they can view the updated details.

- Delete book button - visible in same places as edit button. Once pressed, book is deleted and user is taken to the books page, where deleted book will no longer be visible.


## 12 - Contact Page

``USER STORY: Contact Form``

![Contact Page](docs/contact.JPG) <br>

**Contains**:

- Contact form - allows users to send a message to the site owner, if they have any feedback, questions, requests etc.

## 13 - Author Page 

``USER STORY: View Author``

Reached through link on the book detail page (author's name is the link).

![Author Page](docs/author.JPG) <br>

**Contains**:

- Bio - a brief description of the author's career/life.

- Books - a display of which books the author currently has in site's store.

## 14 - Profile Page 

``USER STORY: Profile App``

![Profile Page](docs/profile.JPG) <br>

**Contains**:

- Saved delivery info - signed in users can enter delivery info here that will be saved to their profile. The info added here will automatically populate the checkout form any time they want to make a purchase. This info can also be added to the profile page/updated by the user clicking the save delivery info checkbox when making a purchase.

- Order history - a display of previous orders made by the user. The order number is a link to the order confirmation page associated with that order.

## 15 - Allauth / Account Management  Pages

``USER STORY: Allauth/User Autorization Management``

- Sign Up <br>
![Sign In](docs/sign-up.JPG) 

- Sign In <br>
![Sign In](docs/sign-in.JPG) 

- Sign Out <br>
![Sign In](docs/sign-out.JPG) 

**Contains**:

- allauth authentication, registration and account management - gives user high quality experience when working with their account, including email verification and password resets.

## 16 - Custom 404 Page 

``USER STORY: Custom 404 Page``

![404 Page](docs/404.JPG) <br>

**Contains**:

- 404 - let's user know a 404 error has occured and provides them with a button link to get to the book store.

## 17 - Favicon

![favicon](docs/favicon.JPG) <br>

**Contains**:

- Favicon - makes it easier for user to find the tab to the site when they have multiple tabs open. It also adds a touch of professionalism to the site.

# Planning / Agile

## 1 - Project Board & User Stories

[Click here to view GitHub project board.](https://github.com/users/adammkeane/projects/7)

- Project Board <br>
![Project Board](docs/agile1.JPG)

- User Story Example <br>
![User Story Example](docs/agile2.JPG)

The project was broken down in Epics, User stories and Tasks, as can be seen from the prooject board.

## 2 - Wireframes

Rough wireframes were created to find the basic layout for key pages before coding. During coding, the nav bar was made cleaner on mobile by hiding more elements inside the hamburger dropdown, improving the orignal wireframe layout.

- Home Desktop <br>
![Home Desktop](docs/home-wire1.JPG)

- Home Mobile <br>
![Home Mobile](docs/home-wire2.JPG)

- Nav & Footer Desktop <br>
![Nav & Footer Desktop](docs/nav-footer-wire1.JPG)

- Nav & Footer Mobile <br>
![Nav & Footer Mobile](docs/nav-footer-wire2.JPG)

- Books Desktop <br>
![Books Desktop](docs/books-wire1.JPG)

- Home Mobile <br>
![Books Mobile](docs/books-wire2.JPG)

# Marketing / SEO

## 1 - Facebook Page

![Facebook Page 1](docs/fb1.JPG) <br>
![Facebook Page 2](docs/fb2.JPG) <br>

## 2 - Business Model / Marketing Strategy

PaperBack is a B2C (Business to Consumer), which sells physcial products through single online payments.

Being a physical book retailer, we are a little restricted in terms of our marketing and appeal. Amazon sells the same books (as well as digital versions) and very effienctly. However, there does seem to be negative sentiment around Amazon's working conditions and monopoly-esque appereance. Whether these views are well founded or not, it does create a opportunity to market our business as one that cares for its employees and whose very existence and success is useful for increased competition in the online book selling market. We could ask social media influencers to get behind this message and promote our store.

Keywords I came up with for PaperPark (mixture of long and short tail):

- books
- buy books online
- buy books
- buy paperback books
- buy paperback books online
- buy hardback books
- book store online 
- online books store
- physical books
- physical books online
- buy physical books
- novel
- paperback books
- hardback books

The keywords are highly competetive, so SEO may not be the best way for this business to stand out.

As for as content ideas, I thought users would want:
- To see what books are available and have access to some key information, eg the price, book image, review score, title.
- A good layout and aesthics to show this info. Don't want to overwhelm user with info.
- Each book should have a link to a book detail page to get more info if the user is interested.
- A payment system should be trustworthy. Ideally link in with a well know brand like PayPal or Stripe.
- The ability to save delivery info so it doesn't have to be entered for every purchase.


### Database Schema

- ER Diagram used to fully describe the database schema used
![ER Diagram](docs/er-diagram.png)

## Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/) was the framework used to build this website.
- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) was used to create and style the front end of the website.
- [Font Awesome](https://fontawesome.com/) icons have been used for the social media links in the Footer and links in the navbar.
- [Google Fonts](https://fonts.google.com/) have been used to import fonts.
- [Favicon](https://favicon.io/) was used to create the favicon for the website.
- [Techsini](http://techsini.com/multi-mockup/index.php) mockup generator was used to create the mockup image for the README.md file.
- [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) were used to inspect elements of the website and test different styles.
- [GitHub](https://github.com/) has been used to store the code, images, and other contents of the website.
- [AWS](https://aws.amazon.com/) was used to store static and media files in deployed stage.
- [Stripe](https://stripe.com/gb) was used to set up the payment system for the shop.
- [Heroku](https://dashboard.heroku.com/apps) was used to deploy the game to the web.
- [Git](https://git-scm.com/) was used to track changes made to the project and to commit and push code to the repository.
- [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org) was used to test the website's accessibility.

# Testing

## 1 - Manual Testing

| Test Case # | Description                                            | Steps                                                                                                                                                                                                                                                                                                                                                                        | Expected                                                                                                                                                                                                                                                                                                  | Actual                                                                                    | Pass/Fail |
| ----------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------- |
| 1           | Checkout form validation (including Stripe validation) | 1\. Incorrectly fill in checkout form and try to submit the form. <br>2\. Correctly fill in form and submit.                                                                                                                                                                                                                                                                 | 1. Form doesn't allow submission.<br>2\. Feedback is given to user to let them know what they need to change.<br>3\. When form is filled in correctly, the form successfully submits and user is taken to the chekout success page.                                                                       | As expected                                                                               | Pass      |
| 2           | Mailchimp form validation                              | 1\. Incorrectly fill in email field and try to submit the form. <br>2\. Correctly fill in email and submit.                                                                                                                                                                                                                                                                  | 1. Form doesn't allow submission.<br>2\. Feedback is given to user to let them know what they need to change.<br>3\. When form is filled in correctly, the form successfully submits and user is shown a success message.                                                                                 | As expected                                                                               | Pass      |
| 3           | Add to bag form validation (book detail page)          | 1\. Incorrectly fill in quantity field (less than 1, or greater than 99) and try to submit the form. <br>2\. Correctly fill in quantity and submit.                                                                                                                                                                                                                          | 1. Form doesn't allow submission.<br>2\. Feedback is given to user to let them know what they need to change.<br>3\. When form is filled in correctly, the form successfully submits and user is shown a success message.                                                                                 | As expected                                                                               | Pass      |
| 4           | Contact form validation                                | Incorrectly fill in contact form and try to submit the form. <br>2\. Correctly fill in form and submit.                                                                                                                                                                                                                                                                      | 1. Form doesn't allow submission.<br>2\. Feedback is given to user to let them know what they need to change.<br>3\. When form is filled in correctly, the form successfully submits and user is taken to home page and shown shown a success message.                                                    | As expected                                                                               | Pass      |
| 5           | Review form validation                                 | Incorrectly fill in review form by leaving the rating field blank and try to submit the form. <br>2\. Correctly fill in form and submit.                                                                                                                                                                                                                                     | 1. Form doesn't allow submission.<br>2\. Feedback is given to user to let them know what they need to change.<br>3\. When form is filled in correctly, the form successfully submits user is shown a success message, and review can be seen on the book detail page.                                     | As expected                                                                               | Pass      |
| 6           | Save delivery info checkbox                            | 1\. Sign into an account.<br>2\. Complete a checkout form, take note of the delviery information used, make sure the save delivery info checkbox is checked and submit the form. <br>3\. Repeat step 2 with different delivery info and unchecking the save delivery info checkbox. <br>4\. After order complete, go to the profile page and check the delivery information. | 1\. Delivery information on profile page matches the delviery info used with the first order.                                                                                                                                                                                                             | The delivery info was saving to the profile, whether the save info box was checked or not | Fail      |
| 7           | Profile form validation                                | 1\. Incorrectly fill in profile form form and try to submit the form. <br>2\. Correctly fill in form and submit.                                                                                                                                                                                                                                                             | 1. Form doesn't allow submission.<br>2\. Feedback is given to user to let them know what they need to change.<br>3\. When form is filled in correctly, the form successfully submits and user is shown a success message.                                                                                 | As expected                                                                               | Pass      |
| 8           | Add book form validation                               | 1\. Incorrectly fill in add book form and try to submit the form. <br>2\. Correctly fill in form and submit.                                                                                                                                                                                                                                                                 | 1. Form doesn't allow submission.<br>2\. Feedback is given to user to let them know what they need to change.<br>3\. When form is filled in correctly, the form successfully submits, user is taken to the book detail page, with info matching what what submitted, and user is shown a success message. | As expected                                                                               | Pass      |
| 9           | Edit book form validation                              | 1\. Incorrectly fill in edit book form form and try to submit the form. <br>2\. Correctly fill in form and submit.                                                                                                                                                                                                                                                           | 1. Form doesn't allow submission.<br>2\. Feedback is given to user to let them know what they need to change.<br>3\. When form is filled in correctly, the form successfully submits, user is taken to book detail page, which shows the updated book info, and user is shown a success message.          | As expected                                                                               | Pass      |
| 10          | Delete book button                                     | 1\. Sign in as super user and add 3 books <br>2\. Go to books page and press delete button under 1 of those books. <br>3\. Go to book detail page and press delete button under 1 of those books. <br>4\. Go to author page and press delete button under last of those books.                                                                                               | 1. With each delete press, user is taken to the books page and shown a success message.<br>2\. Deleted book can no longer be found on the books page.                                                                                                                                                     | As expected                                                                               | Pass      |
| 11          | Update bag item validation (bag page)                  | 1\. Add item to shopping bag and go to bag page. <br>2\. Incorrectly fill in quantity field (less than 1, or greater than 99), changing it from its original value, and try to submit the form. <br>3\. Correctly fill in quantity and submit.                                                                                                                               | 1. Form doesn't allow submission.<br>2\. Feedback is given to user to let them know what they need to change.<br>3\. When form is filled in correctly, the form successfully submits, user is shown a success message and the bag quantity matches their form input.                                      | As expected                                                                               | Pass      |
| 12          | Delete bag item button (bag page)                      | 1\. Add item to shopping bag and go to bag page. <br>2\. Press the delete button under the item.                                                                                                                                                                                                                                                                             | 1\. Bag page reloads, user is shown a success message, and bag is updated to reflect the removed item.                                                                                                                                                                                                    | As expected                                                                               | Pass      |
| 13          | Books page sorting                      | 1\. Click the sorting dropdown menu and select each option.                                                                                                                                                                                                                                                                             | 1\. Each option sorts the books as expected                                                                                                                                                                                        | 1\. When sorting by rating, if a book did not have any reviews, that book would appear higher rated than books that did have reviews. 2\. Would have liked for that to be the other way around. All other sorting options worked as exptected                                                                             | Fail      |



## 2 - Automated Testing

All tests were run successfuly.

- All tests result <br>
![AutoTest](docs/test1.JPG)

- Example from the books/tests.py <br>
![AutoTest](docs/test2.JPG)

## 3 - Validator Testing

- HTML - All pages put through [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm-paradise.herokuapp.com%2F) with no errors <br> 
![html valid](docs/html-valid.JPG)

- CSS - All css put through [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator) with no errors <br>
![css valid](docs/css-valid.JPG)

- Python - All python has been written to adhere to the PEP8 guidelines. Some minor problems still exist in the settings.py file.

- Accessibility - Website was made with the help of the [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org) to test the site's accessibility. Some label issues for inputs on the checkout and profiles page could not fixed as I couldn't figure out how to access the individual fields and was short on time. An alt tag was also missing from the current image field of the the edit book page, but couldn't fix for the same reasons as above.

## 4 - Repsonsiveness Testing

All pages were tested to ensure responsiveness on screen sizes from 320px x 634px and upwards on both Firefox and Chrome. Good user experience found on all screen sizes.

# Unfixed bugs

- The save delivery info bug found in manual testing.
- The review sorting bug found in manual testing.

# Deployment

The below steps were followed to deploy this project to Heroku:

1. Go to [Heroku](https://dashboard.heroku.com/apps) and click 'New' to create a new app.
2. After choosing the app name and setting the region, press 'Create app'.
3. Go to 'Resources' to add a database and scroll down to 'Add-ons'. Search for 'Postgres' and choose 'Heroku Postgres' from available options.
4. Go to 'Settings' and navigate to 'Config Vars'. As the Postgres database has been connected, the DATABASE_URL is already there. Add the remaining config vars: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET, USE_AWS (the values for these variables depend on your own personal set up and will not be added here for security reasons).
5. Leave 'Settings' and go to 'Deploy'. Scroll down and set 'Deployment Method' to GitHub. Once GitHub is chosen, find your repository and connect it to Heroku.
6. Scroll down to Manual Deploy, make sure the 'main' branch is selected and click 'Deploy Branch'.
7. The deployed app can be found [here](https://paperback-pp5-4d817902330a.herokuapp.com/).

# Credits

## 1 - Content & Media

The information about each book and author, and images related to the books, have been taken from:

- [Amazon](https://www.amazon.co.uk/)
- [Britannica](https://www.britannica.com//)
- [Wikipedia](https://www.wikipedia.org/)

## 2 - Acknowledgements

Daisy McGirr(mentor) - for her guidance and great advice throughout this project.<br>
[Olga's Project](https://github.com/OlgaJ1989/bookworm-paradise) - For readme inspiration and help with the contact app code.
