from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF, XSD
from rdflib.namespace import RDF

g = Graph()

EX = Namespace("https://zann-37.github.io/web-semantik-Kelompok03/251402110/kampus#")

g.bind("ex", EX)
g.bind("foaf", FOAF)

g.add((EX.ida, RDF.type, EX.Lecturer))
g.add((EX.ida, FOAF.name, Literal("Muhammad Isa Dadi Hasibuan", lang="id")))

g.add((EX.dedy_arisandi, RDF.type, EX.Lecturer))
g.add((EX.dedy_arisandi, FOAF.name, Literal("Dedy Arisandi", lang="id")))

g.add((EX.ivan_jaya, RDF.type, EX.Lecturer))
g.add((EX.ivan_jaya, FOAF.name, Literal("Ivan Jaya", lang="id")))

g.add((EX.web_semantik, RDF.type, EX.Course))
g.add((EX.web_semantik, FOAF.name, Literal("Web Semantik", lang="id")))
g.add((EX.web_semantik, EX.jumlahKredit, Literal(3, datatype=XSD.integer)))

g.add((EX.manajemen_basis_data, RDF.type, EX.Course))
g.add((EX.manajemen_basis_data, FOAF.name, Literal("Manajemen Basis Data", lang="id")))
g.add((EX.manajemen_basis_data, EX.jumlahKredit, Literal(3, datatype=XSD.integer)))

g.add((EX.pemrograman_web, RDF.type, EX.Course))
g.add((EX.pemrograman_web, FOAF.name, Literal("Pemrograman Web", lang="id")))
g.add((EX.pemrograman_web, EX.jumlahKredit, Literal(3, datatype=XSD.integer)))

g.add((EX.ida, EX.mengajar, EX.web_semantik))
g.add((EX.dedy_arisandi, EX.mengajar, EX.manajemen_basis_data))
g.add((EX.ivan_jaya, EX.mengajar, EX.pemrograman_web))

g.add((EX.izyan, RDF.type, EX.Student))
g.add((EX.izyan, FOAF.name, Literal("Muhammad Izyan", lang="id")))

g.add((EX.yazri, RDF.type, EX.Student))
g.add((EX.yazri, FOAF.name, Literal("Yazri Khoiri", lang="id")))
g.add((EX.yazri, EX.nim, Literal("251402016")))

g.add((EX.izyan, EX.mengambil, EX.web_semantik))
g.add((EX.izyan, EX.mengambil, EX.manajemen_basis_data))

g.add((EX.yazri, EX.mengambil, EX.web_semantik))
g.add((EX.yazri, EX.mengambil, EX.pemrograman_web))

g.add((EX.teknologi_informasi, RDF.type, EX.Faculty))
g.add((EX.teknologi_informasi, FOAF.name, Literal("Fakultas Ilmu Komputer dan Teknologi Informasi", lang="id")))

g.add((EX.ida, EX.bernaung_di, EX.teknologi_informasi))
g.add((EX.dedy_arisandi, EX.bernaung_di, EX.teknologi_informasi))
g.add((EX.ivan_jaya, EX.bernaung_di, EX.teknologi_informasi))

g.add((EX.izyan, EX.bernaung_di, EX.teknologi_informasi))
g.add((EX.yazri, EX.bernaung_di, EX.teknologi_informasi))

print(g.serialize(format="turtle"))

g.serialize("kampus_usu.ttl", format="turtle")
g.serialize("kampus_usu.jsonld", format="json-ld", indent=2)

print("Daftar dosen:")
for subject, predicate, obj in g.triples((None, RDF.type, EX.Lecturer)):
    print(subject)