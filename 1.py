# decodificador.py
import sys

def decoder():
    # Primero, se muestran los valores intermedios en el cálculo.
    # 1. Analizamos las lambdas y su co_nlocals, co_stacksize, etc.
    
    # Creación de una función lambda para obtener los valores de código
    lambda_code = (lambda _: _).__code__
    print("lambda_code:", lambda_code)
    
    # Los atributos que se están manipulando
    print("co_nlocals:", lambda_code.co_nlocals)
    print("co_stacksize:", lambda_code.co_stacksize)
    print("co_argcount:", lambda_code.co_argcount)
    print("co_flags:", lambda_code.co_flags)
    print("co_filename:", lambda_code.co_filename)
    print("co_kwonlyargcount:", lambda_code.co_kwonlyargcount)
    print("co_posonlyargcount:", lambda_code.co_posonlyargcount)
    
    # Evaluar el valor de __spec__ para obtener su comportamiento
    print("sys.__spec__:", sys.__spec__)
    
    # Evaluar la estructura de __builtins__ para ver qué contiene
    print("Builtins:", dir(__builtins__))
    
    # Intentamos acceder al atributo de '__spec__.__reduce_ex__.__class__.__eq__.__class__.__name__'
    try:
        attribute_value = getattr(__builtins__, "__spec__.__reduce_ex__.__class__.__eq__.__class__.__name__")
        print("Found attribute:", attribute_value)
    except AttributeError as e:
        print("Error accessing attribute:", e)
    
    # Podemos seguir evaluando más componentes en el mismo formato para desofuscar.
    return

# Cargar y ejecutar el archivo de código ofuscado
def execute_ofuscado():
    try:
        # Cargar el archivo con el código ofuscado
        with open('codigo_ofuscado.py', 'r') as f:
            exec(f.read())  # Ejecutar el código ofuscado
    except Exception as e:
        print(f"Error al ejecutar el código ofuscado: {e}")

# Llamamos a la función decodificadora
execute_ofuscado()

# Llamamos a la función para ver los valores intermedios
decoder()

