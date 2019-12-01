faves = []

cached_faves_name = './cached_faves.json'

# count how many times API is used
rate_status = {
    'limit' : 5,  # requests per minute
    'current' : 0,  # current count of API
    'start' : -1,  # time when rate counting started
    'seconds' : 60 # seconds of interval
}