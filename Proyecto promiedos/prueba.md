# Casos de Uso del Sistema

## Caso de Uso 1: Buscar película por título

* **Actor:** Usuario.
* **Propósito:** Buscar películas escribiendo solo una o dos palabras del título sin tener que poner el nombre entero.
* **Precondición:** Tener el catálogo cargado desde el JSON.

### Flujo Principal
1. Elegís la opción **1** en el menú.
2. Ingresás una palabra o frase (ej: `"El"` o `"batalla"`).
3. El sistema busca con `in` entre los títulos y guarda todas las coincidencias en una lista.
4. Te muestra las películas encontradas una por una en la terminal.
5. Vuelve al menú.

### Flujo Alternativo
* **A1 (No hay coincidencias):** Si lo que pusiste no coincide con nada, te avisa que no se encontraron películas y vuelve al menú.

---

## Caso de Uso 2: Listar todas las películas

* **Actor:** Usuario.
* **Propósito:** Ver el catálogo completo con todas las películas cargadas.
* **Precondición:** Tener el sistema iniciado.

### Flujo Principal
1. Elegís la opción **2** en el menú.
2. El sistema pide todas las películas con `catalogo.listar()`.
3. Te las imprime una por una en la pantalla.
4. Vuelve al menú.

---

## Caso de Uso 3: Filtrar películas por género

* **Actor:** Usuario.
* **Propósito:** Buscar y ver solo las películas de un género en particular (Acción, Fantasía, etc.).
* **Precondición:** Que haya películas en el catálogo.

### Flujo Principal
1. Elegís la opción **3** en el menú.
2. Escribís la categoría o género que querés.
3. El sistema corrige los acentos si los escribiste sin tilde (como `"accion"` o `"fantasia"`) y filtra las películas.
4. Te muestra en la terminal la lista con las películas de ese género.
5. Vuelve al menú.

### Flujo Alternativo
* **A1 (Categoría vacía):** Si ponés un género que no existe en la lista, te dice que no hay elementos en esa categoría y vuelve al menú.
