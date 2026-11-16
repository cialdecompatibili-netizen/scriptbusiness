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
V = [("cmspush", "CmsPush", 1900), ("cmspushaccademy", "CmsPush Accademy", 2900)]

cat = {"_nota": "Catalogo ScriptBusiness (prezzi in CENTESIMI). Generato da automation/genera_scriptbusiness.py.",
       "categorie": [{"nome": "CmsPush", "id": "cmspush-cat", "icona": "🚀", "tr": {"en": {"nome": "CmsPush"}}}], "prodotti": []}
for pid, nome, cent in V:
    fi = IT + "\n" + "\n".join("✓ " + b for b in BI) + "\nDemo: " + DEMO
    fe = EN + "\n" + "\n".join("✓ " + b for b in BE) + "\nDemo: " + DEMO
    cat["prodotti"].append({"tipo": "digitale", "id": pid, "nome": nome, "categoria": "cmspush-cat", "prezzo_centesimi": cent,
        "descrizione": IT, "descrizione_completa": fi, "immagine": "", "icona": "🚀", "visibile": True,
        "tr": {"en": {"nome": nome, "descrizione": EN, "descrizione_completa": fe}}})
W("_data/catalogo.json", json.dumps(cat, ensure_ascii=False, indent=2))
W("_data/shop-categorie.json", json.dumps([{"nome": "cmspush-cat", "slug": "cmspush-cat"}], indent=2))

# pagine: via gli esempi e i vecchi file generati
for f in (glob.glob(os.path.join(R, "_negozio", "*.md")) + glob.glob(os.path.join(R, "en", "negozio", "*.md")) + glob.glob(os.path.join(R, "en", "negozio", "categoria", "*.md"))):
    os.remove(f)
for pid, nome, cent in V:
    W(f"_negozio/{pid}.md", f'---\nlayout: negozio-prodotto\ntitle: "{nome}"\npid: {pid}\npermalink: /negozio/{pid}/\ndescription: "{IT[:150]}"\nref: shop-prod-{pid}\n---\n')
    W(f"en/negozio/{pid}.md", f'---\nlayout: negozio-prodotto\ntitle: "{nome}"\npid: {pid}\npermalink: /en/shop/{pid}/\ndescription: "{EN[:150]}"\nlang: en\nlocale: en\nref: shop-prod-{pid}\ntr: tradotto\n---\n')
W("_negozio/categoria-cmspush.md", '---\nlayout: negozio-categoria\ntitle: "CmsPush"\ncid: cmspush-cat\npermalink: /negozio/categoria/cmspush-cat/\ndescription: "CmsPush: sito gratis per sempre su GitHub"\nref: shop-cat-cmspush-cat\n---\n')
W("en/negozio/categoria/cmspush-cat.md", '---\nlayout: negozio-categoria\ntitle: "CmsPush"\ncid: cmspush-cat\npermalink: /en/shop/category/cmspush-cat/\ndescription: "CmsPush: free website forever on GitHub"\nlang: en\nlocale: en\nref: shop-cat-cmspush-cat\ntr: tradotto\n---\n')

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
