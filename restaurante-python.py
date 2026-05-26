# =====================================================================
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Problema 2: Gestión de Precios de un Menú de Restaurante
# =====================================================================

def calcular_precio_final(categoria_producto, precio_base, categoria_objetivo, umbral_precio):
    """
    Función encargada de calcular el precio final aplicando la lógica de negocio.
    Retorna el precio final con o sin descuento del 15%.
    """
    # Validar si cumple con la categoría objetivo Y supera el umbral de precio
    if categoria_producto.lower() == categoria_objetivo.lower() and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        # Si no cumple las condiciones, se mantiene el precio base
        precio_final = precio_base
        
    return precio_final


def main():
    print("==================================================")
    print("     SISTEMA DE GESTIÓN DE PRECIOS - RESTAURANTE   ")
    print("==================================================\n")
    
    # 1. Definición de la matriz con 6 productos (Nombre, Categoría, Precio Base)
    # Usamos una lista de listas para representar la matriz en Python
    menu_restaurante = [
        ["Hamburguesa Angus", "Comida Rápida", 35000],
        ["Papas Supremas", "Comida Rápida", 12000],
        ["Filete de Salmón", "Plato Fuerte", 45000],
        ["Pechuga a la Plancha", "Plato Fuerte", 28000],
        ["Jugo Natural", "Bebidas", 7000],
        ["Limonada Cerezada", "Bebidas", 9500]
    ]
    
    # 2. Definición de parámetros para la promoción
    # Ajusta estos valores según lo que quieras evaluar
    categoria_promocion = "Plato Fuerte"
    umbral_minimo_precio = 30000
    
    print(f"--- Promoción Activa ---")
    print(f"Categoría objetivo: {categoria_promocion}")
    print(f"Umbral de precio mayor a: ${umbral_minimo_precio:,}\n")
    print("----------------------------------------------------------------------")
    print(f"{'Producto':<25} | {'Categoría':<15} | {'Precio Base':<12} | {'Precio Final':<12}")
    print("----------------------------------------------------------------------")
    
    # 3. Recorrido de la matriz para procesar cada producto
    for producto in menu_restaurante:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]
        
        # Llamado a la función (módulo) para aplicar la lógica
        precio_final = calcular_precio_final(categoria, precio_base, categoria_promocion, umbral_minimo_precio)
        
        # Formatear la salida en filas ordenadas
        print(f"{nombre:<25} | {categoria:<15} | ${precio_base:<11,} | ${precio_final:<11,.0f}")
        
    print("----------------------------------------------------------------------")

# Punto de entrada del programa
if __name__ == "__main__":
    main()