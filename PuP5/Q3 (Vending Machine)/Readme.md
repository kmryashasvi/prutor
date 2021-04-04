# Vending Machine
## LAB5
## PROBLEM STATEMENT
In this program, you have to simulate a simple Vending Machine. You need to read a file, ```__VendingItems__.csv```. It contains Item names and their Prices (integers) separated by a PIPE (```|```). Here is a sample:<br>
Potato Chips|20<br>
Popcorn|30<br>
<br>
(I encourage you to find out the rest of the lines in the file.)<br>
<br>
The input consists of an item name. If the item is not a valid item (i.e., an item available in the vending machine), you need to ask the user to try again.<br>
After a proper item is read, the program expects the user to provide the money to deposit in the vending machine (integer). Again, the program will ask the user to try again till a proper integer is read. 
<br>
Finally, depending upon the money deposited by the user, Machine will display appropriate message(s). See the examples.<br>
<br>

### EXAMPLES: 
<pre>
INPUT:
batata vada
pani-puri
Potato Chips
credit-card
debit-card
25
OUTPUT:
Available Items are ['Potato Chips', 'Popcorn', 'Chocolate', 'Biscuit', 'Soft Drink'].
Try Again.
Available Items are ['Potato Chips', 'Popcorn', 'Chocolate', 'Biscuit', 'Soft Drink'].
Try Again.
Bad Input credit-card.
Try Again.
Bad Input debit-card.
Try Again.
Thank you for your purchase. Enjoy
Do not forget to collect your change, 5 Rs.


INPUT:
Chocolate
10
OUTPUT:
Sorry, can not buy item. Not enough money

INPUT:
Chocolate
15
OUTPUT:
Thank you for your purchase. Enjoy

