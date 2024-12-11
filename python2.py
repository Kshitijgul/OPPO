import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Step 1: Define fuzzy variables

# Temperature in the range of 16 to 40 degrees Celsius
temperature = ctrl.Antecedent(np.arange(16, 41, 1), 'temperature')

# Humidity in the range of 0 to 100%
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')

# Cooling Power as a percentage (0-100%)
cooling_power = ctrl.Consequent(np.arange(0, 101, 1), 'cooling_power')

# Fan Speed as a percentage (0-100%)
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Step 2: Define fuzzy membership functions

# Temperature membership functions (Low, Medium, High)
temperature['low'] = fuzz.trapmf(temperature.universe, [16, 16, 20, 25])
temperature['medium'] = fuzz.trimf(temperature.universe, [20, 25, 30])
temperature['high'] = fuzz.trapmf(temperature.universe, [25, 30, 40, 40])

# Humidity membership functions (Low, Medium, High)
humidity['low'] = fuzz.trapmf(humidity.universe, [0, 0, 30, 50])
humidity['medium'] = fuzz.trimf(humidity.universe, [30, 50, 70])
humidity['high'] = fuzz.trapmf(humidity.universe, [50, 70, 100, 100])

# Cooling Power membership functions (Low, Medium, High)
cooling_power['low'] = fuzz.trimf(cooling_power.universe, [0, 0, 50])
cooling_power['medium'] = fuzz.trimf(cooling_power.universe, [25, 50, 75])
cooling_power['high'] = fuzz.trimf(cooling_power.universe, [50, 100, 100])

# Fan Speed membership functions (Low, Medium, High)
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Step 3: Define fuzzy rules

# Cooling Power Rules (more temperature-centric)
rule1 = ctrl.Rule(temperature['high'] & humidity['high'], cooling_power['high'])
rule2 = ctrl.Rule(temperature['high'] & humidity['medium'], cooling_power['medium'])
rule3 = ctrl.Rule(temperature['medium'] & humidity['low'], cooling_power['low'])
rule4 = ctrl.Rule(temperature['low'] & humidity['low'], cooling_power['low'])

# Fan Speed Rules (more humidity-centric)
rule5 = ctrl.Rule(temperature['high'] & humidity['high'], fan_speed['medium'])
rule6 = ctrl.Rule(temperature['high'] & humidity['medium'], fan_speed['low'])
rule7 = ctrl.Rule(temperature['medium'] & humidity['low'], fan_speed['high'])
rule8 = ctrl.Rule(temperature['low'] & humidity['low'], fan_speed['low'])


# Step 4: Control System

# Create the control system for cooling power and fan speed
ac_control = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])

# Create the simulation for the AC control system
ac_simulation = ctrl.ControlSystemSimulation(ac_control)

# Step 5: Simulate the system with a sample input

ac_simulation.input['temperature'] = 30  # Example temperature (in Celsius)
ac_simulation.input['humidity'] = 60   # Example humidity (in %)

# Perform the fuzzy inference computation
ac_simulation.compute()

# Step 6: Display the output

print(f"Cooling Power: {ac_simulation.output['cooling_power']}%")
print(f"Fan Speed: {ac_simulation.output['fan_speed']}%")

# Optionally: Plot the membership functions and results
temperature.view()
humidity.view()
cooling_power.view()
fan_speed.view()
