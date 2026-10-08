
#punya siapa ini woi isi dlu nanti

from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, DCTERMS, XSD

g = Graph()
g.parse("kampus_usu.ttl", format="turtle")

EX = Namespace("https://zann-37.github.io/web-semantik-Kelompok03/251402110/kampus#")
stmt = URIRef(EX + "stmt-01")

jumlah_sebelum = len(g)

g.add((stmt, RDF.type, RDF.Statement))
g.add((stmt, RDF.subject, EX.ida))
g.add((stmt, RDF.predicate, EX.mengajar))
g.add((stmt, RDF.object, EX.web_semantik))
g.add((stmt, DCTERMS.creator, EX.ida))
g.add((stmt, DCTERMS.date, Literal("2026-10-01", datatype=XSD.date)))
g.add((stmt, DCTERMS.source, Literal("Data akademik kampus")))

print(f"Triple sebelum reifikasi: {jumlah_sebelum}")
print(f"Triple sesudah reifikasi: {len(g)}")

g.bind("ex", EX)
g.bind("dct", DCTERMS)
g.serialize("kampus_usu_reifikasi.ttl", format="turtle")
