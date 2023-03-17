# Just a fun little project


year_considered = 2023  # Year being considered
num_ancestors = 2  # Approx. ancestors in considered year
years_per_generation = 20  # Approx. years per generation

user_year = int(input('Enter a past year (neg. for B.C.): '))
print()

while year_considered >= user_year:
    print('Ancestors in {}: {}'.format(year_considered, num_ancestors))

    num_ancestors = num_ancestors * 2
    year_considered = year_considered - years_per_generation
