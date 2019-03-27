from  urllib.request import urlretrieve

photos_silvio_santos = [
  'https://s3.portalt5.com.br/imagens/senor-abravanel-silvio-santos.jpg',
  'https://noticiasdatv.uol.com.br/media/_versions/_versions/silvio_santos_foto_lourival_ribeiro_sbt_fechada_free_big_fixed_large.jpg',
  'https://abrilexame.files.wordpress.com/2016/09/size_960_16_9_silvio-santos-nova4.jpg',
  'https://imagens2.ne10.uol.com.br/blogsne10/social1/uploads//2016/06/silvio-santos-748x410.jpg',
  'https://extra.globo.com/incoming/20464452-977-6cf/w640h360-PROP/xsilvio-santos.jpg.pagespeed.ic.ckJcIzsMIX.jpg',
  'https://abrilexame.files.wordpress.com/2016/09/size_960_16_9_silvio-santos-trofeu-5904.jpg',
  'https://correio-cdn3.cworks.cloud/fileadmin/acervo/uploads/RTEmagicC_silvio_01.jpg.jpg',
  'https://abrilexame.files.wordpress.com/2016/09/size_960_16_9_silvio-santos-nova.jpg',
  'https://cdn-ofuxico.akamaized.net/img/upload/noticias/2018/07/30/reproducao_silvio_santos-sbt_326024_36.jpg'
  ]

photos_black_widow = [
  'https://entreterse.com.br/wp-content/uploads/2019/01/viuva-negra.jpg',
  'https://jovemnerd.com.br/wp-content/uploads/2019/03/viuva-negra-pistola-vingadores-ultimato-760x428.jpg',
  'https://static.cineclick.com.br/sites/adm/uploads/banco_imagens/31/602x0_1374852183.jpg',
  'https://4.bp.blogspot.com/-roCg7tsUO6s/W6j2L6jOn3I/AAAAAAAAN0M/EU00s5P_OusZ7lTtxwGwqx2yx6lI31rGACLcBGAs/s1600/viuva-negra-2_NWc60C0-1200x800_c.jpg',
  'http://3.bp.blogspot.com/-7pYmxKhky7Q/VU7LG3SFPhI/AAAAAAAApo4/VFuImGTDvXM/s1600/Marvel_-_Avengers_-_Natasha_Romanoff_(The_Avengers).jpg',
  'https://cdn.ome.lt/T_QNIYXMG9_gAcv12mLas2idblE=/fit-in/837x500/smart/uploads/conteudo/fotos/viuva_negra_LeHac3Q.jpg',
  'http://images6.fanpop.com/image/photos/40600000/Natasha-Romanoff-natasha-romanoff-40691086-500-411.jpg',
  'https://kanto.legiaodosherois.com.br/w750-h393-gnw-cfill-q80/wp-content/uploads/2017/04/legiao_KDMv8_31kgu52N9XiCGHOm4ISxLZfcyonEpWw7bP0B.jpg.jpeg',
]

photos_avengers = [
  'http://4.bp.blogspot.com/-XFJtUkzzrjo/T5odX2l2UBI/AAAAAAAACOU/mLeo1-UzkFs/s1600/vingador.jpg',
  'https://d.ibtimes.co.uk/en/full/1402568/avengers-age-ultron.jpg',
  'http://geeksoncoffee.com/wp-content/uploads/2019/02/captain-marvel-avengers.jpg'
]

def dowload_photos(links, prefix_name):
  count = 1
  
  for link in links:
    photo_name = '{}_{:02d}.jpg'.format(prefix_name, count)

    try:
      urlretrieve(link, photo_name)
      print('[SUCCESS]', photo_name)
      count += 1
    except:
      print('[ERROR]', link)

dowload_photos(photos_silvio_santos, 'ss')
dowload_photos(photos_black_widow, 'bw')
dowload_photos(photos_avengers, 'av')