## Functional Requirements

1. Login
2. Logout
3. Create new account
4. Delete account
5. User ratings
6. User profile
7. Splash page
8. Add pictures for items
9. Find item
10. Add to cart
11. See all items available from all of the sellers
12. Filter by categories

## Non-functional Requirements

1. Sellers should be notified of a new job
2. Webpage should load quickly to show that it is not unresponsive
3. Users should not be able to see others' transactions
4. Users can set links to other sites on their profile

## Use Cases

5. Visit Splash Page
- **Pre-condition:** The site exists

- **Trigger:** A user visits the site

- **Primary Sequence:**
  
  1. A user visits the site
  2. The site loads home bar
  3. The site loads popular services available to buy

- **Primary Postconditions:** The user can see the splash page 

6. Filter by Categories
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

2. Use Case Name (Add to cart)
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
	 
