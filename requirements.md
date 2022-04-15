## Functional Requirements

1. Login (Hetal)
2. Logout (Jonathan)
3. Create new account (Michael)
4. Delete account (William)
5. User ratings (Hetal)
6. User profile (Jonathan)
7. Splash page (Michael)
8. Add pictures for items (William)
9. Find item (Hetal)
10. Add to cart (Jonathan)
11. See all items available from all of the sellers (Michael)
12. Filter by categories (William)

## Non-functional Requirements

1. Sellers should be notified of a new job
2. Webpage should load quickly to show that it is not unresponsive
3. Users should not be able to see others' transactions
4. Users can set links to other sites on their profile

## Use Cases

1. Visit Splash Page
- **Pre-condition:** The site exists

- **Trigger:** A user visits the site

- **Primary Sequence:**
  
  1. A user visits the site
  2. The site loads home bar
  3. The site loads popular services available to buy

- **Primary Postconditions:** The user can see the splash page 

2. Filter by Categories
- **Pre-condition:** Multiple services exist

- **Trigger:** A user decides to serach services by category

- **Primary Sequence:**

  1. User clicks on categories
  2. Site shows available filters
  3. User clicks on category to fileter out or search for
  4. Site shows services with all currently selected categories

- **Primary Postconditions:** Services only with desired categories are shown   

- **Alternative Sequence:**

 1. No services match the selected filters
  - Site shows an error message and prompts user to go back to filters to change choices

3. User profile
- **Pre-condition:** <can be a list or short description> user must have a registered account.

- **Trigger:** <can be a list or short description> website user clicks on the username or userprofile icon. 

- **Primary Sequence:**
  
  1. Website user views the services that are provided
  2. Website user clicks on the service they like
  3. Website user clicks on the username of the user for more information on them
  4. Website shows a page with information on the user
   

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Website user uses the search bar to search username
  2. Website user clicks on the username
  3. Website shows a page with information on the user

4. Use Case Name (Add to cart)
	**Pre-condition:** 
	   Must have an account
	   Customer must be logged in
	**Trigger:**
	   Customer selects add to cart option   
        **Primary Sequence:**
		1. Customer views services that can be purchased
		2. Customer selects and views the service 
		3. After selecting, system provides avaiability and cost of service
		4. Customer can select to add to cart 
		5. System stores the customers selection in cart
	**Primary Postconditions:**
		1. The customer's cart holds the service(s) that they have selected
	**Alternate Sequence**
		1. The customer leaves the webpage and the customers cart will be saved to their profile
	 
5. Find item
        **Pre-condition:**
          Customer must type in keywords matching to service
        **Trigger:**
          Customer uses a search bar
        **Primary Sequence:**
                1. Customer clicks on the search bar
                2. Customer types in keywords that match (similar words)
                3. Page displays items
        **Primary Postconditions:**
                1. Page shows page with similar service
        **Alternate Sequence:**
                1. Page shows other services closely related
