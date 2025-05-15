# 🛒 E-Commerce Website (Dairy Web-App)

An E-commerce web application incorporating essential features such as product catalog, shopping cart, checkout process, and‬ user authentication using HTML, CSS, JavaScript, Django, and SQLite3. Implemented stringent‬ security measures including SQL injection prevention, brute force protection, password hashing‬,data encryption and secure payment processing with **Razorpay**.

---

## 🚀 Features

- 🛍️ Product catalog with images, pricing, and descriptions  
- 🛒 Add-to-cart and cart management system  
- 🔐 User registration, login/logout, and profile management  
- 💳 Checkout with **Razorpay API** for secure online payments  
- 📦 Order summary and confirmation  
- 🛡️ Security implementations:
  - SQL injection prevention
  - Brute-force attack protection
  - Password hashing (Django's built-in mechanism)
  - Sensitive data encryption

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Django (Python), SQLite3  
- **Payments:** Razorpay API  
- **Authentication:** Django’s built-in auth system  
- **Security:** Django’s security middleware + custom protections  

---

## 📂 Project Structure
```
Dairy-webapp/
│
├── ec/ # Project config files
│ └── settings.py
│
├── app/ # Main app
│ ├── models.py # Product, Order, Cart models
│ ├── views.py # View logic for each page
│ ├── templates/ # HTML templates
│ └── static/ # CSS, JS, images
│
├── manage.py
└── requirements.txt
```

---

## 💳 Razorpay Integration

- Razorpay payment gateway is integrated at the checkout step.
- Secure and encrypted transactions using Razorpay’s APIs.
- Real-time confirmation and order logging upon payment success.

---

## 🔐 Security Measures

- **SQL Injection Prevention:** Django ORM safely handles queries.
- **Brute Force Protection:** Rate-limiting strategies or external middleware.
- **Password Security:** Hashed using PBKDF2 with salt.  
- **Sensitive Data Handling:** Encryption in transit and protection using Django security best practices.

---

## 🧪 How to Run Locally

1. **Clone the repo**
```
   git clone https://github.com/rohithgowdax/Dairy-webapp.git
   cd Dairy-webapp
```
2. **Create a virtual environment**
 ```
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
 ```
3. **Install dependencies**
```
pip install -r requirements.txt
```
4. **Run migrations**
```
python manage.py migrate
```
5. **Create a superuser** (optional)
```
python manage.py createsuperuser
```
6. **Run the server**
```
python manage.py runserver
```
---
# 📌 Future Improvements
- Email notifications on order placement
- Admin dashboard for order and product management
- Wishlist and product filtering
- Integration with PostgreSQL for production
---
# 👨‍💻 Author
Rohith Gowda R        
[LinkedIn](https://www.linkedin.com/in/rohithgowdax/)   
[GitHub](https://github.com/rohithgowdax)

# 📄 License
This project is licensed under the MIT License see the [LICENSE](LICENSE) file for detail.
