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
    ct = base + ("/contact/" if en else "/contatti/"); catp = base + ("/shop/category/" if en else "/negozio/categoria/"); prp = base + ("/shop/" if en else "/negozio/")
    cnt = {}
    for pr in cat["prodotti"]: cnt[pr["categoria"]] = cnt.get(pr["categoria"], 0) + 1
    D = {"cmspush-cat": ("Your website free forever on GitHub Pages", "Il tuo sito gratis per sempre su GitHub Pages"),
         "moduli-wordpress": ("InPost Locker, Redis Cache, Antispam CAPTCHA, AI Copilot, Translate AI", "InPost Locker, Redis Cache, Antispam CAPTCHA, AI Copilot, Translate AI")}
    dflt = ("InPost Locker, Redis Cache and Antispam CAPTCHA", "InPost Locker, Redis Cache e Antispam CAPTCHA")
    def card(href, ic, name, desc, meta):
        return f'<a class="gc-card" href="{href}"><div class="gc-card-b"><div class="gc-card-t">{ic} {name}</div><div class="gc-card-d">{desc}</div><div class="gc-card-m">{meta}</div></div></a>'
    cats = "".join(card(f"{catp}{cid}/", ic, ne if en else n, D.get(cid, dflt)[0 if en else 1],
                        (f"{cnt.get(cid,0)} products" if en else f"{cnt.get(cid,0)} prodotti")) for cid, n, ne, ic in CATS)
    feat = "".join(card(f"{prp}{pid}/", "🚀", n, EN if en else IT, f"€{c/100:.0f}") for pid, n, c in V)
    L = (dict(eb="Scripts, modules and CMS ready to use", h="Scripts ready. Real profits.",
              lead="Tested CMS and modules, already in production, ready to install and go online. One-time payment, no subscription, no surprises.",
              b1="Browse the shop", b2="Contact us",
              w=[("Tested in production", "Every script already runs on real sites."), ("One-time payment", "No subscription, no monthly fees."), ("Your platform", "PrestaShop, WordPress, Magento, OpenCart, Shopify, CS-Cart.")],
              c_eb="What you will find", c_h="Pick your platform", c_l="Modules for the main e-commerce platforms and WordPress, plus the CMS that is free forever on GitHub.",
              f_eb="Featured", f_h="CmsPush: your website, free forever", f_l="Host it on GitHub Pages: no server, no hosting fees. Manage posts, pages and shop from a visual admin in your browser.",
              k_h="Questions? Write to us") if en else
         dict(eb="Script, moduli e CMS pronti all'uso", h="Script pronti. Profitti reali.",
              lead="CMS e moduli testati, già in produzione, pronti da installare e mettere online. Pagamento unico, nessun abbonamento, nessuna sorpresa.",
              b1="Sfoglia lo shop", b2="Contattaci",
              w=[("Testati in produzione", "Ogni script gira già su siti reali."), ("Pagamento unico", "Nessun abbonamento, nessun canone mensile."), ("La tua piattaforma", "PrestaShop, WordPress, Magento, OpenCart, Shopify, CS-Cart.")],
              c_eb="Cosa trovi", c_h="Scegli la tua piattaforma", c_l="Moduli per le principali piattaforme e-commerce e per WordPress, più il CMS gratis per sempre su GitHub.",
              f_eb="In evidenza", f_h="CmsPush: il tuo sito gratis per sempre", f_l="Ospitalo su GitHub Pages: niente server, niente spese di hosting. Gestisci articoli, pagine e shop da un pannello visuale nel browser.",
              k_h="Hai domande? Scrivici"))
    w = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in L["w"])
    hero = f'<div class="gc"><section class="ent-hero"><div class="gc-wrap gc-hero-in"><div><p class="gc-eyebrow">{L["eb"]}</p><h1 class="gc-h1">{L["h"]}</h1><p class="gc-lead">{L["lead"]}</p><div class="gc-act"><a class="gc-btn gc-btn-a" href="{shop}">{L["b1"]}</a><a class="gc-btn gc-btn-o" href="{ct}">{L["b2"]}</a></div></div><div class="ent-cycle">{w}</div></div></section></div>'
    sec_c = f'<div class="gc"><section class="gc-sec gc-soft" id="servizi"><div class="gc-wrap"><p class="gc-eyebrow">{L["c_eb"]}</p><h2 class="gc-h2">{L["c_h"]}</h2><p class="gc-lead">{L["c_l"]}</p><div class="gc-grid">{cats}</div></div></section></div>'
    sec_f = f'<div class="gc"><section class="gc-sec" id="perchi"><div class="gc-wrap"><p class="gc-eyebrow">{L["f_eb"]}</p><h2 class="gc-h2">{L["f_h"]}</h2><p class="gc-lead">{L["f_l"]}</p><div class="gc-grid">{feat}</div></div></section></div>'
    sec_w = f'<div class="gc"><section class="gc-sec gc-soft" id="contesto"><div class="gc-wrap"><div class="ent-stats">{w}</div></div></section></div>'
    sec_k = f'<div class="gc"><section class="gc-sec" id="contatti"><div class="gc-wrap"><h2 class="gc-h2">{L["k_h"]}</h2><p><a class="gc-btn gc-btn-a" href="{ct}">{L["b2"]}</a></p></div></section></div>'
    return {"hero": ("Hero", True, hero), "servizi": ("Categorie", True, sec_c), "perchi": ("In evidenza", True, sec_f), "contesto": ("Perché", True, sec_w), "contatti": ("Contatti", True, sec_k)}
for lang, path in (("it", "_data/blocks_home.json"), ("en", "_data/i18n/en/blocks_home.json")):
    d = home(lang); out = []
    for k in ["hero", "servizi", "perchi", "contesto", "metodo", "avvisi", "contatti"]:
        nome, on, html = d.get(k, (k.capitalize(), False, ""))
        out.append({"id": k, "nome": nome, "enabled": on, "html": html})
    W(path, json.dumps(out, ensure_ascii=False, indent=2))
print("ok")
