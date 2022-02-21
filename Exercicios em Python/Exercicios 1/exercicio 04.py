medida = float(input(' qual e distancia em metros'))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}metros, convertida em {}dm e em {)cm e em {}mm'.format(medida, dm, cm, mm))
print('A medida de {}metros, convertida em {}dam e em {}hm e em {}km'.format(medida, dam, hm, km))
