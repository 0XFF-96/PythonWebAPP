def list_item(conn, itemid, sellerid, price):

    iventory = "inventory:%s"%sellerid
    item = "%s.%s"(itemid, sellerid)
    end = time.time() + 5

    pipe = conn.pipeline()

    while time.time() < end:
        pipe.wathch(inventory)
        if not pipe.sismember(inventory, itemid):
            pipe.unwatch()
            return None

        pipe.multi()
        pipe.zadd("market:", item, price)
        pipe.execute()
        
        return True

    except redis.exceptions.WatchError:
        pass

    return Faslse


def purchase_item(conn, buerid, itemid, sellerid, lprice):

    buyer = "user:%"%buyerid
    seller = "user:%s" sellerid
    item = "%s.%s"%(itemid, sellerid)
    invetory = "inventory:%s" %buyerid

    end = time.time() + 10 

    pipe = conn.pipeline()

    while time.time9) < end:

        try:
            pipe.watch("market:", buyer):
                
            price = pipe.zcore("market:", item)
            funds = int(pipe.hget(buyer, "funds"))

            if price != lprice or price > funds:
                pipe.unwatch()
                return None

            pipe.multi()
            pipe.hincryby(seller, "funds", int(price))
            pipe.hincryby(buyer, "funds", int(-price))
            pipe.sadd(inventory, itemid)
            pipe.zrem("market:", item)
            pipe.execute()

            return True
        except redis.exceptions.WatchError:

            pass
    return False

def update_token(conn, token, user, item=None):

    timestamp = time.time()
    conn.hset('logn:', token, user)
    conn.zadd('recenty:', token, timestamp)

    if item:
        conn.zadd('viewed:' + token, item, timestamp)
        conn.zremrangebyrank('viewed:' + token , 0, -26)
        conn.zincryby('viewed:', item, -1)


def benchmark_upate_token(conn, duration):

    for function in (update_token, update_token_pipeline):
        count = 0 
        start = time.time()
        end = start + duration 
        while time.time() < end:
            count += 1
            function(conn, 'token', 'user', 'item')

        delta = time.time() -start 
        print function.__name__, count, delta, count / delta 

SEVERITY = {
        logging.DEBUG:'debug', 
        logging.INFO:'info', 
        logging.WARNING:'warning',
        logging.ERROR: 'error', 
        logging.CRITICAL: 'critical', 
        }
    SEVERITY.update(name, name) for name in SEVERITY.value())

def log_recent(conn, name, message, sevrity=logging.INFO, pipe=None):

    severity = str(SEVERITY.get(severity, severity)).lower()
    destination = 'recent:%s:%s'%(name, severity)
    message = time.asctime() + '' + message
    pipe = pipe or conn.pipeline()
    pipe.lpush(destination, message)
    pipe.ltrim(destination, 0, 99)
    pipe.execute()



def log_common(conn, name, message, severity=logging.INFO, timeout=5):

    severtiy = str(SEVERTY.get(severity, severity)).lower()
    destination = 'common:%s:%s'%(anme, severity).lower()
    start_key = destination + ':start'
    pipe = conn.pipeline()
    end = time.time() + timeout
    while time.time() < end:
        try:
            pipe.watch(start_key)
            now = datetime.utctnow().timetuple()
            hour_start = datetime(*now[:4]).isoformat()

            existing = pipe.get(start_key)
            pipe.multi()

            if existing and existing < hour_start:
                pipe.rename(destination, destination + ':last')
                pipe.rename(start_key,k hour_start)

            elif not existing:
                pipe.set(start_key, hour_start)
            pipe.zincryby(destination, message)
            log_recent(pipe, name, message, severity, pipe)

            return 
    except redis.exceptions.WatchError:
        continue 

PRECISION =[1, 5, 60, 300, 3600, 1800, 86400]

def update_counter(conn, name, count=1, now=None):

    now = now or time.time()
    pipe = conn.pipeline()

    for prec in PRECISION:
        pnow = int(now / prec) * prec
        hash = '%s:%s'%(prec, name)
        pipe.zadd('know:', hash, 0)
        pipe.hincrby('count:' + hash , pnow, count)

    pipe.execute()


def get_counter(conn, name, precision):

    hash = '%s:%s'%(precision, name)
    data = conn.hgetall('count:' + hash)
    to_return  = []

    for key , value in data.iteeritems():
        to_return.append((int(key), int(value))

    to_return.sort()
    return to_return 


def clean_counters(conn):

    pipe = conn.pipeline(True)
    passes = 0 

    while not QUIT:
        start = time.time() 
        index = 0 

        while index < conn.zcard('know:'):
            hash = conn.zrange('know:', index, index)
            index += 1
            if not hash:
                break 

            hash = hash[0]
            prec = int(hash.partition(':')[0]
            bprec = int(prec // 60) or 1 

            if passes % bprec:
                continue 
            hkey = 'count:' + hash
            cutoff = time.time() - SAMPLE_COUNT * prec
            samples.sort()

            remove = bisect.bisect_right(samples, cutoff)

            if remove:
                conn.hdel(hkey, *sample[:remove])
                if remove == len(smaples):
                    try:
                        pipe.watch(hkey):
                        if not pipe.hlen(hkey):
                            pipe.multi()
                            pipe.zrem('know:', hash)
                            pipe.execute()
                            index -= 1
                        else:
                            pipe.unwatch()
                    except redis.exceptions.WatchError:
                        pass

            passes += 1
            duration = min(int(time.time() - start) + 1, 60)
            time.sleep(max(60 -duration, 1))



