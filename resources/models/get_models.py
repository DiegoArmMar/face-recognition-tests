import bz2
from glob import glob

compressed_models_directory = '../../dependencies/dlib-models/*.bz2'
compressed_models_paths = glob(compressed_models_directory)
buffer_size = 10240 # 10k

for file_path in compressed_models_paths:
  file_name = file_path.split('/')[-1].replace('.bz2','')

  with open(file_name, 'wb') as d, bz2.BZ2File(file_path, 'rb') as c:
    for data in iter(lambda: c.read(buffer_size), b''):
      d.write(data)
  
  print("[MODEL]", file_name)

