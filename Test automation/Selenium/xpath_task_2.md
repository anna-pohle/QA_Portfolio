#1. Schreibe das XPath für das header icon auf https://grocerymate.masterschool.com/
//div[@class='headerIcon']

#2. Auf https://grocerymate.masterschool.com/auth, schreibe das XPath für alle Eingabefelder, 
die "Sign In"-Schaltfläche, den Link "Create a new account" und den Link "Go to Home".

#a Eingabe Mail
//input[@type='email']

#b Eingabe Passwort
//input[@type='password']

#c Sign In
//button[@type='submit']

#d Create a new account
//a[@href='#!' and @class='switch-link']

#e Go to Home
//a[@href='#!' and @class='home-link']


#3. Nach dem click auf 2d, schreibe das XPath für alle Eingabefelder und die "Sign Up"-Schaltfläche.

#a Name
//input[@type='text' and @placeholder='Full Name']

#b Email
//input[@type='email']

#c Passwort
//input[@type='password']

#d Signup
//button[@type='submit']

#4. Auf https://grocerymate.masterschool.com/store, Schreibe das **XPath** der **"Confirm"**-Schaltfläche, die du im Modal sehen kannst.
//div[@class='modal-content']/button

#5. Gehe zur **Shop**Seite (https://grocerymate.masterschool.com/store#) und schreibe das **XPath** für das **Mengeneingabefeld von Oranges**, 
die **"Add to cart"** Schaltfläche für Oranges und die **"Add to wish list"** Schaltfläche für Oranges.

#a Mengeneingabe Orangen
//p[@class='lead' and text()='Oranges']/ancestor::div[@class='card']//input[@type='number']

#b Add to cart
//p[@class='lead' and text()='Oranges']/ancestor::div[@class='card']//button[@class="btn btn-primary btn-cart"]

#c Add to wishlist
//p[@class='lead' and text()='Oranges']/ancestor::div[@class='card']//button[@class="btn btn-outline-dark "]