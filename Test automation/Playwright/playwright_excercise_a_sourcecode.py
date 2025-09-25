html_content = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Playwright Semantic Locators Practice</title>
</head>

<body>
    <header>
        <img src="images/logo.png" alt="Company Logo" width="150">
        <nav>
            <a href="/home">Home</a>
            <a href="/about">About Us</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>
    <main>
        <section id="login-section">
            <h2>Login Form</h2>
            <form>
                <label for="email">Email</label>
                <input id="email" type="email" placeholder="Enter your email">
                <label for="password">Password</label>
                <input id="password" type="password" placeholder="Enter your pa
ssword">
                <button type="submit">Login</button>
                <button type="button">Sign Up</button>
                Playwright Exercise 1
            </form>
        </section>
        <section id="search-section">
            <h2>Product Search</h2>
            <input type="text" placeholder="Search products…">
            <button>Search</button>
        </section>
        <section id="cart-section">
            <h2>Shopping Cart</h2>
            <img src="images/cart.png" alt="Cart Icon" width="50">
        </section>
    </main>
    <footer>
    </footer>
</body>

</html>
"""