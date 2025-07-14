def evaluate_time(method, image, scale, repeat=10, verbose=True):
    times = []
    result = None

    for _ in range(repeat):
        result, elapsed = method(image, scale) 
        times.append(elapsed)

    avg_time = sum(times) / repeat

    if verbose:
        print(f"[{method.__name__}] 평균 실행 시간: {avg_time:.6f}초")

    return result, avg_time
