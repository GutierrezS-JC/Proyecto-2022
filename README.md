# Proyecto de Software - 2022

**Deploy App pública:** https://grupo26.proyecto2022.linti.unlp.edu.ar/

**Deploy App privada:** https://admin-grupo26.proyecto2022.linti.unlp.edu.ar/

:black_nib: Hecho por Juan Cruz Gutierrez (Pero a que costo)

## Motivacion de proyecto
Todos los años se trata de coordinar el trabajo integrador (TI) de la materia con necesidades y/o demandas de la comunidad. 

Para la cursada 2022, se trabajo en una aplicación que permita gestionar un club barrial. Este trabajo surge ante el pedido del **Club Deportivo Villa Elisa**, quien en 2022 cumplió 100 años desde su fundación.

El trabajo se llevó a cabo en dos (2) etapas, realizando dos aplicaciones con la idea de permitir gestionar y brindar distinta informacion a las personas asociadas del club.

## Aplicacion privada
Por un lado se desarrollo una _aplicacion privada_ en donde se contemplo la siguiente funcionalidad:
  - Gestión de las personas asociadas del club (con alguna funcionalidad para la importación y exportación de datos).
  - Gestión de las disciplinas y/o actividades.
  - Gestión de pagos.
  - Mantener opciones de configuración del sistema.
  - Administración de roles para aplicación privada.

## Aplicacion pública
También se desarrolló una aplicación pública, que permite visualizar la información de interés para la comunidad y personas asociadas al club.
A través de esta aplicación se podrá:
  - Obtener información para establecer contacto con el club.
  - Conocer los precios de las actividades del club y sus disciplinas.
  - Tramitar la credencial digital (No completado)
  - Visualizar estado de cuenta/socio.
  - Registrar la realización de un pago de cuota.

## Herramientas y tecnologias usadas :hammer_and_wrench:
  #### `En frontend` (App Publica)
  - Vue.js
      - Pinia
      - Vuex
      - Vue-router
  - Bootstrap
  - SweetAlert2
  - Chart.js
  - Axios
    
#### `En backend` (App Privada)
- Python
- Flask
    - Flask-SQLAlchemy
    - Flask-Session
    - Flask-WTF
    - Flask-Cors
    - Flask-JWT-Extended
- pdfkit
- Bootstrap y SweetAlert2 (Para la UI de los templates generados en Flask)

---

Espero que les sea de utilidad, sobre todo a aquellos que por algun motivo u otro no llegaron a completar el grupo.

Dentro de cada carpeta (admin - portal) van a poder ver mas informacion sobre cada aplicacon respectivamente ademas de imagenes y gifs sobre el funcionamiento de las aplicaciones.

Por ultimo, entiendan que es un proyecto que fue realizado por distintas circunstancias en forma individual por lo que el codigo puede necesitar una revision (refactoring) ya que estoy seguro que se puede mejorar no solo la legibilidad sino tambien el funcionamiento del mismo. 

**Manaos_**
