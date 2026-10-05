// ===== Configuración: cambia estos datos por los tuyos =====
const CONFIG = {
  email: "erick.david.p@hotmail.com",
  whatsapp: "524461157374", // código de país + número, sin espacios ni "+"
};

const $ = (id) => document.getElementById(id);

// Enlaces de contacto (no todas las páginas tienen todos)
const waUrl = `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent("Hola DAVLI, me interesa cotizar un proyecto.")}`;
if ($("emailLink")) { $("emailLink").textContent = CONFIG.email; $("emailLink").href = `mailto:${CONFIG.email}`; }
if ($("waLink")) $("waLink").href = waUrl;
if ($("waFloat")) $("waFloat").href = waUrl;
if ($("year")) $("year").textContent = new Date().getFullYear();

// Nav: fondo al hacer scroll + menú móvil
const nav = document.getElementById("nav");
const toggle = document.getElementById("navToggle");
const links = document.getElementById("navLinks");

const onScroll = () => nav.classList.toggle("is-scrolled", window.scrollY > 20);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

toggle.addEventListener("click", () => {
  const open = links.classList.toggle("is-open");
  toggle.setAttribute("aria-expanded", open);
});
// Submenú "Servicios": se abre con clic (útil en pantallas táctiles)
document.querySelectorAll(".nav__drop > button").forEach((btn) =>
  btn.addEventListener("click", () => btn.parentElement.classList.toggle("is-open"))
);
document.addEventListener("click", (e) => {
  document.querySelectorAll(".nav__drop.is-open").forEach((d) => { if (!d.contains(e.target)) d.classList.remove("is-open"); });
});

links.querySelectorAll("a").forEach((a) =>
  a.addEventListener("click", () => {
    links.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
  })
);

// Animación al aparecer
const io = new IntersectionObserver(
  (entries) =>
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add("is-visible");
        io.unobserve(e.target);
      }
    }),
  { threshold: 0.12 }
);
document.querySelectorAll(".reveal").forEach((el, i) => {
  el.style.transitionDelay = `${(i % 4) * 80}ms`;
  io.observe(el);
});

// Brillo que sigue al mouse en tarjetas
document.querySelectorAll(".card").forEach((card) =>
  card.addEventListener("mousemove", (e) => {
    const r = card.getBoundingClientRect();
    card.style.setProperty("--mx", `${e.clientX - r.left}px`);
    card.style.setProperty("--my", `${e.clientY - r.top}px`);
  })
);

// Formulario: envía el mensaje directo al correo con FormSubmit (formsubmit.co).
// La primera vez que alguien lo use, FormSubmit manda un correo de activación a CONFIG.email.
const form = $("contactForm");
const status = $("formStatus");
const submitBtn = $("formSubmit");

const setStatus = (type, text) => {
  status.className = `form__status ${type}`;
  status.textContent = text;
};

if (form) form.addEventListener("submit", async (e) => {
  e.preventDefault();
  let valid = true;
  form.querySelectorAll("[required]").forEach((f) => {
    const bad = f.type === "checkbox"
      ? !f.checked
      : !f.value.trim() || (f.type === "email" && !f.checkValidity());
    f.classList.toggle("is-invalid", bad);
    if (bad) valid = false;
  });
  if (!valid) {
    setStatus("err", "Revisa los campos marcados.");
    return;
  }

  const d = Object.fromEntries(new FormData(form));
  if (d._honey) return; // bot

  submitBtn.disabled = true;
  submitBtn.textContent = "Enviando…";
  try {
    const res = await fetch(`https://formsubmit.co/ajax/${CONFIG.email}`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify({
        _subject: `Nuevo proyecto (${d.servicio}) — ${d.nombre}`,
        _replyto: d.correo,
        _template: "table",
        _captcha: "false",
        Nombre: d.nombre,
        Correo: d.correo,
        Servicio: d.servicio,
        Mensaje: d.mensaje,
      }),
    });
    const json = await res.json().catch(() => ({}));
    if (!res.ok || json.success === "false" || json.success === false) throw new Error(json.message || res.status);
    setStatus("ok", "¡Gracias! Recibimos tu mensaje y te responderemos pronto.");
    form.reset();
  } catch {
    setStatus("err", "No se pudo enviar. Escríbenos por WhatsApp o al correo de la izquierda.");
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "Enviar mensaje";
  }
});

// Fondo animado: red de puntos azul/rojo
(() => {
  const canvas = document.getElementById("bg-grid");
  const ctx = canvas.getContext("2d");
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let w, h, pts;

  const init = () => {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = canvas.width = innerWidth * dpr;
    h = canvas.height = innerHeight * dpr;
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    const n = Math.min(70, Math.floor((innerWidth * innerHeight) / 22000));
    pts = Array.from({ length: n }, () => ({
      x: Math.random() * w,
      y: Math.random() * h,
      vx: (Math.random() - 0.5) * 0.25 * dpr,
      vy: (Math.random() - 0.5) * 0.25 * dpr,
      red: Math.random() < 0.12,
    }));
  };

  const draw = () => {
    ctx.clearRect(0, 0, w, h);
    const max = 150 * (w / innerWidth);
    for (let i = 0; i < pts.length; i++) {
      const p = pts[i];
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0 || p.x > w) p.vx *= -1;
      if (p.y < 0 || p.y > h) p.vy *= -1;
      for (let j = i + 1; j < pts.length; j++) {
        const q = pts[j];
        const dist = Math.hypot(p.x - q.x, p.y - q.y);
        if (dist < max) {
          ctx.strokeStyle = `rgba(31,107,255,${0.12 * (1 - dist / max)})`;
          ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke();
        }
      }
      ctx.fillStyle = p.red ? "rgba(255,43,43,.7)" : "rgba(61,139,255,.55)";
      ctx.beginPath(); ctx.arc(p.x, p.y, 1.6 * (w / innerWidth), 0, Math.PI * 2); ctx.fill();
    }
    if (!reduce) requestAnimationFrame(draw);
  };

  init(); draw();
  addEventListener("resize", () => { init(); if (reduce) draw(); });
})();
