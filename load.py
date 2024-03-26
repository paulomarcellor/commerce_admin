import sqlite3
import random
import string

products = [
    {"id": 1, "name": "Smartphone", "category": "Electronics"},
    {"id": 2, "name": "Running Shoes", "category": "Sports"},
    {"id": 3, "name": "Laptop", "category": "Electronics"},
    {"id": 4, "name": "T-shirt", "category": "Fashion"},
    {"id": 5, "name": "Headphones", "category": "Electronics"},
    {"id": 6, "name": "Backpack", "category": "Accessories"},
    {"id": 7, "name": "Sunglasses", "category": "Accessories"},
    {"id": 8, "name": "Digital Camera", "category": "Electronics"},
    {"id": 9, "name": "Yoga Mat", "category": "Sports"},
    {"id": 10, "name": "Watch", "category": "Accessories"},
    {"id": 11, "name": "Tennis Racket", "category": "Sports"},
    {"id": 12, "name": "Dress", "category": "Fashion"},
    {"id": 13, "name": "Gaming Console", "category": "Electronics"},
    {"id": 14, "name": "Water Bottle", "category": "Accessories"},
    {"id": 15, "name": "Running Shorts", "category": "Sports"},
    {"id": 16, "name": "Portable Speaker", "category": "Electronics"},
    {"id": 17, "name": "Wallet", "category": "Accessories"},
    {"id": 18, "name": "Hiking Boots", "category": "Outdoor"},
    {"id": 19, "name": "Earrings", "category": "Jewelry"},
    {"id": 20, "name": "Tablet", "category": "Electronics"},
    {"id": 21, "name": "Gym Bag", "category": "Accessories"},
    {"id": 22, "name": "Baseball Cap", "category": "Fashion"},
    {"id": 23, "name": "Cycling Helmet", "category": "Sports"},
    {"id": 24, "name": "Wireless Mouse", "category": "Electronics"},
    {"id": 25, "name": "Scarf", "category": "Fashion"},
    {"id": 26, "name": "Jump Rope", "category": "Fitness"},
    {"id": 27, "name": "USB Flash Drive", "category": "Electronics"},
    {"id": 28, "name": "Tennis Shoes", "category": "Sports"},
    {"id": 29, "name": "Luggage", "category": "Travel"},
    {"id": 30, "name": "Necklace", "category": "Jewelry"},
    {"id": 31, "name": "Wireless Earbuds", "category": "Electronics"},
    {"id": 32, "name": "Swimwear", "category": "Fashion"},
    {"id": 33, "name": "Bluetooth Speaker", "category": "Electronics"},
    {"id": 34, "name": "Running Jacket", "category": "Sports"},
    {"id": 35, "name": "Sleeping Bag", "category": "Outdoor"},
    {"id": 36, "name": "Bracelet", "category": "Jewelry"},
    {"id": 37, "name": "USB Charger", "category": "Electronics"},
    {"id": 38, "name": "Camping Tent", "category": "Outdoor"},
    {"id": 39, "name": "Sneakers", "category": "Fashion"},
    {"id": 40, "name": "Hiking Backpack", "category": "Outdoor"},
    {"id": 41, "name": "Smartwatch", "category": "Electronics"},
    {"id": 42, "name": "Hoodie", "category": "Fashion"},
    {"id": 43, "name": "Football", "category": "Sports"},
    {"id": 44, "name": "External Hard Drive", "category": "Electronics"},
    {"id": 45, "name": "Sunscreen", "category": "Skincare"},
    {"id": 46, "name": "Basketball", "category": "Sports"},
    {"id": 47, "name": "Portable Charger", "category": "Electronics"},
    {"id": 48, "name": "Rain Jacket", "category": "Outdoor"},
    {"id": 49, "name": "Earrings", "category": "Accessories"},
    {"id": 50, "name": "Polarized Sunglasses", "category": "Accessories"},
    {"id": 51, "name": "Mouse Pad", "category": "Electronics"},
    {"id": 52, "name": "Swimsuit", "category": "Fashion"},
    {"id": 53, "name": "Cycling Gloves", "category": "Sports"},
    {"id": 54, "name": "Wireless Keyboard", "category": "Electronics"},
    {"id": 55, "name": "Sleeping Pad", "category": "Outdoor"},
    {"id": 56, "name": "Bracelet", "category": "Fashion"},
    {"id": 57, "name": "Fitness Tracker", "category": "Electronics"},
    {"id": 58, "name": "Yoga Pants", "category": "Sports"},
    {"id": 59, "name": "Hiking Shoes", "category": "Outdoor"},
    {"id": 60, "name": "Crossbody Bag", "category": "Fashion"},
    {"id": 61, "name": "Bluetooth Headset", "category": "Electronics"},
    {"id": 62, "name": "Waterproof Backpack", "category": "Outdoor"},
    {"id": 63, "name": "Running Belt", "category": "Sports"},
    {"id": 64, "name": "Ring", "category": "Jewelry"},
    {"id": 65, "name": "Wireless Router", "category": "Electronics"},
    {"id": 66, "name": "Cycling Shorts", "category": "Sports"},
    {"id": 67, "name": "Solar Charger", "category": "Electronics"},
    {"id": 68, "name": "Trekking Poles", "category": "Outdoor"},
    {"id": 69, "name": "Baseball Glove", "category": "Sports"},
    {"id": 70, "name": "Travel Pillow", "category": "Travel"},
    {"id": 71, "name": "Smart Lock", "category": "Electronics"},
    {"id": 72, "name": "Dumbbells", "category": "Fitness"},
    {"id": 73, "name": "Camping Stove", "category": "Outdoor"},
    {"id": 74, "name": "Leather Jacket", "category": "Fashion"},
    {"id": 75, "name": "VR Headset", "category": "Electronics"},
    {"id": 76, "name": "Running Socks", "category": "Sports"},
    {"id": 77, "name": "Portable Hammock", "category": "Outdoor"},
    {"id": 78, "name": "Hair Dryer", "category": "Beauty"},
    {"id": 79, "name": "Cycling Jersey", "category": "Sports"},
    {"id": 80, "name": "External Battery Pack", "category": "Electronics"},
    {"id": 81, "name": "Rollerblades", "category": "Sports"},
    {"id": 82, "name": "Smart Thermostat", "category": "Home"},
    {"id": 83, "name": "Camping Chair", "category": "Outdoor"},
    {"id": 84, "name": "Leather Bag", "category": "Fashion"},
    {"id": 85, "name": "Desktop Computer", "category": "Electronics"},
    {"id": 86, "name": "Hiking Pole", "category": "Outdoor"},
    {"id": 87, "name": "Makeup Brushes", "category": "Beauty"},
    {"id": 88, "name": "Snowboard", "category": "Sports"},
    {"id": 89, "name": "Portable Projector", "category": "Electronics"},
    {"id": 90, "name": "Winter Gloves", "category": "Fashion"},
    {"id": 91, "name": "Bluetooth Earphones", "category": "Electronics"},
    {"id": 92, "name": "Camping Lantern", "category": "Outdoor"},
    {"id": 93, "name": "Skateboard", "category": "Sports"},
    {"id": 94, "name": "Facial Cleanser", "category": "Skincare"},
    {"id": 95, "name": "Fishing Rod", "category": "Outdoor"},
    {"id": 96, "name": "Wireless Security Camera", "category": "Electronics"},
    {"id": 97, "name": "Travel Adapter", "category": "Travel"},
    {"id": 98, "name": "Winter Hat", "category": "Fashion"},
    {"id": 99, "name": "Action Camera", "category": "Electronics"},
    {"id": 100, "name": "Gaming Mouse", "category": "Electronics"}
]

# Função para gerar um nome aleatório
def generate_name():
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    return ''.join(random.choice(consonants) + random.choice(vowels) for _ in range(random.randint(4, 10))).title()

# Função para gerar uma idade aleatória entre 18 e 80
def generate_age():
    return random.randint(18, 80)

# Função para gerar um sexo aleatório
def generate_sex():
    return random.choice(['M', 'F'])

# Função para gerar um estado civil aleatório
def generate_marital_status():
    return random.choice(['Single', 'Married', 'Divorced', 'Widowed'])

# Função para gerar um e-mail aleatório
def generate_email(name):
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    return f"{name.lower().replace(' ', '_')}@{random.choice(domains)}"

# Função para gerar um número de telefone aleatório
def generate_phone():
    return ''.join(random.choices(string.digits, k=9))

# Função para gerar uma ocupação aleatória
def generate_occupation():
    occupations = ["Engineer", "Teacher", "Doctor", "Artist", "Lawyer", "Student", "Accountant", "Entrepreneur"]
    return random.choice(occupations)

# Função para gerar uma forma de comunicação preferencial aleatória
def generate_preferencial_communication():
    preferences = ["Email", "Phone", "SMS", "WhatsApp"]
    return ', '.join(random.sample(preferences, random.randint(1, len(preferences))))

# Função para gerar uma localização aleatória
def generate_location():
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
    return random.choice(cities)

# Função para gerar um ticket médio aleatório
def generate_average_ticket():
    return round(random.uniform(50.0, 500.0), 2)

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('commerce.db')
cursor = conn.cursor()

# Gerar e inserir 1000 registros aleatórios na tabela CLIENTS
client_id = 1
for _ in range(1000):
    name = generate_name()
    age = generate_age()
    sex = generate_sex()
    marital_status = generate_marital_status()
    email = generate_email(name)
    phone = generate_phone()
    occupation = generate_occupation()
    preferencial_communication = generate_preferencial_communication()
    location = generate_location()
    average_ticket = generate_average_ticket()

    cursor.execute('''INSERT INTO CLIENTS (client_id, name, age, sex, marital_status, email, phone, occupation, preferencial_communication, location, average_ticket) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (client_id, name, age, sex, marital_status, email, phone, occupation, preferencial_communication, location, average_ticket))
    client_id += 1

# Insert products
for i in products:
    product_id = i['id']
    product_name = i['name']
    product_category = i['category']
    cursor.execute('''INSERT INTO PRODUCTS (product_id, name, category) 
                  VALUES (?, ?, ?)''', (product_id, product_name, product_category))

# Commit das alterações e fechar conexão
conn.commit()
conn.close()

print("Registros inseridos com sucesso!")