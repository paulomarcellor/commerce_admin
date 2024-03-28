from faker import Faker
import random
import sqlite3

fake = Faker('en_US')

occupations = [
    'Engineer',
    'Teacher',
    'Doctor',
    'Lawyer',
    'Nurse',
    'Programmer',
    'Chef',
    'Artist',
    'Accountant',
    'Writer'
]

conn = sqlite3.connect('commerce.db')
c = conn.cursor()

### CLIENTS DATABASE
def generate_marital_status():
    return random.choice(['Single', 'Married', 'Divorced', 'Widowed'])

for _ in range(100):
    name = fake.name()
    age = random.randint(18, 90)
    marital_status = generate_marital_status()
    email = fake.email()
    phone = fake.phone_number()
    occupation = random.choice(occupations)
    preferencial_communication = fake.random_element(elements=('Email', 'Phone', 'SMS'))
    location = fake.address()
    average_ticket = 0

    c.execute('''INSERT INTO CLIENTS (name, age, marital_status, email, phone, occupation, preferencial_communication, location, average_ticket)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (name, age, marital_status, email, phone, occupation, preferencial_communication, location, average_ticket))

## PRODUCTS DATABASE
def generate_price(cost):
    increase_percentage = random.uniform(1.0, 1.4)  # Aumento aleatório entre 100% e 140%
    return round(cost * increase_percentage, 2)

# Dicionário de produtos e categorias
products = {
    # Electronics
    'Smartphone': ['Electronics', 800, generate_price(800)],  # [categoria, preço bruto, função de preço]
    'Laptop': ['Electronics', 1200, generate_price(1200)],
    'Wireless Headphones': ['Electronics', 150, generate_price(150)],
    'Digital Camera': ['Electronics', 500, generate_price(500)],
    'Smart TV': ['Electronics', 1000, generate_price(1000)],
    'Tablet': ['Electronics', 300, generate_price(300)],
    'Bluetooth Speaker': ['Electronics', 100, generate_price(100)],
    'Fitness Tracker': ['Electronics', 80, generate_price(80)],
    'Gaming Console': ['Electronics', 400, generate_price(400)],
    'Portable Charger': ['Electronics', 30, generate_price(30)],
    
    # Clothing
    'T-Shirt': ['Clothing', 20, generate_price(20)],
    'Jeans': ['Clothing', 50, generate_price(50)],
    'Sneakers': ['Clothing', 80, generate_price(80)],
    'Dress': ['Clothing', 70, generate_price(70)],
    'Hoodie': ['Clothing', 40, generate_price(40)],
    'Jacket': ['Clothing', 100, generate_price(100)],
    'Skirt': ['Clothing', 60, generate_price(60)],
    'Swimwear': ['Clothing', 50, generate_price(50)],
    'Socks': ['Clothing', 10, generate_price(10)],
    'Underwear': ['Clothing', 15, generate_price(15)],
    
    # Food
    'Apples': ['Food', 2, generate_price(2)],
    'Bread': ['Food', 3, generate_price(3)],
    'Milk': ['Food', 4, generate_price(4)],
    'Eggs': ['Food', 2, generate_price(2)],
    'Chicken': ['Food', 8, generate_price(8)],
    'Pasta': ['Food', 5, generate_price(5)],
    'Rice': ['Food', 4, generate_price(4)],
    'Chocolate': ['Food', 3, generate_price(3)],
    'Ice Cream': ['Food', 6, generate_price(6)],
    'Coffee': ['Food', 7, generate_price(7)],
    
    # Cosmetics
    'Lipstick': ['Cosmetics', 15, generate_price(15)],
    'Mascara': ['Cosmetics', 12, generate_price(12)],
    'Foundation': ['Cosmetics', 20, generate_price(20)],
    'Eyeliner': ['Cosmetics', 10, generate_price(10)],
    'Shampoo': ['Cosmetics', 8, generate_price(8)],
    'Conditioner': ['Cosmetics', 10, generate_price(10)],
    'Face Cream': ['Cosmetics', 25, generate_price(25)],
    'Body Lotion': ['Cosmetics', 18, generate_price(18)],
    'Perfume': ['Cosmetics', 30, generate_price(30)],
    'Nail Polish': ['Cosmetics', 5, generate_price(5)],
    
    # Furniture
    'Sofa': ['Furniture', 500, generate_price(500)],
    'Bed': ['Furniture', 800, generate_price(800)],
    'Dining Table': ['Furniture', 300, generate_price(300)],
    'Wardrobe': ['Furniture', 400, generate_price(400)],
    'Desk': ['Furniture', 200, generate_price(200)],
    'Bookshelf': ['Furniture', 150, generate_price(150)],
    'Coffee Table': ['Furniture', 100, generate_price(100)],
    'Armchair': ['Furniture', 250, generate_price(250)],
    'Dresser': ['Furniture', 350, generate_price(350)],
    'TV Stand': ['Furniture', 150, generate_price(150)],
    
    # Books
    'Harry Potter and the Philosopher\'s Stone': ['Books', 15, generate_price(15)],
    'To Kill a Mockingbird': ['Books', 10, generate_price(10)],
    '1984': ['Books', 12, generate_price(12)],
    'The Great Gatsby': ['Books', 10, generate_price(10)],
    'The Catcher in the Rye': ['Books', 8, generate_price(8)],
    'Lord of the Rings Trilogy': ['Books', 25, generate_price(25)],
    'The Hobbit': ['Books', 10, generate_price(10)],
    'Pride and Prejudice': ['Books', 8, generate_price(8)],
    'The Hunger Games': ['Books', 10, generate_price(10)],
    'The Da Vinci Code': ['Books', 10, generate_price(10)],
    
    # Toys
    'Lego Set': ['Toys', 50, generate_price(50)],
    'Barbie Doll': ['Toys', 30, generate_price(30)],
    'Board Game': ['Toys', 20, generate_price(20)],
    'Action Figure': ['Toys', 15, generate_price(15)],
    'Dollhouse': ['Toys', 80, generate_price(80)],
    'Puzzle': ['Toys', 10, generate_price(10)],
    'Teddy Bear': ['Toys', 20, generate_price(20)],
    'Play-Doh Set': ['Toys', 15, generate_price(15)],
    'Hot Wheels Set': ['Toys', 10, generate_price(10)],
    'Stuffed Animal': ['Toys', 15, generate_price(15)],
    
    # Tools
    'Cordless Drill': ['Tools', 80, generate_price(80)],
    'Screwdriver Set': ['Tools', 20, generate_price(20)],
    'Hammer': ['Tools', 15, generate_price(15)],
    'Measuring Tape': ['Tools', 10, generate_price(10)],
    'Power Saw': ['Tools', 120, generate_price(120)],
    'Pliers': ['Tools', 15, generate_price(15)],
    'Wrench Set': ['Tools', 30, generate_price(30)],
    'Toolbox': ['Tools', 25, generate_price(25)],
    'Circular Saw': ['Tools', 100, generate_price(100)],
    'Angle Grinder': ['Tools', 50, generate_price(50)],
    
    # Sporting Goods
    'Soccer Ball': ['Sporting Goods', 20, generate_price(20)],
    'Basketball': ['Sporting Goods', 25, generate_price(25)],
    'Yoga Mat': ['Sporting Goods', 15, generate_price(15)],
    'Dumbbell Set': ['Sporting Goods', 100, generate_price(100)],
    'Tennis Racket': ['Sporting Goods', 50, generate_price(50)],
    'Running Shoes': ['Sporting Goods', 80, generate_price(80)],
    'Golf Clubs': ['Sporting Goods', 200, generate_price(200)],
    'Swimming Goggles': ['Sporting Goods', 20, generate_price(20)],
    'Cycling Helmet': ['Sporting Goods', 40, generate_price(40)],
    'Boxing Gloves': ['Sporting Goods', 50, generate_price(50)],
    
    # Video Games
    'FIFA 24': ['Video Games', 60, generate_price(60)],
    'The Legend of Zelda: Breath of the Wild 2': ['Video Games', 70, generate_price(70)],
    'Grand Theft Auto VI': ['Video Games', 80, generate_price(80)],
    'Fortnite': ['Video Games', 40, generate_price(40)],
    'Minecraft': ['Video Games', 30, generate_price(30)],
    'Assassin\'s Creed: Valhalla': ['Video Games', 70, generate_price(70)],
    'NBA 2K24': ['Video Games', 50, generate_price(50)],
    'God of War: Ragnarok': ['Video Games', 80, generate_price(80)],
    'Spider-Man 2': ['Video Games', 60, generate_price(60)],
    'Overwatch 2': ['Video Games', 70, generate_price(70)]
}

for product in products.items():
    name = product[0]
    category = product[1][0]
    cost = product[1][1]
    price = product[1][2]
    c.execute('''INSERT INTO PRODUCTS (name, category, cost, price)
                        VALUES (?, ?, ?, ?)''', (name, category, cost, price))

# Commit e fecha a conexão com o banco de dados
conn.commit()
conn.close()