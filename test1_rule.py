from rdflib import Graph
g = Graph()

rule = URIRef("http://example.com/testRule")
Group = URIRef("http://www.w3.org/2007/rif#Group")
sentences = URIRef("http://www.w3.org/2007/rif#sentences")
Forall = URIRef("http://www.w3.org/2007/rif#Forall")

g.add( (rule, RDF.type, Group) )

s = BNode() # a GUID is generated

g.add( (rule, sentences, s) )

r = BNode() # a GUID is generated

g.add( (s, RDF.type, RDF.List) )
g.add( (s, RDFS.first, r) )
g.add( (s, RDFS.next, RDFS.NIL) )

g.add( (r, RDFS.type, Forall) )
g.add( (r, RDFS.type, Forall) )

...

print g.serialize(format='n3')
