from pathlib import Path
from rdflib import Graph

# Membaca file RDF
BASE_DIR = Path(__file__).resolve().parent

SUMBER = BASE_DIR.parent / "pertemuan 10" / "kampus_usu_v3.ttl"

if not SUMBER.exists():
    # Jika v3 belum tersedia, gunakan v2
    SUMBER = BASE_DIR.parent / "pertemuan 9" / "kampus_usu_v2.ttl"

g = Graph().parse(SUMBER, format="turtle")

print("Sumber:", SUMBER, "| triple awal:", len(g))


PREFIX = """
PREFIX ex:     <https://contoh.github.io/web-semantik/251402043/kampus#>
PREFIX foaf:   <http://xmlns.com/foaf/0.1/>
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <https://schema.org/>
"""


# A. Pemetaan ke schema.org: graf baru, IRI tetap
q_peta = PREFIX + """
CONSTRUCT {
    ?d a schema:Person ;
       schema:name ?nama .
}
WHERE {
    ?d a ex:Kom_A ;
       foaf:name ?nama .
}
"""

peta = Graph()

for t in g.query(q_peta):
    peta.add(t)

print("Triple hasil pemetaan:", len(peta))

peta.serialize(
    destination=str(BASE_DIR / "dosen_schema.ttl"),
    format="turtle"
)


# B. Tambah hierarki kecil
g.update(PREFIX + """
INSERT DATA {
    ex:Kom_A rdfs:subClassOf ex:Pegawai .
    ex:Pegawai rdfs:subClassOf foaf:Person .
}
""")


# Menghitung jumlah foaf:Person sebelum materialisasi
q_orang = PREFIX + """
SELECT ?x WHERE {
    ?x a foaf:Person
}
"""

print("foaf:Person sebelum:", len(g.query(q_orang)))


# C. Inferensi dan materialisasi
turunan = g.query(PREFIX + """
CONSTRUCT {
    ?x a ?super .
}
WHERE {
    ?x a/rdfs:subClassOf+ ?super .
}
""")

baru = [t for t in turunan if t not in g]

for t in baru:
    g.add(t)

print("Triple turunan baru:", len(baru))

# Menghitung kembali setelah materialisasi
print("foaf:Person sesudah:", len(g.query(q_orang)))


# D. Menyimpan hasil RDF
g.serialize(
    destination=str(BASE_DIR / "kampus_usu_v4.ttl"),
    format="turtle"
)

print("File berhasil disimpan!")
