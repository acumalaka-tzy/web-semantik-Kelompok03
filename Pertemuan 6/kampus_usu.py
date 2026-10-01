from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF, XSD

g = Graph()
EX = Namespace("https://contoh.github.io/web-semantik/ISI_NIM/kampus#")

g.bind("ex", EX)
g.bind("foaf", FOAF)

# Dosen dan mata kuliah
g.add((EX.ida, RDF.type, EX.Lecturer))
g.add((EX.ida, FOAF.name, Literal("ISI_NAMA_DOSEN", lang="id")))
g.add((EX.web_semantik, RDF.type, EX.Course))
g.add((EX.web_semantik, FOAF.name, Literal("Web Semantik", lang="id")))
g.add((EX.ida, EX.mengajar, EX.web_semantik))

# Tambahkan triple Anda di bawah ini
# g.add((EX...., ..., ...))

print(g.serialize(format="turtle"))
g.serialize("kampus_usu.ttl", format="turtle")
g.serialize("kampus_usu.jsonld", format="json-ld", indent=2)
