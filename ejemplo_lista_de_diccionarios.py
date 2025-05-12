# Lista vacía que va a contener diccionarios de productos
inventory = []

# Función para validar que el texto no esté vacío y solo contenga letras
def validate_str(value):
    return value.strip() != "" and value.replace(" ", "").isalpha()

# Función para validar que sea un número entero positivo
def validate_num(value):
    return value.strip().isdigit() and int(value) > 0

# Agrega productos al inventario
def create_product():
    while True:
        name = input("Ingresa el nombre del producto: ").strip().lower()
        if not validate_str(name):
            print("Error. Ingresa un nombre válido (solo letras).")
            continue

        # Verifica si ya existe el producto
        for product in inventory:
            if product['nombre'] == name:
                print("Este producto ya existe. Puedes actualizarlo si lo deseas.")
                return

        price = input("Ingresa el precio del producto: ").strip()
        quantity = input("Ingresa la cantidad del producto: ").strip()

        if not validate_num(price) or not validate_num(quantity):
            print("Error. Precio y cantidad deben ser números positivos.")
            continue

        # Se guarda en minúscula para estandarizar
        inventory.append({
            "nombre": name,
            "precio": int(price),
            "cantidad": int(quantity)
        })
        print(f"✅ Producto '{name}' agregado exitosamente.")

        choice = input("¿Deseas ingresar otro producto? [s/n]: ").strip().lower()
        if choice == "n":
            break

# Consulta un producto en el inventario
def get_product():
    name = input("Ingresa el nombre del producto: ").strip().lower()
    if not validate_str(name):
        print("Error. Ingresa un nombre válido.")
        return

    for product in inventory:
        if product["nombre"] == name:
            print("✅ Producto encontrado:")
            print("Nombre:", product["nombre"])
            print("Precio:", product["precio"])
            print("Cantidad:", product["cantidad"])
            return product["precio"], product["cantidad"]

    print("❌ Producto no encontrado.")

# Actualiza el precio de un producto
def update_product():
    name = input("Ingresa el nombre del producto: ").strip().lower()
    for product in inventory:
        if product["nombre"] == name:
            new_price = input("Ingresa el nuevo precio: ").strip()
            if not validate_num(new_price):
                print("Error. Precio inválido.")
                return
            product["precio"] = int(new_price)
            print(f"✅ Precio del producto '{name}' actualizado.")
            return
    print("❌ Producto no encontrado.")

# Elimina un producto del inventario
def delete_product():
    name = input("Ingresa el nombre del producto: ").strip().lower()
    for i, product in enumerate(inventory):
        if product["nombre"] == name:
            inventory.pop(i)
            print(f"✅ Producto '{name}' eliminado.")
            return
    print("❌ Producto no encontrado.")

# Calcula el valor total del inventario
def calculate_inventory():
    total = 0
    for product in inventory:
        total += product["precio"] * product["cantidad"]
    print(f"💰 Valor total del inventario: {total}")

# Menú principal
def menu():
    while True:
        print("""
===== MENÚ DE INVENTARIO =====
[1] Agregar producto
[2] Consultar producto
[3] Actualizar precio
[4] Eliminar producto
[5] Calcular valor total
[6] Salir
""")
        option = input("Elige una opción: ").strip()
        match option:
            case "1":
                create_product()
            case "2":
                get_product()
            case "3":
                update_product()
            case "4":
                delete_product()
            case "5":
                calculate_inventory()
            case "6":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            case _:
                print("❌ Opción no válida.")

# Ejecutar el menú
menu()
