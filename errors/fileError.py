try:
    file = open('zeroEror.py')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(file.read())
    file.close()
finally:
    print("Adios Muchachos")
