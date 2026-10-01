from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF, XSD

g = Graph()
EX = Namespace("https://zann-37.github.io/web-semantik-Kelompok03/251402110/kampus#")

g.bind("ex", EX)
g.bind("foaf", FOAF)

# Dosen dan mata kuliah
g.add((EX.ida, RDF.type, EX.Lecturer))
g.add((EX.ida, FOAF.name, Literal("Muhammad Isa Dadi Hasibuan", lang="id")))
g.add((EX.web_semantik, RDF.type, EX.Course))
g.add((EX.web_semantik, FOAF.name, Literal("Web Semantik", lang="id")))
g.add((EX.ida, EX.mengajar, EX.web_semantik))

# Tambahkan triple Anda di bawah ini
# Mahasiswa
g.add((EX.izyan, RDF.type, EX.Student))
g.add((EX.izyan, FOAF.name, Literal("Muhammad Izyan", lang="id")))
g.add((EX.izyan, EX.mengambil, EX.web_semantik))

# Fakultas
g.add((EX.ilmu_komputer, RDF.type, EX.Faculty))
g.add((EX.ilmu_komputer, FOAF.name, Literal("Fakultas Ilmu Komputer dan Teknologi Informasi", lang="id")))
g.add((EX.ida, EX.bernaung_di, EX.teknologi_informasi))

print(g.serialize(format="turtle"))
g.serialize("kampus_usu.ttl", format="turtle")
g.serialize("kampus_usu.jsonld", format="json-ld", indent=2)
