from pathlib import Path
from rdflib import Graph, RDF, RDFS
from owlrl import DeductiveClosure, RDFS_Semantics

BASE = "https://zann-37.github.io/web-semantik-Kelompok03/251402110/kampus#"
BASE_DIR = Path(__file__).resolve().parent
SUMBER = BASE_DIR.parent / "Pertemuan 9" / "kampus_usu_v2.ttl"

# 1. Graf asserted: data Anda + skema kecil
asserted = Graph().parse(SUMBER, format="turtle")
asserted.update(f"""
PREFIX ex: <{BASE}>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
INSERT DATA {{
    ex:Lecturer rdfs:subClassOf ex:Pegawai .
    ex:Pegawai rdfs:subClassOf foaf:Person .
    ex:mengajar rdfs:domain ex:Lecturer ;
                rdfs:range ex:Course .
}}""")
print("Sumber:", SUMBER, "| asserted:", len(asserted))

# 2. Closure dihitung pada salinan, inferred = selisihnya
closure = Graph() + asserted
DeductiveClosure(RDFS_Semantics).expand(closure)
inferred = closure - asserted

# 3. Simpan hanya turunan yang bermakna
TRIVIAL = {RDFS.Resource, RDF.Property}
bermakna = Graph()
for s, p, o in inferred:
    if str(s).startswith(BASE) and o not in TRIVIAL and s != o:
        bermakna.add((s, p, o))
print("Closure:", len(closure), "| inferred:", len(inferred),
      "| bermakna:", len(bermakna))

asserted.serialize(BASE_DIR / "kampus_usu_v5.ttl", format="turtle")
bermakna.serialize(BASE_DIR / "kampus_usu_inferred.ttl", format="turtle")