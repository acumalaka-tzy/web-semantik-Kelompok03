import csv
from pathlib import Path
from rdflib import Graph, Namespace, RDF, URIRef
from owlrl import DeductiveClosure, RDFS_Semantics, OWLRL_Semantics

BASE = "https://zann-37.github.io/web-semantik-Kelompok03/251402110/kampus#"
ERR = Namespace("http://www.daml.org/2002/03/agents/agent-ont#")
BASE_DIR = Path(__file__).resolve().parent

asserted = Graph().parse(BASE_DIR / "kampus_usu_v5.ttl", format="turtle")
asserted.update(f"""
PREFIX ex: <{BASE}>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
INSERT DATA {{
    ex:Pegawai owl:disjointWith ex:Course .
    ex:web_semantik ex:mengajar ex:ida .   # sengaja terbalik
}}""")

KELAS = ["Lecturer", "Pegawai", "Course"]

def anggota(g, kelas):
    return len(set(g.subjects(RDF.type, URIRef(BASE + kelas))))

hasil = {}
for nama, semantik in [("RDFS", RDFS_Semantics), ("OWL RL", OWLRL_Semantics)]:
    g = Graph() + asserted
    DeductiveClosure(semantik).expand(g)
    pesan = [str(e) for m in g.subjects(RDF.type, ERR.ErrorMessage)
             for e in g.objects(m, ERR.error)]
    hasil[nama] = {k: anggota(g, k) for k in KELAS}
    print(nama, len(g), "triple |", len(pesan), "pesan galat")
    for p in pesan:
        print(" ", p)

with open(BASE_DIR / "laporan_kelas.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["kelas", "asserted", "rdfs", "owl_rl"])
    for k in KELAS:
        w.writerow([k, anggota(asserted, k), hasil["RDFS"][k], hasil["OWL RL"][k]])
print("CSV tersimpan: laporan_kelas.csv")