import sys
import numpy as np
from qiskit import (QuantumCircuit, execute, Aer)
from qiskit.visualization import plot_histogram

#   Aer's QASM_Simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a quantum circuit on q register
circuit = QuantumCircuit(2,2)

#Add Hadamar Gate to Qubit 0
circuit.h(0)

#Add a CNOT gate on control qubit 0 and targer qubit 1
circuit.cx(0,1)

#Mapp Quantum Measurement to classical bits
circuit.measure([0,1],[0,1])

#execute the circuit on qasm simulator
job = execute(circuit, simulator, shots = 10000)

#Obtain results
result = job.result()

#Get the counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are: ",counts)
circuit.draw()
plot_histogram(counts)