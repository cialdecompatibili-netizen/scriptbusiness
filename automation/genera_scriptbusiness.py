# -*- coding: utf-8 -*-
# Genera catalogo, pagine _negozio (IT+EN), categorie shop e blocchi home di ScriptBusiness.
# Prodotto unico CmsPush in 3 varianti (nomi/prezzi/differenze da decidere: modificare qui e rilanciare).
import json, os, glob
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def W(p, s):
    p = os.path.join(R, p); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8', newline='\n').write(s)

DEMO = "https://cialdecompatibili-netizen.github.io/cmspush2/"
IT = "CMS admin per Jekyll e GitHub Pages: il tuo sito gratis per sempre, ospitato su GitHub. Gestisci articoli, pagine e shop direttamente dal browser. Zero server, zero spese di hosting."
EN = "Admin CMS for Jekyll and GitHub Pages: your website free forever, hosted on GitHub. Manage posts, pages and shop right from the browser. No server, no hosting costs."
BI = ["Sito gratis per sempre su GitHub Pages", "Admin panel visuale nel browser", "Blog + Shop integrati", "Aggiornamenti automatici inclusi", "Zero server, zero spese di hosting"]
BE = ["Website free forever on GitHub Pages", "Visual admin panel in the browser", "Blog + Shop built in", "Automatic updates included", "No server, no hosting costs"]
# id, nome, prezzo in centesimi
V = [("cmspush", "CmsPush", 1900), ("cmspushacademy", "CmsPush Academy", 1900)]

CATS = [("cmspush-cat", "CmsPush", "CmsPush", "🚀"),
        ("moduli-prestashop", "Moduli PrestaShop", "PrestaShop modules", "🛒"),
        ("moduli-wordpress", "Moduli WordPress", "WordPress modules", "📝"),
        ("moduli-magento", "Moduli Magento 2", "Magento 2 modules", "🧱"),
        ("moduli-opencart", "Moduli OpenCart", "OpenCart modules", "🛍️"),
        ("moduli-shopify", "Moduli Shopify", "Shopify modules", "🏪"),
        ("moduli-cscart", "Moduli CS-Cart", "CS-Cart modules", "🧩")]

cat = {"_nota": "Catalogo ScriptBusiness (prezzi in CENTESIMI). Generato da automation/genera_scriptbusiness.py.",
       "categorie": [{"nome": n, "id": i, "icona": ic, "tr": {"en": {"nome": ne}}} for i, n, ne, ic in CATS], "prodotti": []}
for pid, nome, cent in V:
    fi = IT + "\n" + "\n".join("✓ " + b for b in BI) + "\nDemo: " + DEMO
    fe = EN + "\n" + "\n".join("✓ " + b for b in BE) + "\nDemo: " + DEMO
    cat["prodotti"].append({"tipo": "digitale", "id": pid, "nome": nome, "categoria": "cmspush-cat", "prezzo_centesimi": cent,
        "descrizione": IT, "descrizione_completa": fi, "immagine": "", "icona": "🚀", "visibile": True,
        "tr": {"en": {"nome": nome, "descrizione": EN, "descrizione_completa": fe}}})

# ---- Moduli per piattaforma (testi e prezzi dal sito originale scriptbusiness.shop)
PLAT = [("cscart", "CS-Cart", "moduli-cscart"), ("magento", "Magento 2", "moduli-magento"), ("opencart", "OpenCart", "moduli-opencart"),
        ("prestashop", "PrestaShop", "moduli-prestashop"), ("shopify", "Shopify", "moduli-shopify"), ("woocommerce", "WooCommerce", "moduli-wordpress")]
PRZ = {"inpost-locker": [5990, 8990, 3990, 4990, 6990, 4490], "redis-cache": [4490, 6990, 2990, 3990, 4990, 3490], "antispam-captcha": [2990, 3990, 1990, 2490, 2990, 1990]}
NM = {"inpost-locker": ("InPost Locker", "InPost Locker", "📦"), "redis-cache": ("Redis Cache", "Redis Cache", "⚡"), "antispam-captcha": ("Antispam CAPTCHA", "Antispam CAPTCHA", "🛡️")}
def txt(mod, plat, en):
    if mod == "inpost-locker":
        if en: return f"InPost locker map in {plat} checkout, active right away: no paid business API required, unlike the official free module too. Stable, no forced branding."
        return f"Mappa locker InPost nel checkout {plat}, attiva da subito: nessuna API business a pagamento richiesta, a differenza anche del modulo gratuito ufficiale. Stabile, senza branding forzato."
    if mod == "redis-cache":
        if en: return f"Redis cache for {plat}, ready in minutes: one-time payment, no monthly subscription. The most popular enterprise version for WordPress costs $95/month recurring - here you pay once. Fewer database queries, faster pages."
        return f"Cache Redis per {plat}, pronta in pochi minuti: pagamento unico, nessun abbonamento mensile. La versione enterprise più diffusa per WordPress costa 95$/mese in ricorrenza - qui paghi una volta sola. Riduce le query al database e velocizza le pagine."
    if en: return f"Block spam and bots on {plat} with Google reCAPTCHA, the engine customers already know and trust. One-time payment, no subscription: since late 2025 reCAPTCHA is free only up to 10,000 checks/month."
    return f"Blocca spam e bot su {plat} con Google reCAPTCHA, il motore che i clienti già conoscono e di cui si fidano. Pagamento unico, nessun abbonamento: da fine 2025 reCAPTCHA è gratis solo fino a 10.000 verifiche/mese."
X = []  # (id, nome_it, nome_en, cat, cent, it, en, icona)
for mod in PRZ:
    for (sl, plat, cid), cent in zip(PLAT, PRZ[mod]):
        n = NM[mod]
        X.append((f"{mod}-{sl}", f"{n[0]} per {plat}", f"{n[1]} for {plat}", cid, cent, txt(mod, plat, False), txt(mod, plat, True), n[2]))
X += [("wordpress-ai-copilot", "WordPress AI Copilot", "WordPress AI Copilot", "moduli-wordpress", 2490,
       "Collega WordPress a un assistente AI e pilota il sito scrivendo in chat: articoli, pagine, media e menu senza aprire la bacheca. Installazione in due minuti, licenza una tantum.",
       "Connect WordPress to an AI assistant and run the site by chatting: posts, pages, media and menus without opening the dashboard. Two-minute setup, one-time license.", "✨"),
      ("wp-translate-ai", "WP Translate AI", "WP Translate AI", "moduli-wordpress", 2490,
       "Plugin WordPress leggero per siti multilingua, con traduzione automatica via API AI (chiave tua, nessun credito proprietario). Alternativa a WPML senza abbonamento fisso.",
       "Lightweight WordPress plugin for multilingual sites, with automatic translation via AI API (your own key, no proprietary credits). A WPML alternative with no fixed subscription.", "🌍")]
for pid, ni, ne, c, cent, ti, te, ic in X:
    cat["prodotti"].append({"tipo": "digitale", "id": pid, "nome": ni, "categoria": c, "prezzo_centesimi": cent, "descrizione": ti,
        "descrizione_completa": ti, "immagine": "", "icona": ic, "visibile": True, "tr": {"en": {"nome": ne, "descrizione": te, "descrizione_completa": te}}})

W("_data/catalogo.json", json.dumps(cat, ensure_ascii=False, indent=2))
W("_data/shop-categorie.json", json.dumps([{"nome": i, "slug": i} for i, n, ne, ic in CATS], indent=2))

# pagine: via gli esempi e i vecchi file generati
for f in (glob.glob(os.path.join(R, "_negozio", "*.md")) + glob.glob(os.path.join(R, "en", "negozio", "*.md")) + glob.glob(os.path.join(R, "en", "negozio", "categoria", "*.md"))):
    os.remove(f)
for pid, nome, cent in V:
    W(f"_negozio/{pid}.md", f'---\nlayout: negozio-prodotto\ntitle: "{nome}"\npid: {pid}\npermalink: /negozio/{pid}/\ndescription: "{IT[:150]}"\nref: shop-prod-{pid}\n---\n')
    W(f"en/negozio/{pid}.md", f'---\nlayout: negozio-prodotto\ntitle: "{nome}"\npid: {pid}\npermalink: /en/shop/{pid}/\ndescription: "{EN[:150]}"\nlang: en\nlocale: en\nref: shop-prod-{pid}\ntr: tradotto\n---\n')

for i, n, ne, ic in CATS:
    W(f"_negozio/categoria-{i}.md", f'---\nlayout: negozio-categoria\ntitle: "{n}"\ncid: {i}\npermalink: /negozio/categoria/{i}/\ndescription: "{n} ScriptBusiness"\nref: shop-cat-{i}\n---\n')
    W(f"en/negozio/categoria/{i}.md", f'---\nlayout: negozio-categoria\ntitle: "{ne}"\ncid: {i}\npermalink: /en/shop/category/{i}/\ndescription: "{ne} ScriptBusiness"\nlang: en\nlocale: en\nref: shop-cat-{i}\ntr: tradotto\n---\n')

for pid, ni, ne, c, cent, ti, te, ic in X:
    W(f"_negozio/{pid}.md", f'---\nlayout: negozio-prodotto\ntitle: "{ni}"\npid: {pid}\npermalink: /negozio/{pid}/\ndescription: "{ti[:150]}"\nref: shop-prod-{pid}\n---\n')
    W(f"en/negozio/{pid}.md", f'---\nlayout: negozio-prodotto\ntitle: "{ne}"\npid: {pid}\npermalink: /en/shop/{pid}/\ndescription: "{te[:150]}"\nlang: en\nlocale: en\nref: shop-prod-{pid}\ntr: tradotto\n---\n')

def home(lang):
    en = lang == "en"; base = "__BASEURL__/en" if en else "__BASEURL__"; shop = base + ("/shop/" if en else "/negozio/")
    ct = base + ("/contact/" if en else "/contatti/")
    t = (("Free website, forever", "Your website. Free forever.", "Host it on GitHub Pages: no server, no hosting fees, no surprises. Manage posts, pages and shop from a visual admin in your browser.", "Get CmsPush", "Contact us",
          [("Free forever", "Hosted on GitHub Pages at zero cost."), ("Admin in the browser", "Posts, pages and shop without touching code."), ("Blog + Shop", "Sell and publish from the same site.")], "Choose your version", "Questions? Write to us") if en else
         ("Sito gratis per sempre", "Il tuo sito. Gratis per sempre.", "Ospitalo su GitHub Pages: niente server, niente spese di hosting, nessuna sorpresa. Gestisci articoli, pagine e shop da un pannello visuale nel browser.", "Scopri CmsPush", "Contattaci",
          [("Gratis per sempre", "Ospitato su GitHub Pages a costo zero."), ("Admin nel browser", "Articoli, pagine e shop senza toccare il codice."), ("Blog + Shop", "Pubblichi e vendi dallo stesso sito.")], "Scegli la tua versione", "Hai domande? Scrivici"))
    cards = '<div class="gc-grid">' + "".join(
        f'<a class="gc-card" href="{shop}{pid}/"><div class="gc-card-b"><div class="gc-card-t">🚀 {n}</div><div class="gc-card-d">{EN if en else IT}</div><div class="gc-card-m">€{c/100:.2f}</div></div></a>'.replace(".00", "") for pid, n, c in V) + "</div>"
    w = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in t[5])
    hero = f'<div class="gc"><section class="ent-hero"><div class="gc-wrap gc-hero-in"><div><p class="gc-eyebrow">{t[0]}</p><h1 class="gc-h1">{t[1]}</h1><p class="gc-lead">{t[2]}</p><div class="gc-act"><a class="gc-btn gc-btn-a" href="{shop}">{t[3]}</a><a class="gc-btn gc-btn-o" href="{ct}">{t[4]}</a></div></div><div class="ent-cycle">{w}</div></div></section></div>'
    scr = f'<div class="gc"><section class="gc-sec gc-soft" id="servizi"><div class="gc-wrap"><h2 class="gc-h2">{t[6]}</h2>{cards}</div></section></div>'
    ctb = f'<div class="gc"><section class="gc-sec" id="contatti"><div class="gc-wrap"><h2 class="gc-h2">{t[7]}</h2><p><a class="gc-btn gc-btn-a" href="{ct}">{t[4]}</a></p></div></section></div>'
    return {"hero": ("Hero", True, hero), "servizi": ("Versioni", True, scr), "contatti": ("Contatti", True, ctb)}
for lang, path in (("it", "_data/blocks_home.json"), ("en", "_data/i18n/en/blocks_home.json")):
    d = home(lang); out = []
    for k in ["hero", "contesto", "servizi", "perchi", "metodo", "avvisi", "contatti"]:
        nome, en_, html = d.get(k, (k.capitalize(), False, ""))
        out.append({"id": k, "nome": nome, "enabled": en_, "html": html})
    W(path, json.dumps(out, ensure_ascii=False, indent=2))
print("ok")
