from pathlib import Path
from rdflib import Graph

BASE = Path(__file__).resolve().parent            # folder Pertemuan 11
SUMBER = BASE.parent / "Pertemuan 7" / "kampus_usu.ttl"
print("Mencari:", SUMBER, "| ada?", SUMBER.exists())
g = Graph().parse(data=SUMBER.read_text(encoding="utf-8"), format="turtle")
print("Sumber:", SUMBER, "| triple awal:", len(g))

# TODO: ganti IRI ex: persis sama dengan prefix ex: di berkas kampus_usu Anda
# (cek baris "@prefix ex:" di kampus_usu_v3.ttl / v2.ttl, termasuk akhiran # atau /)
PREFIX = """
PREFIX ex:     <https://zann-37.github.io/web-semantik-Kelompok03/251402110/kampus#>
PREFIX foaf:   <http://xmlns.com/foaf/0.1/>
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <https://schema.org/>
"""

# A. Pemetaan ke schema.org: graf baru, IRI tetap
# TODO: ganti Dosen dengan nama kelas dosen di graf Anda (mis. Dosen / Lecturer)
# TODO: bila properti nama bukan foaf:name, ganti juga
q_peta = PREFIX + """
CONSTRUCT { ?d a schema:Person ; schema:name ?nama . }
WHERE { ?d a ex:Lecturer ; foaf:name ?nama . }
"""
peta = Graph()
for t in g.query(q_peta):
    peta.add(t)
print("Triple hasil pemetaan:", len(peta))
peta.serialize("dosen_schema.ttl", format="turtle")

# B. Tambah hierarki kecil, lalu materialisasi
g.update(PREFIX + """
INSERT DATA {
  ex:Lecturer rdfs:subClassOf ex:Pegawai .
  ex:Pegawai rdfs:subClassOf foaf:Person .
}
""")
q_orang = PREFIX + "SELECT ?x WHERE { ?x a foaf:Person }"
print("foaf:Person sebelum:", len(g.query(q_orang)))

turunan = g.query(PREFIX + """
CONSTRUCT { ?x a ?super } WHERE { ?x a/rdfs:subClassOf+ ?super }
""")
baru = [t for t in turunan if t not in g]
for t in baru:
    g.add(t)
print("Triple turunan baru:", len(baru))
print("foaf:Person sesudah:", len(g.query(q_orang)))

g.serialize("kampus_usu_v4.ttl", format="turtle")
