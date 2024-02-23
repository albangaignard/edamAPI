import unittest
from rdflib import ConjunctiveGraph
from rdflib.compare import to_isomorphic, graph_diff
import jellyfish

class ReformatTestCase(unittest.TestCase):
    v1 = """
    @prefix : <http://edamontology.org/> .
    @prefix dc: <http://purl.org/dc/elements/1.1/> .
    @prefix doap: <http://usefulinc.com/ns/doap#> .
    @prefix edam: <http://purl.obolibrary.org/obo/edam#> .
    @prefix foaf: <http://xmlns.com/foaf/0.1/> .
    @prefix oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> .
    @prefix oboOther: <http://purl.obolibrary.org/obo/> .
    @prefix owl: <http://www.w3.org/2002/07/owl#> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

    :data_0852 a owl:Class ;
        rdfs:label "Sequence mask type" ;
        :created_in "beta12orEarlier" ;
        :obsolete_since "1.5" ;
        oboInOwl:consider :data_0842 ;
        oboInOwl:hasDefinition "A label (text token) describing the type of sequence masking to perform." ;
        oboInOwl:inSubset edam:obsolete ;
        rdfs:comment "Sequence masking is where specific characters or positions in a molecular sequence are masked (replaced) with an another (mask character). The mask type indicates what is masked, for example regions that are not of interest or which are information-poor including acidic protein regions, basic protein regions, proline-rich regions, low compositional complexity regions, short-periodicity internal repeats, simple repeats and low complexity regions. Masked sequences are used in database search to eliminate statistically significant but biologically uninteresting hits." ;
        rdfs:subClassOf owl:DeprecatedClass ;
        owl:deprecated "true" .

    :data_0853 a owl:Class ;
        rdfs:label "DNA sense specification" ;
        :created_in "beta12orEarlier" ;
        :obsolete_since "1.20" ;
        :oldParent :data_2534 ;
        oboInOwl:consider :data_2534 ;
        oboInOwl:hasDefinition "The strand of a DNA sequence (forward or reverse)." ;
        oboInOwl:inSubset edam:obsolete ;
        rdfs:comment "The forward or 'top' strand might specify a sequence is to be used as given, the reverse or 'bottom' strand specifying the reverse complement of the sequence is to be used." ;
        rdfs:subClassOf owl:DeprecatedClass ;
        owl:deprecated "true" .
    """

    v2 = """
    @prefix : <http://edamontology.org/> .
    @prefix dc: <http://purl.org/dc/elements/1.1/> .
    @prefix doap: <http://usefulinc.com/ns/doap#> .
    @prefix edam: <http://purl.obolibrary.org/obo/edam#> .
    @prefix foaf: <http://xmlns.com/foaf/0.1/> .
    @prefix oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> .
    @prefix oboOther: <http://purl.obolibrary.org/obo/> .
    @prefix owl: <http://www.w3.org/2002/07/owl#> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

    :data_0852 a owl:Class ;
        rdfs:label "Sequence mask type" ;
        oboInOwl:hasDefinition "A label (text token) describing the type of sequence masking to perform." ;
        :created_in "beta12orEarlier" ;
        rdfs:comment "Sequence masking is where specific characters or positions in a molecular sequence are masked (replaced) with an another (mask character). The mask type indicates what is masked, for example regions that are not of interest or which are information-poor including acidic protein regions, basic protein regions, proline-rich regions, low compositional complexity regions, short-periodicity internal repeats, simple repeats and low complexity regions. Masked sequences are used in database search to eliminate statistically significant but biologically uninteresting hits." ;
        :obsolete_since "1.5" ;
        oboInOwl:inSubset edam:obsolete ;
        oboInOwl:consider :data_0842 ;    
        rdfs:subClassOf owl:DeprecatedClass ;
        owl:deprecated "true" .



    :data_0853 a owl:Class ;
        rdfs:label "DNA sense specification" ;
        :created_in "beta12orEarlier" ;
        :obsolete_since "1.20" ;
        :oldParent :data_2534 ;
        oboInOwl:consider :data_2534 ;
        oboInOwl:hasDefinition "The strand of a DNA sequence (forward or reverse)." ;
        oboInOwl:inSubset edam:obsolete ;
        rdfs:comment "The forward or 'top' strand might specify a sequence is to be used as given, the reverse or 'bottom' strand specifying the reverse complement of the sequence is to be used." ;
        rdfs:subClassOf owl:DeprecatedClass ;
        owl:deprecated "true" .

    """

    v3 = """
    @prefix : <http://edamontology.org/> .
    @prefix dc: <http://purl.org/dc/elements/1.1/> .
    @prefix doap: <http://usefulinc.com/ns/doap#> .
    @prefix edam: <http://purl.obolibrary.org/obo/edam#> .
    @prefix foaf: <http://xmlns.com/foaf/0.1/> .
    @prefix oboInOwl: <http://www.geneontology.org/formats/oboInOwl#> .
    @prefix oboOther: <http://purl.obolibrary.org/obo/> .
    @prefix owl: <http://www.w3.org/2002/07/owl#> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

    :data_0853 a owl:Class ;
        rdfs:label "DNA sense specification" ;
        :created_in "beta12orEarlier" ;
        :obsolete_since "1.20" ;
        :oldParent :data_2534 ;
        oboInOwl:consider :data_2534 ;
        oboInOwl:hasDefinition "The strand of a DNA sequence (forward or reverse)." ;
        oboInOwl:inSubset edam:obsolete ;
        rdfs:comment "The forward or 'top' strand might specify a sequence is to be used as given, the reverse or 'bottom' strand specifying the reverse complement of the sequence is to be used." ;
        rdfs:subClassOf owl:DeprecatedClass ;
        owl:deprecated "true" .

    :data_0852 a owl:Class ;
        rdfs:label "Sequence mask type" ;
        oboInOwl:hasDefinition "A label (text token) describing the type of sequence masking to perform." ;
        :created_in "beta12orEarlier" ;
        rdfs:comment "Sequence masking is where specific characters or positions in a molecular sequence are masked (replaced) with an another (mask character). The mask type indicates what is masked, for example regions that are not of interest or which are information-poor including acidic protein regions, basic protein regions, proline-rich regions, low compositional complexity regions, short-periodicity internal repeats, simple repeats and low complexity regions. Masked sequences are used in database search to eliminate statistically significant but biologically uninteresting hits." ;
        :obsolete_since "1.5" ;
        oboInOwl:inSubset edam:obsolete ;
        oboInOwl:consider :data_0842 ;    
        rdfs:subClassOf owl:DeprecatedClass ;
        owl:deprecated "true" .

    """

    def test_different_serializations(self):
        self.assertNotEquals(self.v1, self.v2)
        self.assertNotEquals(self.v1, self.v3)
        self.assertGreaterEqual(jellyfish.levenshtein_distance(self.v1, self.v2), 255)

    def test_same_serializations(self):
        kg1 = ConjunctiveGraph()
        kg1.parse(data=self.v1, format="turtle")
        v11 = to_isomorphic(kg1).serialize(format="xml")

        kg2 = ConjunctiveGraph()
        kg2.parse(data=self.v2, format="turtle")
        v21 = to_isomorphic(kg2).serialize(format="xml")

        self.assertGreaterEqual(jellyfish.levenshtein_distance(v11, v21), 0)
        self.assertEqual(v11, v21)


if __name__ == '__main__':
    unittest.main()
