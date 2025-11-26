from datetime import datetime

def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def input_data(prompt):
    while True:
        data = input(prompt).strip()
        if validar_data(data):
            return data
        print("Data inválida. Use o formato YYYY-MM-DD.")
