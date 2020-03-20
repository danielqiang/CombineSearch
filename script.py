options = {
    # TODO: Use prepared SPARQL queries to avoid SPARQL injection
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
    # TODO: Add SPARQL mappings for all statements
    'Contain species': None,
    'Contain reaction': None,
    'Include protein': None,
    'Contain protein': None,
    'Include compartment': None,
    'Apply to taxon': None,
    'Include protein as reactant': None,
    'Include protein as product': None
}

# http://purl.obolibrary.org/obo/PR_P29994
