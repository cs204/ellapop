def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):

    feet = float(v.replace('ft', ''))


    conversion_factor = 0.3048


    meters = feet * conversion_factor

    return meters

main()