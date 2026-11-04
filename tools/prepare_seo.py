from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,re
root=Path('dist');logo=Image.open(root/'assets/logo-oficial.png').convert('RGBA')
# A marca original é preservada, apenas redimensionada sobre fundo claro.
def icon(size):
 im=Image.new('RGBA',(size,size),'#FAFBF4');mark=logo.copy();mark.thumbnail((int(size*.9),int(size*.9)));im.alpha_composite(mark,((size-mark.width)//2,(size-mark.height)//2));return im
icon(256).save(root/'favicon.ico',sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])
for size,name in [(32,'favicon-32.png'),(180,'apple-touch-icon.png'),(192,'icon-192.png'),(512,'icon-512.png')]:icon(size).save(root/name)
im=Image.new('RGB',(1200,630),'#FAFBF4');d=ImageDraw.Draw(im);d.rectangle((0,0,1200,16),fill='#526437');mark=logo.copy();mark.thumbnail((650,330));im.paste(mark,((1200-mark.width)//2,70),mark)
f=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',30);b=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',25)
d.text((600,448),'Cuidado para seus pés. Beleza para sua pele.',font=f,fill='#303B25',anchor='mm');d.text((600,514),'Campinas • São José / SC',font=b,fill='#526437',anchor='mm');im.save(root/'assets/compartilhar-clinica.jpg',quality=92)
base='https://esteticaepodologia.com.br/'
title='Estética & Podologia em São José | Campinas, SC'
desc='Clínica de estética e podologia em Campinas, São José/SC. Tratamentos faciais, corporais, unhas e atendimento domiciliar. Agende pelo WhatsApp.'
h=(root/'index.html').read_text(encoding='utf-8');h=re.sub(r'<title>.*?</title>','<title>'+title+'</title>',h);h=re.sub(r'<meta name="description"[^>]*>','<meta name="description" content="'+desc+'">',h)
meta=f'''\n<!-- URL de produção prevista: atualizar se o endereço final mudar. -->
<link rel="canonical" href="{base}"><meta name="robots" content="index,follow,max-image-preview:large">
<link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png"><link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png"><link rel="manifest" href="site.webmanifest">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="Clínica Estética &amp; Podologia"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{base}"><meta property="og:image" content="{base}assets/compartilhar-clinica.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:type" content="image/jpeg"><meta property="og:image:alt" content="Logo da Clínica Estética &amp; Podologia, em São José, SC">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{base}assets/compartilhar-clinica.jpg"><meta name="twitter:image:alt" content="Clínica Estética &amp; Podologia">
'''
data={'@context':'https://schema.org','@graph':[{'@type':'WebSite','@id':base+'#website','url':base,'name':'Clínica Estética & Podologia','inLanguage':'pt-BR'},{'@type':'LocalBusiness','@id':base+'#clinica','name':'Clínica Estética & Podologia','url':base,'logo':base+'assets/logo-oficial.png','image':base+'assets/compartilhar-clinica.jpg','telephone':'+5548991520543','address':{'@type':'PostalAddress','streetAddress':'Av. Presidente Kennedy, 698, Sala 437, Campinas','addressLocality':'São José','addressRegion':'SC','postalCode':'88101-000','addressCountry':'BR'},'openingHoursSpecification':[{'@type':'OpeningHoursSpecification','dayOfWeek':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],'opens':'09:00','closes':'19:00'}],'sameAs':['https://www.instagram.com/estetica_e_podologia','https://www.facebook.com/esteticaeepodologia/'],'description':'Atendimento com hora marcada. Estética, podologia e atendimento domiciliar.'}]}
h=h.replace('</head>',meta+'<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False)+'</script></head>');(root/'index.html').write_text(h,encoding='utf-8')
(root/'site.webmanifest').write_text(json.dumps({'name':'Clínica Estética & Podologia','short_name':'Estética & Podologia','lang':'pt-BR','start_url':'./','display':'browser','theme_color':'#526437','background_color':'#FAFBF4','icons':[{'src':f'icon-{n}.png','sizes':f'{n}x{n}','type':'image/png'} for n in [192,512]]},ensure_ascii=False),encoding='utf-8')
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+base+'sitemap.xml\n',encoding='utf-8')
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>'+base+'</loc></url></urlset>',encoding='utf-8')
Path('PUBLICACAO-SEO.md').write_text('''# Publicação e prévia de links

Configuração preparada para https://esteticaepodologia.com.br/ (raiz). Ainda não publicada.

- Enviar TODO o conteúdo de dist à raiz pública, incluindo ícones, assets, robots.txt e sitemap.xml.
- Se usar /home/, GitHub Pages ou outro domínio, atualizar canonical, og:url, og:image, twitter:image, URLs do JSON-LD, sitemap.xml e robots.txt para o endereço efetivo antes de publicar.
- A imagem de compartilhamento precisa responder publicamente em HTTPS sem login. Redes sociais podem manter a prévia antiga em cache.
- Validar o link publicado e os dados estruturados e cadastrar o sitemap no Search Console. Metadados não garantem posição no Google nem exibição da imagem em todos os aplicativos.
- Preservar/redirecionar URLs antigas ao substituir o site. Validar os avisos legais e os direitos de mídia antes de publicação pública.
''',encoding='utf-8')
print('Ícones, imagem social, metadados, JSON-LD, sitemap e robots criados.')
