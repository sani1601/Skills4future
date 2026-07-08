print("--- break example ---")
for i in range(10):
    if i == 5:
        print("Breaking loop at i = 5")
        break
    print(i)

print("--- continue example ---")
for i in range(5):
    if i == 2:
        print("Skipping i = 2")
        continue
    print(i)

print("--- pass example ---")
# pass is a null operation; nothing happens when it executes.
# It's useful as a placeholder when a statement is syntactically required but you don't want any code to run.
def my_function():
    pass # TODO: Implement this function later

print("Function with 'pass' executed.")

for i in range(3):
    if i == 1:
        pass # Do nothing when i is 1
    print(f"Current i: {i}")
