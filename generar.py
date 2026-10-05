"""Genera las páginas del sitio a partir de las piezas en paginas/.

Cada página tiene su contenido en paginas/<nombre>.html; el menú, el pie de página,
los metadatos y el botón de WhatsApp se agregan aquí, en un solo lugar.

Uso:  python generar.py
"""

from pathlib import Path

RAIZ = Path(__file__).parent
URL_BASE = "https://craxker120519.github.io/davli/"  # cambiar al conectar el dominio propio
FECHA = "2026-10-05"

ICONOS = {
    "soporte": '<path d="M3 18v-6a9 9 0 0 1 18 0v6M21 19a2 2 0 0 1-2 2h-1v-6h3zM3 19a2 2 0 0 0 2 2h1v-6H3z"/>',
    "consultoria": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
    "software": '<path d="M8 6 2 12l6 6M16 6l6 6-6 6M14 4l-4 16"/>',
    "redes": '<path d="M12 3v6M5 21v-4h14v4M12 13v4M8 9h8v4H8z"/>',
    "ciberseguridad": '<path d="M12 3 4 6v6c0 5 3.4 8.3 8 9 4.6-.7 8-4 8-9V6l-8-3z"/><path d="m9 12 2 2 4-4"/>',
    "servidores": '<rect x="4" y="3" width="16" height="7" rx="1.5"/><rect x="4" y="14" width="16" height="7" rx="1.5"/><path d="M8 6.5h.01M8 17.5h.01"/>',
    "equipos": '<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M8 20h8M12 16v4"/>',
}

SERVICIOS = [
    ("software.html", "software", "Software y automatización"),
    ("servidores.html", "servidores", "Infraestructura y servidores"),
    ("redes.html", "redes", "Redes y conectividad"),
    ("ciberseguridad.html", "ciberseguridad", "Ciberseguridad"),
    ("soporte.html", "soporte", "Soporte y administración TI"),
    ("consultoria.html", "consultoria", "Consultoría y proyectos"),
    ("equipos.html", "equipos", "Venta de equipo"),
]

# archivo -> (título de la pestaña, descripción, prioridad en sitemap)
PAGINAS = {
    "index.html": ("DAVLI | Soluciones tecnológicas integrales",
                   "Software a la medida, redes y cableado estructurado, ciberseguridad, administración de servidores y venta de equipo. Ingenieros que planean, documentan y entregan trabajo de calidad.", "1.0"),
    "software.html": ("Software y automatización | DAVLI",
                      "Desarrollo de software a la medida, páginas web, integraciones y automatización de procesos para su empresa.", "0.9"),
    "redes.html": ("Redes y conectividad | DAVLI",
                   "Cableado estructurado certificado y documentado, redes con Cisco, Ubiquiti, UniFi, MikroTik y Fortinet, Wi-Fi empresarial y enlaces.", "0.9"),
    "ciberseguridad.html": ("Ciberseguridad para empresas | DAVLI",
                            "Firewalls Palo Alto y Fortinet, VPN, segmentación, auditorías, respaldos y protección contra ransomware.", "0.9"),
    "servidores.html": ("Infraestructura y servidores | DAVLI",
                        "Instalación y administración de servidores Windows y Linux, virtualización, almacenamiento, respaldos y monitoreo.", "0.9"),
    "soporte.html": ("Soporte y administración TI | DAVLI",
                     "Mesa de ayuda, pólizas de soporte, mantenimiento preventivo y administración de usuarios y equipos para su empresa.", "0.9"),
    "consultoria.html": ("Consultoría y proyectos de TI | DAVLI",
                         "Diagnóstico tecnológico, planeación, gestión de proyectos, migraciones y documentación de infraestructura.", "0.9"),
    "equipos.html": ("Venta de equipo de cómputo y redes a medida | DAVLI",
                     "Computadoras, servidores, switches, access points, firewalls y UPS dimensionados de acuerdo con su necesidad real.", "0.8"),
    "proyectos.html": ("Proyectos | DAVLI",
                       "Sistemas que hemos desarrollado: control de reparaciones, ERP, cotizador, automatización y gestión de flotilla.", "0.8"),
    "nosotros.html": ("Nosotros | DAVLI",
                      "Más de 8 años de experiencia en soluciones tecnológicas para empresas. Ingenieros que planean, documentan y entregan trabajo de calidad.", "0.7"),
    "contacto.html": ("Contacto | DAVLI",
                      "Compártanos su proyecto de software, redes, seguridad o servidores y le enviaremos una propuesta.", "0.8"),
    "aviso-privacidad.html": ("Aviso de privacidad | DAVLI",
                              "Aviso de privacidad de DAVLI: tratamiento de los datos personales que usted nos proporciona.", "0.3"),
}


def icono(nombre):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONOS[nombre]}</svg>'


def actual(pagina, archivo):
    return ' aria-current="page"' if pagina == archivo else ""


def encabezado(pagina):
    en_servicios = any(pagina == a for a, _, _ in SERVICIOS)
    submenu = "\n".join(
        f'            <a href="{a}"{actual(pagina, a)}>{icono(i)}{t}</a>' for a, i, t in SERVICIOS
    )
    return f"""  <header class="nav" id="nav">
    <div class="container nav__inner">
      <a href="./" class="nav__brand" aria-label="DAVLI inicio">
        <img src="assets/rabbit.webp" alt="" width="40" height="36">
        <span>DAVLI</span>
      </a>
      <button class="nav__toggle" id="navToggle" aria-label="Abrir menú" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
      <nav class="nav__links" id="navLinks">
        <a href="./"{actual(pagina, "index.html")}>Inicio</a>
        <div class="nav__drop{" is-active" if en_servicios else ""}">
          <button type="button" aria-haspopup="true">Servicios</button>
          <div class="nav__menu">
{submenu}
          </div>
        </div>
        <a href="proyectos.html"{actual(pagina, "proyectos.html")}>Proyectos</a>
        <a href="nosotros.html"{actual(pagina, "nosotros.html")}>Nosotros</a>
        <a href="contacto.html" class="btn btn--sm btn--primary">Cotizar proyecto</a>
      </nav>
    </div>
  </header>"""


def pie():
    servicios = "\n".join(f'          <li><a href="{a}">{t}</a></li>' for a, _, t in SERVICIOS)
    return f"""  <footer class="footer">
    <div class="container footer__grid">
      <div>
        <a href="./" class="nav__brand">
          <img src="assets/rabbit.webp" alt="" width="32" height="28">
          <span>DAVLI</span>
        </a>
        <p class="muted small footer__tag">Soluciones tecnológicas integrales. Una sola empresa para toda su tecnología.</p>
      </div>
      <div>
        <h4>Servicios</h4>
        <ul>
{servicios}
        </ul>
      </div>
      <div>
        <h4>DAVLI</h4>
        <ul>
          <li><a href="proyectos.html">Proyectos</a></li>
          <li><a href="nosotros.html">Nosotros</a></li>
          <li><a href="contacto.html">Contacto</a></li>
          <li><a href="aviso-privacidad.html">Aviso de privacidad</a></li>
        </ul>
      </div>
      <div>
        <h4>Contacto</h4>
        <ul>
          <li><a href="mailto:erick.david.p@hotmail.com">erick.david.p@hotmail.com</a></li>
          <li><a href="https://wa.me/524461157374" target="_blank" rel="noopener">WhatsApp: 446 115 7374</a></li>
          <li><a href="tel:+524461157374">Tel: 446 115 7374</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer__bottom">
      <p class="muted small">© <span id="year">2026</span> DAVLI. Todos los derechos reservados.</p>
      <p class="muted small">Soluciones <span class="dot dot--blue"></span> Tecnológicas <span class="dot dot--red"></span> Integrales</p>
    </div>
  </footer>

  <a class="wa-float" id="waFloat" href="https://wa.me/524461157374" target="_blank" rel="noopener" aria-label="Contáctenos por WhatsApp">
    <svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C9 3 3.3 8.6 3.3 15.6c0 2.4.7 4.7 1.9 6.7L3 29l6.9-2.1c1.9 1 4 1.6 6.1 1.6 7 0 12.7-5.6 12.7-12.6S23 3 16 3zm0 23.1c-1.9 0-3.8-.5-5.4-1.5l-.4-.2-4.1 1.2 1.3-4-.3-.4c-1.1-1.7-1.7-3.6-1.7-5.6C5.4 9.8 10.2 5.1 16 5.1s10.6 4.7 10.6 10.5S21.8 26.1 16 26.1zm5.8-7.8c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1c-.3-.2-1.3-.5-2.5-1.5-.9-.8-1.6-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.5-.6c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4s-1.2 1.1-1.2 2.7 1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.7 5 .8.3 1.4.5 1.9.7.8.2 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>
  </a>"""


def pagina_completa(archivo, contenido):
    titulo, descripcion, _ = PAGINAS[archivo]
    url = URL_BASE + ("" if archivo == "index.html" else archivo)
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{titulo}</title>
  <meta name="description" content="{descripcion}">
  <meta name="theme-color" content="#01070e">
  <link rel="canonical" href="{url}">
  <link rel="icon" type="image/png" href="assets/favicon.png">
  <link rel="apple-touch-icon" href="assets/favicon.png">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_MX">
  <meta property="og:site_name" content="DAVLI">
  <meta property="og:title" content="{titulo}">
  <meta property="og:description" content="{descripcion}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{URL_BASE}assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Michroma&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <!-- Archivo generado por generar.py a partir de paginas/{archivo}. Edita la pieza, no este archivo. -->
  <canvas id="bg-grid" aria-hidden="true"></canvas>

{encabezado(archivo)}

  <main>
{contenido.rstrip()}
  </main>

{pie()}

  <script src="js/main.js"></script>
</body>
</html>
"""


def sitemap():
    urls = "\n".join(
        f"  <url>\n    <loc>{URL_BASE}{'' if a == 'index.html' else a}</loc>\n    <lastmod>{FECHA}</lastmod>\n    <priority>{p}</priority>\n  </url>"
        for a, (_, _, p) in PAGINAS.items()
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n'


def main():
    for archivo in PAGINAS:
        contenido = (RAIZ / "paginas" / archivo).read_text(encoding="utf-8")
        (RAIZ / archivo).write_text(pagina_completa(archivo, contenido), encoding="utf-8", newline="\n")
        print("generada:", archivo)
    (RAIZ / "sitemap.xml").write_text(sitemap(), encoding="utf-8", newline="\n")
    (RAIZ / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {URL_BASE}sitemap.xml\n", encoding="utf-8", newline="\n")
    print("generados: sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
