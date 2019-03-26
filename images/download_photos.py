from  urllib.request import urlretrieve

photos = [
  'https://s3.portalt5.com.br/imagens/senor-abravanel-silvio-santos.jpg',
  'https://noticiasdatv.uol.com.br/media/_versions/_versions/silvio_santos_foto_lourival_ribeiro_sbt_fechada_free_big_fixed_large.jpg',
  'https://abrilexame.files.wordpress.com/2016/09/size_960_16_9_silvio-santos-nova4.jpg',
  'https://imagens2.ne10.uol.com.br/blogsne10/social1/uploads//2016/06/silvio-santos-748x410.jpg',
  'https://extra.globo.com/incoming/20464452-977-6cf/w640h360-PROP/xsilvio-santos.jpg.pagespeed.ic.ckJcIzsMIX.jpg'
  ]

count = 1
for photo in photos:
  try:
    urlretrieve(photo, 'ss%02d.jpg'%count)
    count += 1
  except:
    pass
