from pathlib import Path
from rdflib import Graph

# Membaca file RDF
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR.parent / "pertemuan 6" / "kampus_usu.ttl"

g = Graph()
g.parse(file_path, format="turtle")

print("Jumlah triple awal:", len(g))

PREFIX = """
PREFIX ex:   <https://Zann-37.github.io/web-semantik-kelompok03/251402110/kampus#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
"""

# 1. SELECT: siapa mengajar apa
q_select = PREFIX + """
SELECT ?namaDosen ?namaMK WHERE {
    ?dosen ex:mengajar ?mk ;
           foaf:name ?namaDosen .
    ?mk foaf:name ?namaMK .
}
ORDER BY ?namaDosen
"""

print("\nHasil SELECT:")
for row in g.query(q_select):
    print(row.namaDosen, "-", row.namaMK)


# 2. ASK: fakta yang belum tercatat
q_ask = PREFIX + """
ASK {
    ex:ida ex:mengajar ex:pti
}
"""

print("\nSebelum INSERT:", g.query(q_ask).askAnswer)


# 3. INSERT DATA: menambahkan fakta baru
g.update(PREFIX + """
INSERT DATA {
    ex:ida ex:mengajar ex:pti .
    ex:pti foaf:name "Pengantar Teknologi Informasi"@id .
}
""")

print("Sesudah INSERT:", g.query(q_ask).askAnswer)

# Menampilkan jumlah triple akhir
print("Jumlah triple akhir:", len(g))

# Menyimpan hasil RDF
output_file = BASE_DIR / "kampus_usu_v2.ttl"
g.serialize(destination=str(output_file), format="turtle")

print("\nFile berhasil disimpan:", output_file)
