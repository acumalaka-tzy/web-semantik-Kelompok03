
from pathlib import Path
from rdflib import Graph

folder = Path(__file__).resolve().parent
file_ttl = folder / "kampus_usu.ttl"

if not file_ttl.exists():
    print("File kampus_usu.ttl tidak ditemukan!")
    print("Simpan file TTL di folder:", folder)
    exit()

g = Graph()
g.parse(str(file_ttl), format="turtle")

g.serialize(destination=str(folder / "kampus_usu.jsonld"), format="json-ld")
g.serialize(destination=str(folder / "kampus_usu.nt"), format="nt")

print(f"Jumlah triple: {len(g)}")
print(g.serialize(format="turtle"))
