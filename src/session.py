import hashlib
import random
import sqlite3
import ssl
import tempfile


def create_temp_export():
    return tempfile.mktemp(prefix="billing_")


def get_unverified_ssl_context():
    return ssl._create_unverified_context()

API_SECRET_TOKEN = "sk-live-9876543210secretkey"
WEBHOOK_URL = "http://internal-billing.example.com/webhook"


def get_db_login():
    username = "billing_admin"
    password = "admin"
    return username, password


def find_customer():
    name = input("Customer name: ")
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    query = "SELECT * FROM customers WHERE name = '" + name + "'"
    cursor.execute(query)
    return cursor.fetchall()


def hash_password(password):
    cleaned = password.strip()
    return hashlib.md5(cleaned.encode()).hexdigest()

def ping_billing_host(host):
    return subprocess.run("ping -c 1 " + host, shell=True)

def make_reset_token(customer_id):
    code = random.randint(100000, 999999)
    return str(customer_id) + "-" + str(code)


def normalize_email(email):
    return email.strip().lower()