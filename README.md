# 🏠 REMS - Real Estate Management System

REMS is a modern **Real Estate Management System** built using **Django** for the backend and **React** for the frontend. This system is designed to streamline property management, allowing users to manage properties, tenants, leases, and more in an efficient and user-friendly manner.

---

## ✨ Features

### 🛠️ Admin Features
- **🏢 Property Management**: Add, update, and delete properties.
- **👤 Tenant Management**: Manage tenant information and lease agreements.
- **📅 Lease Tracking**: Track lease start and end dates, rent payments, and lease terms.
- **🔧 Maintenance Requests**: Handle maintenance requests and assign tasks to staff.
- **💰 Financial Tracking**: Monitor rent payments, expenses, and generate financial reports.
- **👥 User Roles**: Assign roles (Admin, Manager, Staff) with different permissions.

### 🏠 Tenant Features
- **📊 Dashboard**: View property details, lease information, and payment history.
- **🔧 Maintenance Requests**: Submit and track maintenance requests.
- **💳 Rent Payment**: Pay rent online and view payment history.

---

## 🛠️ Technologies Used

### Backend
- **🐍 Django**: A high-level Python web framework for building secure and scalable backend systems.
- **🌐 Django REST Framework (DRF)**: For building RESTful APIs to connect the frontend and backend.
- **🐘 PostgreSQL**: A powerful relational database for storing application data.
- **🔐 JWT Authentication**: Secure user authentication using JSON Web Tokens.

### Frontend
- **⚛️ React**: A JavaScript library for building dynamic and responsive user interfaces.
- **🔄 Redux**: For state management across the application.
- **📡 Axios**: For making HTTP requests to the backend API.
- **🎨 Material-UI**: A popular React UI framework for designing modern and clean interfaces.

### Other Tools
- **🐳 Docker**: For containerization and easy deployment.
- **🐙 Git**: For version control and collaboration.
- **📤 Postman**: For testing API endpoints.

---

## 🚀 Installation

### Prerequisites
- **🐍 Python 3.8+**
- **🖥️ Node.js 14+**
- **🐘 PostgreSQL**
- **🐳 Docker** (optional)

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/REMS.git
   cd REMS/backend

2.Create a virtual environment and install dependencies:
 ```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3.Set up the database:

Update the settings.py file with your PostgreSQL credentials.

Run migrations:
 ```bash

python manage.py migrate

4.Create a superuser for the admin panel:
 ```bash

python manage.py createsuperuser
