faves = []

cached_faves_name = './cached_faves.json'

rate_status = {
    'limit' : 5,  # requests per minute
    'current' : 0,
    'start' : -1
}