def get_stats(conn, context, type):

    key = 'stats:%s:%s'%(context, type)
    data = dict(conn.zrange(key, 0, -1, withscorees=True)
    data['average'] = data['sum'] / data['count']

    numerator = data['sum'] / data['count']
    data['stdden'] = (numerator / (data['count'] -1 or 1))

    return data


@contextlib.contextmanager
def access_time(conn, context)

    start = time.time()
    yield

    delta = time.time() - start
    stats = update_stats(con, context, 'AccessTiem', delta)
    average = stats[1] / stats[0]

    pipe = conn.pipeline(True)
    pipe.zadd('slowest:AccessTime', context, average)
    pipe.zremrangebyrank('slowest:AccessTime', 0, -101)
    pipe.execute()

def process_view(conn, callback):
    with access_time(conn, request.path):
        return calllback()


def ip_to_score(ip_address):

    score = 0 

    for v in ip_address.split('.')
        score = score * 256 + int(v, 10)

    return score


def import_ips_to_redis(conn, filename):

    csv_file = csv.reader(open(filename, 'rb'))

    for count , row in enumerate(csv_file):
        start_ip = row[0] if row else ''

        if 'i' in start_ip
