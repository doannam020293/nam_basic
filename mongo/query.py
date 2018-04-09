
def query_with_text(coll, text_query, limit = 10, sort_text = True):
    '''
    query text, return list  document sorted by score text in mongodb
    :param coll: 
    :param text_query: 
    :param limit: 
    :param sort_text: 
    :return: 
    '''
    query1 = { "$text": { "$search": text_query } }
    # query2 = { "score": { "$meta": "textScore" } }
    if sort_text:
        result = list(
        coll.find(
            query1,
            {'score': {'$meta': 'textScore'}},
            limit= limit,
        ).sort([('score', {'$meta': 'textScore'})])
                   )
    else:
        result = list(
        coll.find(
            query1,
            {'score': {'$meta': 'textScore'}},
            limit= limit,
        ))
    return result