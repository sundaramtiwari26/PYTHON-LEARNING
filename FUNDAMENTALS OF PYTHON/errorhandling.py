try:
    numer=int('abc')
except ValueError as e:
    print(f"error: {e}")
except TypeError as e:
    print(f"error : {e}")
else:
    print("conversion sucessful.")
finally:
    print("cleanup code.")
