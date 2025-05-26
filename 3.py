import random
import json
import string


def generate_random_name():
    """Генерирует случайное имя и фамилию."""
    first_names = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "David", "Emma"]
    last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"


def generate_random_email(name):
    """Генерирует email на основе имени."""
    first, last = name.lower().split()
    domains = ["gmail.com", "yahoo.com", "example.com", "outlook.com", "hotmail.com"]
    return f"{first}.{last}@{random.choice(domains)}"


def generate_random_password(length=12):
    """Генерирует случайный пароль из букв, цифр и знаков препинания."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


def generate_user_data():
    """Создает словарь с данными пользователя."""
    name = generate_random_name()
    age = random.randint(18, 80)
    email = generate_random_email(name)
    password = generate_random_password()

    return {
        "name": name,
        "age": age,
        "email": email,
        "password": password
    }


def save_to_json(data, filename="user_data.json"):
    """Сохраняет данные в JSON-файл."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def load_from_json(filename="user_data.json"):
    """Читает данные из JSON-файла."""
    with open(filename, 'r') as f:
        return json.load(f)


# Генерируем данные пользователя
user_data = generate_user_data()

# Сохраняем в файл
save_to_json(user_data)

# Читаем из файла и выводим
loaded_data = load_from_json()
print(json.dumps(loaded_data, indent=4))
