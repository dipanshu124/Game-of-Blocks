This program takes a data input as string and finds a value which when appended to this string, makes the SHA256 hash of the new string less than a target value.

I have used a simple approach - try random values and check if the hash is less than the target or not. If it is we are done, otherwise try with a new random value.
