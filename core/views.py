from django.shortcuts import render
import pickle
import rdflib


def serialize_graph():
    from pathlib import Path

    g = rdflib.Graph()

    for archive in Path('combine').iterdir():
        for rdfpath in archive.glob("model/*.rdf"):
            data = rdfpath.read_text(encoding='utf-8')
            g.parse(data=data)

    with open("rdflib_graph.pickle", mode="wb") as f:
        pickle.dump(g, f, protocol=pickle.HIGHEST_PROTOCOL)


def BootstrapFilterView(request):
    if "filter_for" in request.GET and "entity" in request.GET:
        # TODO: Add SPARQL mappings for all statements
        # TODO: Use prepared SPARQL queries to avoid SPARQL injection
        options = {
            'Has Mediator Participant': (
                """        
                SELECT ?extRef ?participant
                WHERE {{
                  ?s semsim:hasMediatorParticipant ?participant .
                  ?participant semsim:hasPhysicalEntityReference ?entityRef .
                  ?entityRef bqbiol:is ?extRef .
                  FILTER (contains(str(?extRef), "{}")) .
                }}
                ORDER BY ?participant
                """
            ),
            'Contain species': '',
            'Contain reaction': '',
            'Include protein': '',
            'Contain protein': '',
            'Include compartment': '',
            'Apply to taxon': '',
            'Include protein as reactant': '',
            'Include protein as product': ''
        }
        _filter = request.GET["filter_for"]
        entity = request.GET["entity"]
        query = options[_filter].format(entity)

        with open("rdflib_graph.pickle", mode="rb") as f:
            g = pickle.load(f)
            results = g.query(query)
        for result in results:
            print(result[1])
        return render(request, "bootstrap_form.html", context={"models": results})
    return render(request, "bootstrap_form.html", {})
