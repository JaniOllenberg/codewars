    import datetime
    start_time = datetime.datetime.now()

    end_time = datetime.datetime.now()
    runtime = end_time - start_time
    print(f"runtime: {runtime.seconds}:{runtime.microseconds}microseconds")