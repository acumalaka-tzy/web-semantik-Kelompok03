from pathlib import Path
from rdflib import Graph
from owlrl import DeductiveClosure, RDFS_Semantics, OWLRL_Semantics

# Membaca file RDF
BASE_DIR = Path(__file__).resolve().parent

asserted = Graph().parse(
    BASE_DIR / "latihan12.ttl",
    format="turtle"
)

def tutup(semantik):
    g = Graph() + asserted
    DeductiveClosure(semantik).expand(g)
    return g

# Inferensi RDFS dan OWL RL
G = {
    "RDFS": tutup(RDFS_Semantics),
    "OWL RL": tutup(OWLRL_Semantics)
}

P = """
PREFIX ex: <http://contoh.id/latihan12/>
"""

soal = {
    "A": ("RDFS", "SELECT ?x WHERE { ?x a ex:Orang }"),
    "B": ("OWL RL", "SELECT ?a ?b WHERE { ?a ex:beradaDi ?b }"),
    "C": ("RDFS", "SELECT ?m ?d WHERE { ?m ex:dibimbing ?d }"),
    "D": ("OWL RL", "ASK { ex:medan a ex:Tempat }"),
}

for kode, (profil, q) in soal.items():
    hasil = G[profil].query(P + q)

    jawab = (
        hasil.askAnswer
        if hasil.type == "ASK"
        else f"{len(hasil)} baris"
    )

    print(kode, profil, jawab)
