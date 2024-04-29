# Perceptron em python
# Programa em desenvolvimento
# Falta programar o aprendizado
# Elmar Uhl - 2024

threshold = 1.5 # output value for activate
#inputs = [1, 0, 1, 0, 1]
inputs = [1, 0, 1, 0, 1]
weights = [0.7, 0.6, 0.5, 0.3, 0.4] # Weigths for inputs

# Do the sum over all inputs
sum = 0
i = 0
while (i < len(inputs)):
    sum += inputs[i] * weights[i];
    i += 1

# Set the value of activation
if (sum > 1.5):
    activate = 1
else:
    activate = 0

print(activate)
