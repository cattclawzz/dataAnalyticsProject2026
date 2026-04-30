foo = [0,3,9,12,15]
x = foo[0]
bar = [x]

print(bar)

frames = 15
interval = frames/len(foo)

for i in range(1, frames+1):
    if i % interval == 0:
        bar.append(x+1)
    x = foo[int(i//interval)] + interval/(i%interval)
    bar[-1] = x
    print(bar)