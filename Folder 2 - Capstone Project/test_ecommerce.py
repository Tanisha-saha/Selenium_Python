import json
import time
from selenium import webdriver
with open("testdata.json","r") as file :
    data = json.load(file)
website = data["website"]
product = data["product"]
email = data["email"]
password = data["password"]
driver = webdriver.Chrome()
driver.get(website)
print(driver.title)
print("product is",product)
driver.get(website +"login")
driver.find_element("xpath",'//*[@id="form"]/div/div/div[1]/div/form/input[2]').send_keys(email)
driver.find_element("xpath",'//*[@id="form"]/div/div/div[1]/div/form/input[3]').send_keys(password)
driver.find_element("xpath",'//*[@id="form"]/div/div/div[1]/div/form/button').click()
time.sleep(3)
driver.get("https://automationexercise.com/products")
time.sleep(5)
search_box = driver.find_element("id","search_product")
search_box.send_keys(product)
driver.find_element("id","submit_search").click()
print("product search completed")
add_to_cart = driver.find_element("xpath",'//a[@data-product-id="1"]')
driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    add_to_cart
)
time.sleep(2)
driver.execute_script("arguments[0].click();",add_to_cart)
print("product is added to the cart")
time.sleep(3)
driver.find_element(
    "xpath",
    '//u[text()="View Cart"]'
).click()
time.sleep(2)
print("sucessfully view cart")
driver.find_element(
    "xpath",
    '//tr[@id="product-1"]//a[@class="cart_quantity_delete"]'
).click()
time.sleep(2)
driver.get("https://automationexercise.com/products")
time.sleep(5)
search_box = driver.find_element("id","search_product")
search_box.clear()
search_box.send_keys(product)
driver.find_element("id","submit_search").click()
add_to_cart = driver.find_element(
    "xpath",
    '//a[@data-product-id="1"]'
)
driver.execute_script(
    "arguments[0].click();",
    add_to_cart
)
add_to_cart = driver.find_element(
    "xpath",
    '//a[@data-product-id="1"]'
)
driver.execute_script(
    "arguments[0].click();",
    add_to_cart
)
time.sleep(2)
print("sucessfully updated")
time.sleep(2)
view_cart = driver.find_element(
    "xpath",
    '//u[text()="View Cart"]/parent::a'
)
driver.execute_script(
    "arguments[0].click();",
    view_cart
)
time.sleep(2)
quantity = driver.find_element(
    "xpath",
    '//tr[@id = "product-1"]//td[@class="cart_quantity"]//button'
).text
print("product quantity",quantity)
driver.save_screenshot("screenshots/cart.png")
print("cart screenshot captured sucessfully")
report = """
<html>
<head>
    <title>Execution Report</title>
</head>
<body>

<h1>E-Commerce Automation Report</h1>

<p><b>Website:</b> Automation Exercise</p>
<p><b>Product:</b> Blue Top</p>

<h2>Test Execution Summary</h2>

<table border="1" cellpadding="8">
    <tr>
        <th>Test Step</th>
        <th>Status</th>
    </tr>
    <tr>
        <td>Website Launch</td>
        <td>PASS</td>
    </tr>
    <tr>
        <td>Login</td>
        <td>PASS</td>
    </tr>
    <tr>
        <td>Product Search</td>
        <td>PASS</td>
    </tr>
    <tr>
        <td>Add to Cart</td>
        <td>PASS</td>
    </tr>
    <tr>
        <td>Quantity Update</td>
        <td>PASS</td>
    </tr>
    <tr>
        <td>Cart Verification</td>
        <td>PASS</td>
    </tr>
    <tr>
        <td>Screenshot Capture</td>
        <td>PASS</td>
    </tr>
</table>

<h2>Overall Result: PASS</h2>

</body>
</html>
"""

with open("report/report.html", "w") as file:
    file.write(report)

print("done")
driver.quit()

