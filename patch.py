s = open("index.html", encoding="utf-8").read()

def rep(old, new):
    global s
    assert old in s, "Introuvable : " + old[:40]
    s = s.replace(old, new)

rep('<div class="logo">🎶 VIVI <i>MUSIC</i></div>',
 '<div class="logo"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>VIVI <i>MUSIC</i></div>')

rep('<button id="sh" aria-label="Aléatoire">🔀</button>',
 '<button id="sh" aria-label="Aléatoire"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 3 21 3 21 8"/><line x1="4" y1="20" x2="21" y2="3"/><polyline points="21 16 21 21 16 21"/><line x1="15" y1="15" x2="21" y2="21"/><line x1="4" y1="4" x2="9" y2="9"/></svg></button>')

rep('<button id="rp" aria-label="Répéter">🔁</button>',
 '<button id="rp" aria-label="Répéter"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg></button>')

css = '''
:root{--r:#c20000}
.stage::before{background:radial-gradient(ellipse at 50% 40%,rgba(170,0,0,.45),transparent 64%)}
.sun{background:radial-gradient(circle at 36% 30%,#ff2a1f,#c20000 42%,#3d0000);box-shadow:0 0 calc(40px + var(--g,0)*130px) rgba(194,0,0,calc(.45 + var(--g,0)*.5))}
.dunes path:first-child{fill:#3d0000}
.ib{background:#c20000;border-color:#ff2a1f;box-shadow:0 0 18px rgba(194,0,0,.6)}
.logo{letter-spacing:1px}
.logo svg{vertical-align:-4px;margin-right:6px;color:#ff2a1f}
.ti,.t{text-transform:uppercase;letter-spacing:.5px}
.ti{font-size:clamp(20px,6.4vw,28px)}
.nv{color:#c20000;opacity:1}
#pg{stroke:#ff2a1f;filter:drop-shadow(0 0 3px #ff2a1f)}
.ring circle:first-child{stroke:#3d0000}
.tools button{color:#8a0000;opacity:1}
.tools button.on{color:#ff2a1f;filter:drop-shadow(0 0 6px #ff2a1f)}
.tools #hf{font-size:30px;line-height:1}
.sheet{background:#050000;border-top:3px solid var(--r)}
#list li{border-bottom-color:#2a0000;border-left:3px solid transparent;padding-left:10px}
#list li.on{border-left-color:#ff2a1f;background:linear-gradient(90deg,rgba(194,0,0,.3),transparent)}
li.on .t{color:#ff2a1f}
.h{color:#ff2a1f}
.tabs button.on{border-color:#ff2a1f}
dialog{background:#050000;border-color:#c20000}
.btn{background:#c20000;box-shadow:0 0 16px rgba(194,0,0,.5)}
'''
rep('</style>', css + '</style>')
open("index.html", "w", encoding="utf-8").write(s)
print("OK, design mis à jour")
