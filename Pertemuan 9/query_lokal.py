from pathlib import Path
from rdflib import Graph
 
BASE = Path(__file__).parent
 
g = Graph()
g.parse(BASE / ".." / "pertemuan-06" / "kampus_usu.ttl", format="turtle")
print("Jumlah triple awal:", len(g))
 
PREFIX = """
PREFIX ex:   <https://zann-37.github.io/web-semantik-Kelompok03/251402110/kampus#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
"""
 
q_select = PREFIX + """
SELECT ?namaDosen ?namaMK WHERE {
  ?dosen ex:mengajar ?mk ;
         foaf:name   ?namaDosen .
  ?mk    foaf:name   ?namaMK .
}
ORDER BY ?namaDosen
"""
for row in g.query(q_select):
    print(row.namaDosen, "-", row.namaMK)

q_ask = PREFIX + "ASK { ex:ida ex:mengajar ex:data_mining }"
print("Sebelum INSERT:", g.query(q_ask).askAnswer)

g.update(PREFIX + """
INSERT DATA {
  ex:ida ex:mengajar ex:data_mining .
  ex:data_mining a ex:Course ;
                 foaf:name "Data Mining"@id ;
                 ex:jumlahKredit 3 .
}
""")
print("Sesudah INSERT:", g.query(q_ask).askAnswer)
print("Jumlah triple akhir:", len(g))
 
g.serialize(BASE / "kampus_usu_v2.ttl", format="turtle")
