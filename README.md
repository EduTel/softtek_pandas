Debido a que solo se me paso las imagenes y no los datos tuve que usar OCR
* Estructura
    - Datos de prueba
        - data.py
    - Codigo base
        - index.py
    - Pruebas unitarias
        - test.py

instrucciones para ejecutar el codigo
```
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python index.py
```

## Pruebas Unitarias.
Para correr las pruebas unitarias en necesario contar con unittest que es la herramienta con la que se realizaron. Para ejecutarlas se dbe estar en el path donde se encuentra el proyecto y ejecutar:
```
    python -m unittest -v
```

# notas
* "seasons problem" se tiene que comparar por fecha y no por dia del año ya que esto podria  
hacer que se muestre incorrectamente las estaciones en dias bisiestos  

* "detecting change" se tiene que comprobar si hay un dia anterior para poder saber si el clima cambio o no  
si no se puede confundir si el primer dia tiene True lo devuelva como un cambio
