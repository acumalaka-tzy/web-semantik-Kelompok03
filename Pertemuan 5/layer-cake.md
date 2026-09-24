| Lapis | Peran | Contoh Anda |
|---|---|---|
| URI dan Unicode | Identitas global dan representasi karakter | IRI dasar graf RDF kampus yang kubuat: `https://contoh.github.io/web-semantik/062/kampus#` |
| XML | Sintaks pertukaran data | Hasil ekspor ontology `pizza.owl` di Protégé ke format RDF/XML |
| RDF dan RDFS | Pernyataan graph dan kosakata dasar | Triple `kampus:Dosen_A kampus:mengajar kampus:Web_Semantik` yang aku bikin pakai rdflib, plus `rdfs:label` buat kasih nama tampilan entitasnya |
| Ontology / OWL | Makna domain dan penalaran lebih kaya | Hirarki class di ontology mini "Kampus" (Protégé): `Lecturer rdfs:subClassOf Person`, jadi reasoner otomatis tahu Dosen_A juga seorang Person |
| SPARQL | Query graph RDF | Query buat nyari semua dosen yang ngajar Web Semantik: `SELECT ?dosen WHERE { ?dosen kampus:mengajar kampus:Web_Semantik }` |
| Rules, Proof, Trust | Aturan, pembuktian, dan kepercayaan | Inferensi otomatis reasoner: dari `Student rdfs:subClassOf Person` + `andi_s001 rdf:type Student`, disimpulkan `andi_s001 rdf:type Person` tanpa ditulis manual |

Kenapa ontology ada di atas RDF/RDFS dan di bawah SPARQL?
= Karena ontology (OWL) butuh RDF/RDFS dulu sebagai fondasi — ontology cuma nambahin makna dan aturan logika di atas model triple yang udah ada, jadi gak bisa berdiri sendiri tanpa RDF. Sementara SPARQL ada di atas ontology karena SPARQL butuh graf yang udah punya struktur dan makna jelas (hasil dari RDF + ontology) buat bisa di-query secara berguna — makin kaya makna di ontology-nya, makin bermakna juga hasil query-nya.
