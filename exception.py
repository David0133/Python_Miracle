"""
Exception handling
"""
var = 0
try:
    var = int(input("Enter the value"))
except Exception:
    print("Invalid value Alphabets are not allowed")
finally:
    print("Running finally")

print(var)
print("Done")
