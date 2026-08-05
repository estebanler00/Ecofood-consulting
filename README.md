# Ecofood-consulting
Proyecto clase 12,13 y 14. Analisis de datos para EcoFoods, empresa de alimentacion saludable.

Objetivo comercial de EcoFoods: lanzar una nueva línea de productos alimenticios sostenibles en Buenos Aires. 

Objetivos previos al objetivo principal: comprensión de cómo está evolucionando el mercado, qué productos tienen mayor potencial, qué características valoran los consumidores y qué oportunidades existen para diferenciarse frente a la competencia.

Fuente de datos: DB pública de CABA (data.buenosaires.gob.ar/dataset/oferta-establecimientos-gastronomicos). Google Trends. Reseñas de Google Maps.

Metodología:
Extracción: Descarga de base de datos pública, extracción via API Pública (Pytrends) y web scrapping via codigó de creación de bot de scrapping.
Limpieza: Detección de valores nulos o no válidos, descarte de los mismos. Rectificación de tipo de dato de cada base de dato recolectada.
EDA: Análisis de los datos. Comparaciones entre categorias, media de búsqueda de Google y división de opiniones negativas y positivas.
Visualización: Creación de gráficos representativos de cada análisis via Matplot

Principales hallazgos:

El tipo de cocina más solicitada son las minutas.
"SIN TACC" tiene una gran popularidad de búsqueda en Google, teniendo una tendencia creciente y estando cerca de su pico máximo de búsquedas casi constantemente.


Recomendaciones: Inversión segura en local de minutas, incluir opciones sin TACC. Otra posibilidad de inversión en un local: cafeteria de especialidad, opciones sin TACC y saludables, zonas Palermo, y polos gastronómicos como Plaza Arenales, V.Devoto.
