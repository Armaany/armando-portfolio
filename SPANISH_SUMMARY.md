# Resumen en español

## Opportunity Intelligence and Evidence-Assisted Proposal Platform

**Proyecto para un cliente confidencial · Arquitectura, entrega asistida por IA e ingeniería de fiabilidad**

Lideré la arquitectura y entrega de un flujo que conecta la detección de oportunidades públicas con la preparación de una declaración de capacidades revisable y exportable. El trabajo combinó definición de producto, implementación asistida por IA, revisión independiente, pruebas adversariales e integración controlada de dos aplicaciones.

## El problema

Los equipos de desarrollo de negocio y propuestas buscan oportunidades en portales fragmentados, interpretan requisitos y localizan evidencia creíble de experiencia previa. Cada traspaso puede provocar una coincidencia perdida, un registro desactualizado, una afirmación sin sustento o un fallo técnico interpretado como “no se encontró nada”.

## La solución

**Herramienta 1 — Detección de oportunidades.** Adaptadores específicos recopilan y normalizan oportunidades de distintas fuentes públicas. Los términos configurados en inglés y español permiten coincidencias sin depender de mayúsculas ni acentos. El sistema registra la fecha de descubrimiento y las palabras coincidentes mediante un contrato validado de Google Sheets.

**Herramienta 2 — Preparación de propuestas asistida por evidencia.** Un navegador de solo lectura permite buscar, filtrar, ordenar y paginar oportunidades. El usuario puede entender por qué coincidió una oportunidad, seleccionar una, cargar manualmente sus términos de referencia, revisar los requisitos extraídos, recuperar pasajes relevantes de una biblioteca de capacidades y generar un borrador editable con salida DOCX.

## Decisiones de ingeniería

- Validación y escritura por nombre de columna para evitar errores silenciosos cuando cambia el orden de la hoja.
- Separación entre un fallo de fuente y una búsqueda válida sin resultados.
- Uso del texto completo de la fuente para las coincidencias cuando está disponible, sin sobrecargar la interfaz.
- Conservación de evidencia utilizable durante fallos de actualización contemplados.
- Conteos separados para documentos fuente, documentos indexados y fragmentos de búsqueda.

## Forma de trabajo

Convertí los objetivos del producto en contratos y tareas acotadas, utilicé herramientas de IA para acelerar la implementación y revisé el comportamiento resultante de forma independiente. Las pruebas se enfocaron en supuestos de alto riesgo: encabezados reordenados, descripciones largas, escrituras parciales del índice, bibliotecas no disponibles y datos opcionales mal formados.

## Límites actuales

El flujo está entregado, pero los requisitos extraídos, el texto generado y las referencias deben revisarse por una persona. La descarga del ToR sigue siendo manual. La verificación determinista de citas y un producto genérico **Evidence Studio** forman parte de la siguiente etapa. No se presentan métricas no comprobadas de ahorro, adopción, adjudicaciones o impacto comercial.

Contacto: Armando Elizalde · armando21elizalde@gmail.com · [LinkedIn](https://www.linkedin.com/in/elizaltech/)
