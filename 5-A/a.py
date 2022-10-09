from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
Base = declarative_base()
engine = create_engine('postgresql://postgres:1@localhost:5432/postgres', echo = True)
Session = sessionmaker(bind = engine)
session = Session()

def Sahte(i):
  dizi = []
  for i in range(i):
   fake = Faker()
   dizigeç=[]
   dizigeç.append(fake.email())
   dizigeç.append(fake.password())
   dizi.append(dizigeç)
  return dizi


class Tablo(Base):
  __tablename__ = 'Login'
  id = Column(Integer, primary_key=True)
  email = Column(String(100))
  password = Column(String(100), nullable=False)

class Tablo2(Base):
  __tablename__ = 'Finding '
  id = Column(Integer, primary_key=True)
  email = Column(String(100))
  password = Column(String(100), nullable=False)

def Ekle(i):
  dizi=Sahte(i)
  for i in range (len(dizi)):
   c1 = Tablo(email = dizi[i][0], password =dizi[i][1])
   session.add(c1)
   session.commit()

Base.metadata.create_all(engine)
Ekle(10000)
dizi=[]
result = session.query(Tablo).limit(1000).all()
for row in result:
        dizigeç = []
        dizigeç.append(row.email)
        dizigeç.append(row.password)
        dizi.append(dizigeç)
dizi.extend(Sahte(9000))
start_time=time.time()
result1 = session.query(Tablo).all()
for i in range (len(dizi)):
 for row in result:
  if(row.email==dizi[i][0] and row.password==dizi[i][1]):
   c1 = Tablo2(email=dizi[i][0], password=dizi[i][1])
   session.add(c1)
   session.commit()
end_time=time.time()
print(end_time-start_time)



"""
id sebebi aynı e posta geldiğinde primary key olursa hata vermesi
numpy array kullanmak daha kolay olabilirdi ancak ilk bunu yaptım amaç optimazasyon olmadığı için bıraktım.
Comit türünü all yapabileceğimi farkındayım ne kadar yavaşlayacağını görmek için test yapıyordumn.
Süre=1079.4504404067993
"""