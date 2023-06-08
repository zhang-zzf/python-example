def f_to_c(f: float) -> float:
    return (f - 32) / 1.8


f: float = float(input('f='))
c: float = f_to_c(f)
# format output
print('\n%.1f°F=%.1f°C' % (f, c))
# format output
print(f'\n{f:.1f}°F = {c:.1f}°C')

s = 'Hello, World'
print(f'{s}')
