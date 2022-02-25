def tick_tock(n):
    numbers = list(range(1, n+1))
    for n in range(len(numbers)):
        if numbers % 3 == 0 and numbers % 7 == 0:
            numbers = "TickTock"
        elif numbers % 3 == 0:
            numbers = 'Tick'
        elif numbers % 7 == 0:
            numbers = "Tock"
    
    
    return numbers