## Functional Requirements
1. Login (Hetal)
2. Logout (Jonathan)
3. Create new account (Michael)
4. Delete account (Michael)
5. History to see past purchases (Hetal)
6. User profile to edit information (Jonathan)
7. Buy item with fake paying method (William)
8. Add a new listing (William)
9. Find item (Hetal)
10. Add to cart (Michael)
11. See all items available from all of the sellers (Michael)
12. Filter by categories (William)

## Non-functional Requirements
1. Sellers should be notified of a new job
2. Webpage should load quickly to show that it is not unresponsive
3. Users should not be able to see others' transactions
4. Users can set links to other sites on their profile
5. Splash Page

## Use Cases
1. Buy item with fake paying method
        **Pre-condition:**
   - Service/item is in the cart
        -**Trigger:**
   - A user presses a checkout button
        -**Primary Sequence:**
   - 1. A user presses a checkout button
   - 2. The site loads a page showing fields for user to put in fake credit card info (name, card info)
        -**Primary Postconditions:**
   - 1. A user hits submit and page flashes a message of: "service/item has been bought"
        -**Alternative Sequence:**
   - 1. User info doesn't have right information of fake credit card
   - 2. Site shows an error message and page goes back to the payment page

2. Filter by Categories
        -**Pre-condition:**
   - Multiple services/items available for purchase
        -**Trigger:**
   - A user decides to serach services/items by category
        -**Primary Sequence:**
   - 1. User clicks on categories
   - 2. Site shows available filters
   - 3. User clicks on category to filter out or search for
   - 4. Site shows services with all currently selected categories
        -**Primary Postconditions:**
   - 1. Services only with desired categories are shown
        -**Alternative Sequence:**
   - 1. No services match the selected filters
   - 2. Site shows an error message and prompts user to go back to filters to change choices

3. User profile to edit information
        -**Pre-condition:**
   - User must have a registered account.
        -**Trigger:**
   - Website user clicks on the username or userprofile icon.
        -**Primary Sequence:**
   - 1. User clicks on profile tab
   - 2. Website shows user's profile pic (shows default pic), user's name, and user's email.
   - 3. User can edit each field
        -**Alternate Sequence:**
   - 1. User inputs email field with an input that doesn't match a email address
   - 2. Website shows error message to make user to try again with a correct email address.

4. Add to cart
        -**Pre-condition:**
   - Must have an account
   - Customer must be logged in
        -**Trigger:**
   - Customer selects add to cart option
        -**Primary Sequence:**
   - 1. Customer views services that can be purchased
   - 2. Customer selects and views the service
   - 3. After selecting, system provides avaiability and cost of service
   - 4. Customer can select to add to cart
   - 5. System stores the customers selection in cart
        -**Primary Postconditions:**
   - 1. The customer's cart holds the service(s) that they have selected
        -**Alternate Sequence**
   - 1. The customer leaves the webpage and the customers cart will be saved to their profile

5. See all services/items
        -**Pre-condition**
   - Customer must have selected categories option
   - System must have services available for sale
        -**Trigger**
   - Customer selects option to show all items/services in categories section
        -**Primary Sequence**
   - 1. Customer chooses categories tab that holds options to view services offered
   - 2. Customer chooses to view all items from all sellers
   - 3. System provides a gallery of all services provided from all sellers
        -**Primary Postconditions:**
   - 1. All services from all sellers are displayed for customer to see

6. History to see past purchases
        -**Pre-condition:**
   - Customer must have bought a service/item
  	 -**Trigger:**
   - User clicks on history tab on homepage
        -**Primary Sequence:**
   - 1. Customer clicks on history tab
   - 2. Website shows past purchases made by user
        -**Primary Postconditions:**
   - 1. History tab shows the details of past purchases
   - 2. Details include what service/item, name of user who bought it, and cost
