import os
import argparse
from hubmapy import HuBMAPy

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A package to query the HuBMAP Human Reference Atlas Ontology.")
    parser.add_argument("-q", "--query", required=True, type=str,
                        help="Input query file containing a single SPARQL query")
    parser.add_argument("-o", "--output", required=False, type=str, default=os.getcwd(),
                        help="Path to output folder for the query results files (default=current working directory)")
    parser.add_argument("-n", "--name", required=False, type=str, default='user_query',
                        help="Name of the query, to be included in the output query results file (default=user_query)")
    parser.add_argument("-r", "--save_reasoned_ontology", required=False, default=False, action="store_true",
                        help="Save the ontology with its inferred axioms after reasoning (default=False)")
    arguments = parser.parse_args()
    hubmap = HuBMAPy(output_folder=arguments.output, save_reasoned_ontology=arguments.save_reasoned_ontology)
    hubmap.do_query_from_file(query_file_path=arguments.query, query_name=arguments.name)