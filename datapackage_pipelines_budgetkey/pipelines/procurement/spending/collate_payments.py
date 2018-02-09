from datapackage_pipelines.wrapper import process

def process_row(row, row_index,
                spec, resource_index,
                parameters, stats):
    if spec['name'] == parameters['resource']:
        row['payment'] = {
            'year': row['report-year'],
            'period': row['report-period'],
            'timestamp': '{report-year}-{report-period}'.format(**row),
            'executed': row['executed'],
            'volume': row['volume'],
        }
    return row


def modify_datapackage(dp, parameters, stats):
    for resource in dp['resources']:
        if resource['name'] == parameters['resource']:
            resource['schema']['fields'].append({
                'name': 'payment',
                'type': 'object'
            })
    return dp

process(modify_datapackage=modify_datapackage,
        process_row=process_row)