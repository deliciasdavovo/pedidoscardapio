from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Add editorial fonts used only by the opening page.
font_anchor = '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Lora:ital,wght@0,400;0,600;1,400;1,600&family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">'
editorial_font = '<link href="https://fonts.googleapis.com/css2?family=Allura&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">'
if editorial_font not in text:
    text = text.replace(font_anchor, font_anchor + '\n    ' + editorial_font, 1)

# Replace the opening-page styles with a cleaner editorial system.
start = text.index('/* Discovery Overlay */')
end = text.index('/* Transição verde de tela cheia', start)
new_css = r'''/* Discovery Overlay — abertura editorial */
#discovery-overlay {
    position: fixed;
    inset: 0;
    z-index: 60;
    background: #F5F0E7;
    overflow-y: auto;
    transition: opacity 0.42s ease, transform 0.42s ease;
    color: #171913;
}
#discovery-overlay.hiding {
    opacity: 0;
    transform: scale(0.992);
    pointer-events: none;
}
.discovery-shell {
    width: min(100%, 760px);
    min-height: 100%;
    margin: 0 auto;
    padding: 38px 24px 46px;
    display: flex;
    flex-direction: column;
}
.discovery-brand {
    text-align: center;
    margin-bottom: 52px;
}
.discovery-brand-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 16px;
    line-height: 1;
    font-weight: 600;
    letter-spacing: 0.28em;
    text-transform: uppercase;
    color: #173C2D;
}
.discovery-brand-line {
    width: 34px;
    height: 1px;
    margin: 12px auto 9px;
    background: rgba(23, 60, 45, 0.45);
}
.discovery-brand-year {
    font-size: 9px;
    line-height: 1;
    letter-spacing: 0.30em;
    text-transform: uppercase;
    color: rgba(23, 60, 45, 0.68);
}
.discovery-hero {
    margin-bottom: 34px;
}
.discovery-eyebrow {
    margin-bottom: 13px;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: rgba(23, 60, 45, 0.66);
}
.discovery-title {
    margin: 0;
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(52px, 15vw, 82px);
    line-height: 0.82;
    font-weight: 400;
    letter-spacing: -0.045em;
    color: #171913;
}
.discovery-script {
    display: block;
    width: fit-content;
    margin-top: 7px;
    padding-right: 12px;
    font-family: 'Allura', cursive;
    font-size: 1.03em;
    line-height: 0.94;
    letter-spacing: 0;
    color: #1E563D;
    transform: rotate(-1deg);
}
.discovery-copy {
    max-width: 430px;
    margin: 27px 0 0;
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    line-height: 1.65;
    font-weight: 400;
    letter-spacing: -0.01em;
    color: rgba(34, 32, 28, 0.64);
}
.discovery-actions {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 27px;
}
.discovery-cta {
    width: auto;
    min-height: 52px;
    padding: 0 24px;
    border: 1px solid #173C2D;
    border-radius: 999px;
    background: #173C2D;
    color: #F8F4EC;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: -0.01em;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 14px;
    box-shadow: none;
    transition: background 0.18s ease, transform 0.18s ease;
}
.discovery-cta:hover { background: #102F23; transform: translateY(-1px); }
.discovery-cta:active { transform: translateY(0) scale(0.985); }
.discovery-cta i { font-size: 11px; }
.discovery-note {
    margin-left: auto;
    max-width: 136px;
    font-family: 'Cormorant Garamond', serif;
    font-size: 15px;
    font-style: italic;
    line-height: 1.25;
    color: rgba(23, 60, 45, 0.72);
}
.discovery-section-head {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 18px;
    margin: 14px 0 15px;
    padding-top: 24px;
    border-top: 1px solid rgba(23, 60, 45, 0.16);
}
.discovery-section-kicker {
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: rgba(23, 60, 45, 0.58);
}
.discovery-section-title {
    margin-top: 5px;
    font-family: 'Cormorant Garamond', serif;
    font-size: 26px;
    line-height: 1;
    font-weight: 500;
    color: #171913;
}
#discovery-cards {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 10px;
}
.discovery-card {
    position: relative;
    min-height: 150px;
    padding: 18px 16px 16px;
    border: 1px solid rgba(23, 60, 45, 0.10);
    border-radius: 24px;
    background: #EEE5D4;
    overflow: hidden;
    cursor: pointer;
    text-align: left;
    box-shadow: none;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-between;
    transition: transform 0.18s ease, background 0.18s ease, border-color 0.18s ease;
}
.discovery-card::before { display: none; }
.discovery-card:hover {
    transform: translateY(-2px);
    background: #E9DEC9;
    border-color: rgba(23, 60, 45, 0.18);
    box-shadow: none;
}
.discovery-card:active { transform: scale(0.985); }
.discovery-card-wide { grid-column: 1 / -1; min-height: 118px; }
.discovery-card-top {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
}
.discovery-icon {
    width: 38px;
    height: 38px;
    border-radius: 999px;
    border: 1px solid rgba(23, 60, 45, 0.14);
    background: rgba(245, 240, 231, 0.55);
    color: #173C2D;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
}
.discovery-arrow {
    color: rgba(23, 60, 45, 0.70);
    font-size: 11px;
}
.discovery-card-title {
    margin-top: 18px;
    font-family: 'Cormorant Garamond', serif;
    font-size: 22px;
    line-height: 0.98;
    font-weight: 600;
    letter-spacing: -0.025em;
    color: #171913;
}
.discovery-card-copy {
    margin-top: 8px;
    font-family: 'DM Sans', sans-serif;
    font-size: 11.5px;
    line-height: 1.45;
    color: rgba(34, 32, 28, 0.58);
}
.discovery-footer {
    margin-top: 34px;
    padding-top: 19px;
    border-top: 1px solid rgba(23, 60, 45, 0.16);
    text-align: center;
}
.discovery-footer-main {
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 0.28em;
    text-transform: uppercase;
    color: rgba(23, 60, 45, 0.62);
}
.discovery-footer-script {
    margin-top: 4px;
    font-family: 'Cormorant Garamond', serif;
    font-size: 17px;
    font-style: italic;
    color: #173C2D;
}
@media (max-width: 420px) {
    .discovery-shell { padding: 30px 18px 36px; }
    .discovery-brand { margin-bottom: 44px; }
    .discovery-title { font-size: 54px; }
    .discovery-copy { font-size: 14px; }
    .discovery-actions { align-items: flex-start; }
    .discovery-note { max-width: 118px; font-size: 14px; }
    .discovery-card { min-height: 142px; padding: 16px 14px; border-radius: 22px; }
    .discovery-card-wide { min-height: 108px; }
    .discovery-card-title { font-size: 20px; }
    .discovery-card-copy { font-size: 10.5px; }
}

'''
text = text[:start] + new_css + text[end:]

# Replace discovery HTML.
html_pattern = re.compile(r'\s*<!-- Tela de Descoberta -->.*?<!-- Transição verde de tela cheia -->', re.S)
new_html = r'''
    <!-- Tela de Descoberta -->
    <div id="discovery-overlay">
        <div class="discovery-shell">
            <div class="discovery-brand">
                <div class="discovery-brand-name">Delícias da Vovó</div>
                <div class="discovery-brand-line"></div>
                <div class="discovery-brand-year">desde 2005</div>
            </div>

            <section class="discovery-hero">
                <p class="discovery-eyebrow">feito com carinho, todos os dias</p>
                <h1 class="discovery-title">Sabores que <span class="discovery-script">aproximam</span></h1>
                <p class="discovery-copy">Receitas artesanais, preparadas com carinho para o café, para dividir e para transformar pequenos momentos em boas lembranças.</p>
                <div class="discovery-actions">
                    <button onclick="enterMenu()" class="discovery-cta" aria-label="Ver o cardápio completo">
                        Ver cardápio <i class="fas fa-arrow-right"></i>
                    </button>
                    <p class="discovery-note">Mais que comida,<br>são boas lembranças.</p>
                </div>
            </section>

            <div class="discovery-section-head">
                <div>
                    <p class="discovery-section-kicker">nossas delícias</p>
                    <h2 class="discovery-section-title">Escolha por categoria</h2>
                </div>
            </div>

            <div id="discovery-cards"></div>

            <div class="discovery-footer">
                <p class="discovery-footer-main">Delícias da Vovó · Itu</p>
                <p class="discovery-footer-script">feito com carinho desde 2005</p>
            </div>
        </div>
    </div>
    <!-- Transição verde de tela cheia -->'''
text, count = html_pattern.subn(new_html, text, count=1)
if count != 1:
    raise SystemExit(f'Não foi possível trocar o HTML da abertura: {count}')

# Replace discovery card renderer.
render_pattern = re.compile(r'        function renderDiscovery\(\) \{.*?\n        \}\n\n        function showDiscovery', re.S)
new_render = r'''        function renderDiscovery() {
            const container = document.getElementById('discovery-cards');
            if (!container) return;

            const icons = [
                'fa-mug-hot',
                'fa-bread-slice',
                'fa-cake-candles',
                'fa-spoon',
                'fa-gift'
            ];

            container.innerHTML = MACRO_GROUPS.map((group, i) => {
                const isLastOdd = i === MACRO_GROUPS.length - 1 && MACRO_GROUPS.length % 2 !== 0;
                const groupNameAttr = group.name.replace(/'/g, "\\'");
                return `
                    <button type="button" class="discovery-card ${isLastOdd ? 'discovery-card-wide' : ''}" onclick="hideDiscovery('${groupNameAttr}')">
                        <div class="discovery-card-top">
                            <span class="discovery-icon"><i class="fas ${icons[i] || 'fa-utensils'}"></i></span>
                            <i class="fas fa-arrow-right discovery-arrow"></i>
                        </div>
                        <div>
                            <h3 class="discovery-card-title">${group.short || group.name}</h3>
                            <p class="discovery-card-copy">${group.subtitle}</p>
                        </div>
                    </button>`;
            }).join('');
        }

        function showDiscovery'''
text, count = render_pattern.subn(new_render, text, count=1)
if count != 1:
    raise SystemExit(f'Não foi possível trocar renderDiscovery: {count}')

path.write_text(text, encoding='utf-8')
print('Página inicial redesenhada com sucesso.')
