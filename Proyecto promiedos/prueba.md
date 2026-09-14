# Casos de Uso del Sistema

## Caso de Uso 1: Buscar película por título

* **Quién lo usa:** El usuario.
* **Para qué sirve:** Para buscar películas escribiendo el nombre completo o solo una parte sin tener que poner el título completo.
* **Qué se necesita antes:** Que las películas estén cargadas en el sistema.

### Pasos
1. Ponés el número **1** en el menú.
2. Escribís una palabra (por ejemplo: `"El"` o `"batalla"`).
3. El programa se fija cuáles películas tienen esa palabra en el nombre y junta todas las que encuentra.
4. Te muestra la lista de esas películas en la pantalla.
5. Vuelve al menú principal.

### Si algo sale distinto
* **No encuentra nada:** Si la palabra que pusiste no está en ninguna película, te avisa con un mensaje y te devuelve al menú.

---

## Caso de Uso 2: Mostrar todas las películas

* **Quién lo usa:** El usuario.
* **Para qué sirve:** Para ver la lista completa de películas que hay guardadas.
* **Qué se necesita antes:** Tener la aplicación abierta.

### Pasos
1. Ponés el número **2** en el menú.
2. El programa busca todo el listado de películas.
3. Te las va mostrando una por una en la pantalla.
4. Vuelve al menú principal.

---

## Caso de Uso 3: Filtrar por categoría

* **Quién lo usa:** El usuario.
* **Para qué sirve:** Para ver únicamente las películas de un tipo o género (como Acción o Fantasía).
* **Qué se necesita antes:** Que existan películas guardadas en el sistema.

### Pasos
1. Ponés el número **3** en el menú.
2. Escribís el tipo de película que querés ver.
3. El programa arregla si te olvidaste de ponerle tilde a la palabra (como escribir `"accion"` sin acento) y busca las que coinciden.
4. Te muestra en pantalla las películas de ese tipo.
5. Vuelve al menú principal.

### Si algo sale distinto
* **Categoría sin películas:** Si escribís un género que no tiene películas, te avisa que no hay nada en esa categoría y vuelve al menú.
