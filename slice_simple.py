def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.
    print(texto[:3].lower())
    todo = len(texto)
    mid = int(todo/2)
    print(texto[(mid - 1):(mid + 2)].lower())
    print((texto[0:4] + texto[-3:]).lower() )
  

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
slice_simple()

