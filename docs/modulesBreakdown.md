# Modules Breakdown
# BEWARE This Kinda LONG
This program actually uses 2 modules which both stores in the libs folder on the root of the repo, and each of them do these kind of things

custServices              | inventory            
--------------------------|--------------------
Initialize Membership     | Initialize Inventory 
Manage Membership         | Manage Inventory
Use Member's Point        | Show Customer Cart
Add Member's Point        | Checkout
Check is Valid Membership | Append an Item
Do Payment                | Remove an Item
Register as Member        | Buy an Item
Revoke Membership         | Return an Item
Add Member                | Show Item's Info
Show Membership Status    | Update Inventory Storage
Update Membership Storage | 

## Initialize Function
They both worked simiiarly,
1. Open the corresponding files
2. Load the data into their corresponding arrays
3. Close the file

## Manage Function
Essentially they are a wrapper function, which provides a way to interact to their corresponding inner modules' functions

## Use Member's Point
1. Check whether the corresponding user has a membership, if not return
2. Check whether the member's point is sufficient for the transaction, if not give them a prompt then return
3. Substract their point, then return

## Add Member's Point
1. Check whether the corresponding user has a membership, if not return
2. Get the sum of point to be added
3. Increase their point by the amount they added, then return

## Check is Valid Membership
1. Get their hash value by hashing their name
2. Check if in the (their hash value)-th position in the membership storage, resides a data AND contain the same name as theirs, then return the corresponding value according to the result of the comparison

## Do Payment
1. Show all items in the cart with their corresponding prices and quantities, then show the grand total to pay
2. Show a prompt as a choice of payment with their corresponding cost
3. a. If user decided to use point as payment, check whether they're actually a member, if not then return
b.If user decided to use cash as payment, ask them the some of their money
4. a. If their point/cash isn't sufficient to pay, return
b. If their point/cash is sufficient, empty the cart, then return

## Register as Member / Append Item
Its logically similar
1. Get their hash value by hashing their name
2. Check the content of the (their hash-value)-th position in their corresponding storage
3. a. If vacant, put the newly made data in there, update the storage, then return
b. if not, assumes its already exist, then return

## Revoke a Member / Remove Item
Its logically similar
1. Get their hash value by hashing their name
2. Check the content of the (their hash-value)-th position in their corresponding storage
3. a. if vacant, return
    b. if not, NULL'd it, then update the storage, then return

## Add Member / Add Item
Its logically similar
1. Parse the raw data into a parseable data
2. Get their hash value by hashing their name
3. Check the content of the (their hash-value)-th position in their corresponding storage
4. a. if vacant, put the parsed data there, then return
b. if not, return

## Show Membership Status / Show Item's Info
Its logically similar
1. Get their hash value by hashing their name
2. Get the content of their corresponding data in their storage
3. a. if not found, return error
b. if found, show all the data, then return

## Update Membership Storage / Update Inventory Storage
Its logically similar
1. Open their corresponding file in write mode
2. Loop through their corresponding storage
3. if its exist a data, write it to the folder in a formatted way
4. return

## Show Customer Cart
1. Loop through the list
2. if existed a data, print all data on it
3. return

## Buy an Item
1. Check if Item exist
a. if exist continue
b. if not return
2. Check if the amount to buy more than stocks
a. if true, change amount to buy to the stocks, then continue
b. if false, continue
3. substract the stock by the amount bought
4. return

## Return an Item
1. Check if Item exist
2. Remove the data from customer cart
3. Add the amount returned to the stock
4. return

## Checkout
1. Check if cart is empty, if true, return
2. Loop through the cart
3. If exist a data, calculate the cost as the amount bought times prices
4. return the cost

by. [nmluci](https://github.com/nmluci)