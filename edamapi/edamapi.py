import click
from rich.console import Console
import time
from rdflib import ConjunctiveGraph
from rdflib.compare import to_isomorphic, graph_diff

"""
Based on RDFlib graph isomorphism implementation, itself based on the following works :

    An implementation of RGDA1 (publication below),
    a combination of Sayers & Karp's graph digest algorithm using
    sum and SHA-256 <http://www.hpl.hp.com/techreports/2003/HPL-2003-235R1.pdf>
    and traces <http://pallini.di.uniroma1.it>, an average case
    polynomial time algorithm for graph canonicalization.

    McCusker, J. P. (2015). WebSig: A Digital Signature Framework for the Web.
    Rensselaer Polytechnic Institute, Troy, NY.
    http://gradworks.umi.com/3727015.pdf 
"""


@click.command("reformat", short_help="...")
@click.option("-i", "--input_file", "input_file", multiple=False, help="Input file")
@click.option("-o", "--output_file", "output_file", multiple=False, help="Output file")
@click.option("-f", "--format", "formats", multiple=True, help="Output format, it can be 'turtle', 'jsonld', 'xml'")
def reformat(input_file, output_file, formats):
    # TODO Add a dry-run flag
    console = Console()
    start_time = time.time()
    if input_file:

        # TODO check that input file exists and can be parsed
        # TODO check that output file does not exist

        kg = ConjunctiveGraph()
        kg.parse(input_file)

        iso = to_isomorphic(kg)
        for f in formats:
            if f == "turtle":
                iso.serialize(destination=output_file, format="turtle")
            elif f == "jsonld":
                iso.serialize(destination=output_file, format="jsonld")
            elif f == "xml":
                iso.serialize(destination=output_file, format="xml")
            else:
                console.print(":warning: Please specify a supported format: turtle, jsonld, xml", style="bold red")

    elapsed_time = round((time.time() - start_time), 2)
    console.print(f"Ontology reformatted in {elapsed_time} s", style="green")


@click.command("compare", short_help="...")
@click.option("-l", "--first_file", "first_file", multiple=False, help="First file")
@click.option("-r", "--second_file", "second_file", multiple=False, help="Second file")
def reformat(first_file, second_file):
    # TODO check that first_file exists and can be parsed
    # TODO check that second_file exists and can be parsed
    console = Console()
    start_time = time.time()

    g1 = ConjunctiveGraph()
    g1.parse(first_file)
    g2 = ConjunctiveGraph()
    g2.parse(second_file)

    in_both, in_first, in_second = graph_diff(g1, g2)

    console.print("- - -", style="red")
    console.print(in_first.serialize(format="turtle"), style="red")
    console.print("+ + +", style="green")
    console.print(in_second.serialize(format="turtle"), style="green")

    elapsed_time = round((time.time() - start_time), 2)
    console.print(f"Diff processed in {elapsed_time} s")