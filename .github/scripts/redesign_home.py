from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Volta para as fontes originais do site.
editorial_font = '<link href="https://fonts.googleapis.com/css2?family=Allura&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">'
text = text.replace('\n    ' + editorial_font, '', 1)
text = text.replace(editorial_font + '\n', '', 1)

# Abertura compacta: sem rolagem, usando apenas Lora + Libre Caslon + DM Sans.
start = text.index('/* Discovery Overlay')
end = text.index('/* Transição verde de tela cheia', start)
new_css = r'''/* Discovery Overlay — abertura compacta */
#discovery-overlay {
    position: fixed;
    inset: 0;
    z-index: 60;
    background: #F5F0E7;
    overflow: hidden;
    color: #22201C;
    transition: opacity 0.38s ease, transform 0.38s ease;
}
#discovery-overlay.hiding {
    opacity: 0;
    transform: scale(0.995);
    pointer-events: none;
}
.discovery-shell {
    width: min(100%, 560px);
    height: 100vh;
    height: 100dvh;
    margin: 0 auto;
    padding: max(24px, env(safe-area-inset-top)) 22px max(22px, env(safe-area-inset-bottom));
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.discovery-brand {
    text-align: center;
    margin-bottom: clamp(20px, 4.2vh, 34px);
}
.discovery-brand-name {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    line-height: 1;
    font-weight: 700;
    letter-spacing: 0.34em;
    text-transform: uppercase;
    color: #2C4A34;
}
.discovery-brand-line {
    width: 36px;
    height: 1px;
    margin: 11px auto 0;
    background: rgba(44, 74, 52, 0.52);
}
.discovery-hero {
    text-align: center;
    margin-bottom: clamp(18px, 3.8vh, 30px);
}
.discovery-title {
    margin: 0;
    font-family: 'Lora', serif;
    font-size: clamp(34px, 9.6vw, 48px);
    line-height: 1.03;
    font-weight: 400;
    letter-spacing: -0.035em;
    color: #22201C;
}
.discovery-title em {
    display: inline;
    font-family: 'Libre Caslon Text', serif;
    font-weight: 400;
    font-style: italic;
    color: #2C4A34;
}
.discovery-subtitle {
    margin: 12px auto 0;
    max-width: 330px;
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    line-height: 1.45;
    color: rgba(34, 32, 28, 0.52);
}
.discovery-section-label {
    margin: 0 0 10px;
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.20em;
    text-transform: uppercase;
    color: rgba(44, 74, 52, 0.62);
    text-align: center;
}
#discovery-cards {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 9px;
}
.discovery-card {
    min-height: clamp(58px, 8.8vh, 72px);
    padding: 0 15px;
    border: 1px solid rgba(44, 74, 52, 0.12);
    border-radius: 16px;
    background: #EEE5D4;
    color: #22201C;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    text-align: left;
    box-shadow: none;
    transition: background 0.18s ease, transform 0.18s ease, border-color 0.18s ease;
}
.discovery-card::before { display: none; }
.discovery-card:hover {
    transform: translateY(-1px);
    background: #E9DEC9;
    border-color: rgba(44, 74, 52, 0.20);
    box-shadow: none;
}
.discovery-card:active { transform: scale(0.985); }
.discovery-card-wide { grid-column: 1 / -1; }
.discovery-card-title {
    font-family: 'Lora', serif;
    font-size: clamp(14px, 4vw, 17px);
    line-height: 1.12;
    font-weight: 400;
    letter-spacing: -0.02em;
}
.discovery-arrow {
    flex: 0 0 auto;
    color: #2C4A34;
    font-size: 10px;
    opacity: 0.74;
}
.discovery-cta {
    width: 100%;
    min-height: clamp(50px, 7.5vh, 58px);
    margin-top: 11px;
    padding: 0 20px;
    border: 1px solid #2C4A34;
    border-radius: 16px;
    background: #2C4A34;
    color: #F5F0E7;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 650;
    letter-spacing: -0.01em;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    box-shadow: none;
    transition: background 0.18s ease, transform 0.18s ease;
}
.discovery-cta:hover { background: #20361F; }
.discovery-cta:active { transform: scale(0.985); }
.discovery-cta i { font-size: 10px; }
.discovery-footnote {
    margin-top: clamp(12px, 2.2vh, 18px);
    text-align: center;
    font-family: 'Libre Caslon Text', serif;
    font-size: 12px;
    font-style: italic;
    color: rgba(44, 74, 52, 0.58);
}
@media (max-height: 700px) {
    .discovery-shell { padding-top: 18px; padding-bottom: 18px; }
    .discovery-brand { margin-bottom: 16px; }
    .discovery-hero { margin-bottom: 14px; }
    .discovery-title { font-size: 32px; }
    .discovery-subtitle { margin-top: 8px; font-size: 11px; }
    .discovery-section-label { margin-bottom: 8px; }
    #discovery-cards { gap: 7px; }
    .discovery-card { min-height: 52px; border-radius: 14px; }
    .discovery-cta { min-height: 48px; margin-top: 8px; border-radius: 14px; }
    .discovery-footnote { margin-top: 9px; font-size: 11px; }
}

'''
text = text[:start] + new_css + text[end:]

html_pattern = re.compile(r'\s*<!-- Tela de Descoberta -->.*?<!-- Transição verde de tela cheia -->', re.S)
new_html = r'''
    <!-- Tela de Descoberta -->
    <div id="discovery-overlay">
        <div class="discovery-shell">
            <div class="discovery-brand">
                <div class="discovery-brand-name">Delícias da Vovó</div>
                <div class="discovery-brand-line"></div>
            </div>

            <section class="discovery-hero">
                <h1 class="discovery-title">Sabores que <em>aproximam</em></h1>
                <p class="discovery-subtitle">Escolha uma categoria para encontrar o que você procura.</p>
            </section>

            <p class="discovery-section-label">Cardápio</p>
            <div id="discovery-cards"></div>

            <button onclick="enterMenu()" class="discovery-cta" aria-label="Ver o cardápio completo">
                <span>Ver cardápio completo</span>
                <i class="fas fa-arrow-right"></i>
            </button>

            <p class="discovery-footnote">feito com carinho desde 2005</p>
        </div>
    </div>
    <!-- Transição verde de tela cheia -->'''
text, count = html_pattern.subn(new_html, text, count=1)
if count != 1:
    raise SystemExit(f'Não foi possível trocar o HTML da abertura: {count}')

render_pattern = re.compile(r'        function renderDiscovery\(\) \{.*?\n        \}\n\n        function showDiscovery', re.S)
new_render = r'''        function renderDiscovery() {
            const container = document.getElementById('discovery-cards');
            if (!container) return;

            container.innerHTML = MACRO_GROUPS.map((group, i) => {
                const isLastOdd = i === MACRO_GROUPS.length - 1 && MACRO_GROUPS.length % 2 !== 0;
                const groupNameAttr = group.name.replace(/'/g, "\\'");
                return `
                    <button type="button" class="discovery-card ${isLastOdd ? 'discovery-card-wide' : ''}" onclick="hideDiscovery('${groupNameAttr}')">
                        <span class="discovery-card-title">${group.short || group.name}</span>
                        <i class="fas fa-chevron-right discovery-arrow"></i>
                    </button>`;
            }).join('');
        }

        function showDiscovery'''
text, count = render_pattern.subn(new_render, text, count=1)
if count != 1:
    raise SystemExit(f'Não foi possível trocar renderDiscovery: {count}')

path.write_text(text, encoding='utf-8')
print('Abertura compacta aplicada com fontes originais.')
