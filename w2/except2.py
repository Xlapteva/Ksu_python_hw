def get_sum(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        return "Check values"

print(get_sum(1, 4))           