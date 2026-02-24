from typing import List, Dict

# 1. Nueva clase Proyecto
class Proyecto:
    def __init__(self, titulo: str, descripcion: str, tecnologias: List[str], imagen: str, link_github: str):
        self.titulo = titulo
        self.descripcion = descripcion
        self.tecnologias = tecnologias
        self.imagen = imagen
        self.link_github = link_github

class Experiencia:
    def __init__(self, puesto: str, empresa: str, periodo: str, logros: List[str], logo: str):
        self.puesto = puesto
        self.empresa = empresa
        self.periodo = periodo
        self.logros = logros
        self.logo = logo

class Certificacion:
    def __init__(self, anio: str, titulo: str, emisor: str, logo: str):
        self.anio = anio
        self.titulo = titulo
        self.emisor = emisor
        self.logo = logo

class CVModelo:
    def obtener_datos(self) -> Dict:
        return {
            "carrusel_hero": [
                "/static/img/gen_1.png",
                "/static/img/gen_3.jpg",
                "https://images.unsplash.com/photo-1537432376769-00f5c2f4c8d2?auto=format&fit=crop&w=1920&q=80"
            ],
            # 2. Agregamos tus proyectos aquí (puedes cambiar las URLs de las imágenes y repositorios)
            "proyectos": [
                Proyecto(
                    "Dashboard de KPIs Industriales", 
                    "Análisis interactivo de producción, OEE y mantenimiento preventivo en tiempo real conectado a bases de datos SQL.", 
                    ["Power BI", "DAX", "SQL"], 
                    "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80", 
                    "https://github.com/RickLS23"
                ),
                Proyecto(
                    "Cotizador de materiales", 
                    "Cotizador de materiales para empresa de maquinados industriales, de acuerdo a los materiales disponibles en el inventario, precios que manejan, dificultad, medidas (mm / pulgadas), tipo de material, etc.", 
                    ["Python", "Pandas", "SAP Scripting"], 
                    "/static/img/cotizador.png", 
                    "https://github.com/RickLS23"
                ),
                Proyecto(
                    "Automatización de Reportes SAP", 
                    "Script automatizado para extracción, limpieza y envío de reportes de materiales (MM) y producción (PP).", 
                    ["Python", "Pandas", "SAP Scripting"], 
                    "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=600&q=80", 
                    "https://github.com/RickLS23"
                ),
                Proyecto(
                    "Bateria Digital", 
                    "Aplicación web para simulación de bateria digital con interfaz gráfica.", 
                    ["Javascript", "HTML", "CSS", "Web Audio API", "Three.js"], 
                    "/static/img/bateria.png", 
                    "https://github.com/RickLS23"
                ),
                Proyecto(
                    "Monitor SCADA en Planta", 
                    "Software de adquisición de datos para monitoreo de sensores en piso de producción con interfaz gráfica.", 
                    ["Python", "Flask", "SQL", "Socket.IO"], 
                    "/static/img/scada.png", 
                    "https://github.com/RickLS23"
                ),
                Proyecto(
                    "Pagina web para Servicios Industriales NOMI S.A. de C.V.", 
                    "Pagina web para empresa de servicios industriales, con información de sus servicios y galería de modelos 3D.", 
                    ["HTML", "CSS", "JavaScript", "PHP"], 
                    "/static/img/nomi.png", 
                    "https://www.nomi.com"
                ), 
                Proyecto(
                    "Pagina web para CAEC Maquinados Industriales S.A. de C.V.", 
                    "Pagina web para empresa de maquinados industriales, con información de sus servicios y galería de imágenes de sus productos.", 
                    ["HTML", "CSS", "JavaScript", "PHP"], 
                    "/static/img/caec.png", 
                    "https://www.industrialcaec.com"
                ),
                Proyecto(
                    "Pagina web para Corporación Industrial de Maquinados HERSA S.A. de C.V.", 
                    "Pagina web estatica con formulario de contacto, información de la empresa y sus servicios.", 
                    ["HTML", "CSS", "JavaScript", "PHP"], 
                    "/static/img/hersa.png", 
                    "https://www.hersamaqui.com"
                ),
                Proyecto(
                    "Indicadores de productividad en OLSA Sistemas de Iluminación Automotriz, S. A. de R.L de C.V.", 
                    "Software de adquisición de datos, dashboards y reportes para monitoreo de KPI's del area de manufactura.", 
                    ["Java", "Spring Boot", "SQL", "PHP", "JavaScript", "HTML", "CSS","SAP","Excel"], 
                    "/static/img/olsa_tm.png", 
                    "https://github.com/RickLS23"
                )
            ],
            "experiencia": [
                Experiencia(
                    "Ingeniero en Sistemas y Manufactura", "HERSA", "Ago 2019 - Ene 2026",
                    ["Integración IT/OT y desarrollo de dashboards con Excel, Power BI y Python.", 
                     "Responsable de la infraestructura de red, telecomunicaciones y mantenimiento de equipos de cómputo tanto hardware como software, licencias y servidores.",
                     "Desarrollo de software interno (cotizador de materiales, generador QR, scripts, operaciones de ingeniería y diseño) utilizando diversas herramientas",
                     "Diseño de piezas complejas en CAD/CAM (SolidWorks).", 
                     "Optimización: Aplicación de Lean Six Sigma en procesos."],
                    "https://ui-avatars.com/api/?name=Hersa&background=0984E3&color=fff&rounded=true"
                ),
                Experiencia(
                    "Ingeniero en Sistemas Jr.", "OLSA (Magna Int.)", "Ago 2018 - Abr 2019",
                    ["Soporte tecnico integral de hardware y software", 
                    "Manejo de plataformas MES / SCADA, ERP y soporte al sistema SAP.", 
                    "Desarrollo de scripts para control de SCRAP (Java, PHP, JS, Python).",
                    "Desarrollo e implementación de una plataforma digital interna para el reporte y manejo de SCRAP, KPI, BOM, programa de producción, Forecast y MPS que a su vez tuviera integración con el sistema ERP de la empresa (SAP)",
                    "Gestión de bases de datos en el servidor, respaldos y configuración."],
                    "https://ui-avatars.com/api/?name=Olsa&background=00CEC9&color=fff&rounded=true"
                )
            ],
            "certificaciones": [
                Certificacion("2026", "Curso SAP ABAP Programación", "Logali Group", "https://logo.clearbit.com/sap.com"),
                Certificacion("2026", "Certificación CAD Design (CSWP)", "Solidworks", "https://logo.clearbit.com/solidworks.com"),
                Certificacion("2025", "CertificaciónGreen Belt Lean Six Sigma", "Variexa Private Training Organization", "https://ui-avatars.com/api/?name=VX&background=FD79A8&color=fff&rounded=true"),
                Certificacion("2025", "Certificación Associate Data Analyst", "DataCamp", "https://logo.clearbit.com/datacamp.com"),
                Certificacion("2026", "Cursos de SAP (PP, FI, MM, PM, HCM)", "Global Tecnologias Academy", "https://logo.clearbit.com/datacamp.com"),
                Certificacion("2025", "Curso de Excel, Project, Power BI", "Global Tecnologias Academy", "https://logo.clearbit.com/datacamp.com"),
                Certificacion("2024", "Certificación Lean T.P.M", "Variexa Private Training Organization", "https://ui-avatars.com/api/?name=VX&background=FD79A8&color=fff&rounded=true"),
                Certificacion("2024", "Certificación Gold Expert (Lean manufacturing)", "Variexa Private Training Organization", "https://ui-avatars.com/api/?name=VX&background=FD79A8&color=fff&rounded=true"),
                Certificacion("2024", "Curso Prompt Engineering", "Cognitive class", "https://logo.clearbit.com/datacamp.com"),
                Certificacion("2023", "Certificación de Soporte de Tecnologias de la Información", "Google y coursera", "https://logo.clearbit.com/datacamp.com")
                ],
            "habilidades_it": ["Python", "Java", "PHP", "SAP (MM, FI, PP)", "SQL", "Power BI", "Redes Cisco", "Soporte tecnico", "Excel", "Kotlin", "Desarrollo web"],
            "habilidades_ot": ["SolidWorks", "Lean Six Sigma", "TPM", "AutoCAD", "PLC / SCADA", "GD&T", "Torno", "Fresadora", "MiniTab" ]
        }